import json
import os
from datetime import datetime

class SyncPlanner:
    def __init__(self, plan_path="data/sync-plan.json"):
        self.plan_path = plan_path

    def create_plan(self, compare_result):
        print("[Planner] Dang lap ke hoach dong bo...")

        actions = []
        for item in compare_result["new"]:
            actions.append({"action": "UPLOAD", "filename": item["filename"], "media_id": item["media_id"]})
        for item in compare_result["deleted"]:
            actions.append({"action": "DELETE", "filename": item["filename"]})

        plan_data = {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "summary": {
                "upload": len(compare_result["new"]),
                "delete": len(compare_result["deleted"]),
                "unchanged": len(compare_result["unchanged"])
            },
            "actions": actions
        }

        os.makedirs(os.path.dirname(self.plan_path), exist_ok=True)
        with open(self.plan_path, "w", encoding="utf-8") as f:
            json.dump(plan_data, f, indent=2)

        print(f"[Planner] Da tao sync-plan.json thanh cong voi {len(actions)} hanh dong.")
        return plan_data
