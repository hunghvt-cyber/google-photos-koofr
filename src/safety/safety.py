import json
import yaml

class SafetyGuardrail:
    def __init__(self, config_path="config/config.yml", plan_path="data/sync-plan.json", manifest_path="data/photos-manifest.json"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)["safety"]
        self.plan_path = plan_path
        self.manifest_path = manifest_path

    def validate(self):
        print("[Safety] Dang kiem tra cac quy tac an toan...")

        with open(self.manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        with open(self.plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)

        total_scanned = manifest.get("total_count", 0)
        delete_count = plan["summary"]["delete"]
        total_items = total_scanned + delete_count

        # Quy tắc 1: Tổng số file scan được phải đủ lớn
        if total_scanned < self.config["min_expected_items"]:
            print(f"[SAFETY ERROR] So luong file scan qua it ({total_scanned} < {self.config['min_expected_items']}). Kich hoat NGAT TU DONG!")
            return False

        # Quy tắc 2: Số file bị xóa không quá giới hạn tuyệt đối
        if delete_count > self.config["max_delete_absolute"]:
            print(f"[SAFETY ERROR] So luong file can xoa ({delete_count}) vuot gioi han cho phép ({self.config['max_delete_absolute']}).")
            return False

        # Quy tắc 3: Tỷ lệ xóa không vượt quá % cho phép
        if total_items > 0:
            delete_ratio = delete_count / total_items
            if delete_ratio > self.config["max_delete_ratio"]:
                print(f"[SAFETY ERROR] Ty le xoa ({delete_ratio:.2%}) vuot nguong an toan ({self.config['max_delete_ratio']:.2%}).")
                return False

        print("[Safety] PASSED - Ke hoach dong bo an toan!")
        return True
