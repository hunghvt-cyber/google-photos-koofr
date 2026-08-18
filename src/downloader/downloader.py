import os
import json

class PhotoDownloader:
    def __init__(self, plan_path="data/sync-plan.json", download_dir="data/tmp"):
        self.plan_path = plan_path
        self.download_dir = download_dir

    def download_pending(self):
        print("[Downloader] Dang tai các file can thiet ve bo nho tam...")
        
        if not os.path.exists(self.plan_path):
            raise FileNotFoundError(f"Khong tim thay plan: {self.plan_path}")

        with open(self.plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)

        os.makedirs(self.download_dir, exist_ok=True)
        downloaded_files = []

        for item in plan.get("actions", []):
            if item.get("action") == "UPLOAD":
                filename = item["filename"]
                local_file_path = os.path.join(self.download_dir, os.path.basename(filename))
                
                # Trong thuc te, gphotos-cdp se tai file that tai day
                # Tam thoi tao file gia dinh de kiem thu luong
                with open(local_file_path, "w", encoding="utf-8") as temp_f:
                    temp_f.write(f"Mock content for {filename}")
                
                print(f"[Downloader] Da tai: {filename} -> {local_file_path}")
                downloaded_files.append({
                    "filename": filename,
                    "local_path": local_file_path
                })

        return downloaded_files
