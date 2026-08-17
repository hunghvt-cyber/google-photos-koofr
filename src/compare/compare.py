import json

class PhotoComparer:
    def __init__(self, manifest_path="data/photos-manifest.json", koofr_state_path="data/koofr_state.json"):
        self.manifest_path = manifest_path
        self.koofr_state_path = koofr_state_path

    def compare(self):
        print("[Compare] Dang so sanh Google Photos vs Koofr...")
        
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        # Mock dữ liệu Koofr nếu chưa có file state thật
        koofr_items = {}
        try:
            with open(self.koofr_state_path, "r", encoding="utf-8") as f:
                koofr_items = json.load(f)
        except FileNotFoundError:
            print("[Compare] Chua co koofr_state.json, gia dinh Koofr dang trong.")

        gphotos_items = {item["filename"]: item for item in manifest.get("items", [])}

        new_files = []
        unchanged_files = []
        deleted_files = []

        for filename, item in gphotos_items.items():
            if filename not in koofr_items:
                new_files.append(item)
            else:
                unchanged_files.append(item)

        for filename, item in koofr_items.items():
            if filename not in gphotos_items:
                deleted_files.append(item)

        result = {
            "new": new_files,
            "unchanged": unchanged_files,
            "deleted": deleted_files
        }
        
        print(f"[Compare] Ket qua: New={len(new_files)}, Unchanged={len(unchanged_files)}, Deleted={len(deleted_files)}")
        return result
