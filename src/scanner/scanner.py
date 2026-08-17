import json
import os
import subprocess

class GooglePhotosScanner:
    def __init__(self, output_path="data/raw_scan.json"):
        self.output_path = output_path

    def run(self):
        print("[Scanner] Dang quet danh sach anh tu Google Photos via gphotos-cdp...")
        
        # Đảm bảo thư mục chứa file output tồn tại
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        # Lệnh chạy gphotos-cdp (chạy trên GitHub Actions Runner)
        # Tạm thời tạo mock data nếu chạy thử nghiệm cục bộ
        try:
            # Lệnh thực tế sẽ gọi CLI của gphotos-cdp
            # subprocess.run(["gphotos-cdp", "list", "--out", self.output_path], check=True)
            
            # Giả lập dữ liệu scan để kiểm thử luồng
            mock_data = [
                {"id": "photo_001", "name": "2026/08/IMG_0001.jpg", "bytes": 2048000, "created": "2026-08-17T10:00:00Z"},
                {"id": "photo_002", "name": "2026/08/IMG_0002.jpg", "bytes": 5120000, "created": "2026-08-17T11:00:00Z"}
            ]
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(mock_data, f, indent=2)
                
            print(f"[Scanner] Quet thanh cong. Luu ket qua thô tai: {self.output_path}")
            return True
        except Exception as e:
            print(f"[Scanner] LOI trong qua trinh quet: {e}")
            return False
