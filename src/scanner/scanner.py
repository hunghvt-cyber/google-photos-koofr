import os
import subprocess
import json

class GooglePhotosScanner:
    def __init__(self, output_path="data/raw_scan.json"):
        self.output_path = output_path

    def run(self):
        print("[Scanner] Dang quet du lieu thuc tu Google Photos...")
        
        # Tạo file session từ Secret (GitHub Actions sẽ làm bước này)
        if os.environ.get("GPHOTOS_SESSION_CONTENT"):
            with open("session.json", "w") as f:
                f.write(os.environ["GPHOTOS_SESSION_CONTENT"])

        try:
            # Gọi gphotos-cdp list
            # --session: dùng file session đã tạo
            # --out: xuất ra file raw_scan.json
            subprocess.run(["gphotos-cdp", "list", "--session", "session.json", "--out", self.output_path], check=True)
            print(f"[Scanner] Quet thanh cong!")
            return True
        except Exception as e:
            print(f"[Scanner] LOI: {e}")
            return False
