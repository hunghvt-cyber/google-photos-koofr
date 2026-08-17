import json
import os
from datetime import datetime

class ManifestManager:
    def __init__(self, raw_input_path="data/raw_scan.json", manifest_path="data/photos-manifest.json"):
        self.raw_input_path = raw_input_path
        self.manifest_path = manifest_path

    def build_manifest(self):
        print("[Manifest] Dang chuan hoa du lieu sang photos-manifest.json...")
        
        if not os.path.exists(self.raw_input_path):
            raise FileNotFoundError(f"Khong tim thay file scan thô: {self.raw_input_path}")

        with open(self.raw_input_path, "r", encoding="utf-8") as f:
            raw_items = json.load(f)

        manifest_data = {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "total_count": len(raw_items),
            "items": []
        }

        for item in raw_items:
            manifest_data["items"].append({
                "media_id": item.get("id"),
                "filename": item.get("name"),
                "size_bytes": item.get("bytes"),
                "created_at": item.get("created")
            })

        os.makedirs(os.path.dirname(self.manifest_path), exist_ok=True)
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)

        print(f"[Manifest] Da tao manifest thanh cong voi {len(raw_items)} items tại: {self.manifest_path}")
        return manifest_data
