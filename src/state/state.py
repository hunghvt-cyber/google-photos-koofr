import json
import os
from datetime import datetime

class StateManager:
    def __init__(self, state_path="data/koofr_state.json"):
        self.state_path = state_path

    def load_state(self):
        """Đọc danh sách các file đã có trên Koofr từ State DB"""
        if not os.path.exists(self.state_path):
            print(f"[State] Chua tim thấy {self.state_path}. Khoi tao State trong.")
            return {}
        
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"[State] Da tai thành cong state voi {len(data)} items.")
                return data
        except Exception as e:
            print(f"[State] LOI doc file state: {e}. Tra ve state trong.")
            return {}

    def update_state(self, plan_path="data/sync-plan.json", dry_run=False):
        """Cập nhật State DB sau khi Sync/Upload/Delete hoàn tất"""
        print("[State] Dang cap nhat State DB...")
        
        if not os.path.exists(plan_path):
            print("[State] Khong tim thay sync-plan.json. Bỏ qua cap nhat.")
            return

        state_data = self.load_state()

        with open(plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)

        changes = 0
        for action_item in plan.get("actions", []):
            action = action_item.get("action")
            filename = action_item.get("filename")

            if action == "UPLOAD":
                # Thêm/Cập nhật file đã upload thành công
                state_data[filename] = {
                    "synced_at": datetime.utcnow().isoformat() + "Z",
                    "status": "SYNCED",
                    "media_id": action_item.get("media_id")
                }
                changes += 1
            elif action == "DELETE":
                # Xóa file khỏi State DB nếu đã xóa trên Koofr
                if filename in state_data:
                    del state_data[filename]
                    changes += 1

        if dry_run:
            print(f"[State] [DRY-RUN] Gia lap cap nhat {changes} thay doi vao State DB.")
            return

        os.makedirs(os.path.dirname(self.state_path), exist_ok=True)
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2)

        print(f"[State] Da ghi {changes} thay doi vao {self.state_path} thanh cong!")
