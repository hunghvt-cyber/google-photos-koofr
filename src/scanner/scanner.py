import os
import subprocess
import json

class GooglePhotosScanner:
    def __init__(self, output_path="data/raw_scan.json"):
        self.output_path = output_path

    def run(self):
        print("[Scanner] Dang quet du lieu thuc tu Google Photos...")
        
        # Đảm bảo thư mục đầu ra tồn tại
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        
        # Tạo file session từ Secret (GitHub Actions sẽ làm bước này)
        if os.environ.get("GPHOTOS_SESSION_CONTENT"):
            with open("session.json", "w") as f:
                f.write(os.environ["GPHOTOS_SESSION_CONTENT"])

        try:
            # Gọi gphotos-cdp (phiên bản Go của greghesp)
            # -session: dùng file session đã tạo
            # -output: xuất ra file raw_scan.json
            # Lưu ý: gphotos-cdp không có lệnh 'list' và dùng single dash (-)
            subprocess.run(["gphotos-cdp", "-session", "session.json", "-output", self.output_path], check=True)
            print(f"[Scanner] Quet thanh cong!")
            return True
        except Exception as e:
            print(f"[Scanner] LOI: {e}")
            return False
