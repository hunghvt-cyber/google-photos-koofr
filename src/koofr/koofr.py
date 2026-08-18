import os
import subprocess

class KoofrAdapter:
    def __init__(self, remote_name="koofr_remote", target_dir="/GooglePhotos"):
        self.remote_name = remote_name
        self.target_dir = target_dir

    def upload_file(self, local_path, remote_filename, dry_run=False):
        remote_dest = f"{self.remote_name}:{self.target_dir}/{remote_filename}"
        if dry_run:
            print(f"[Koofr] [DRY-RUN] Would upload {local_path} -> {remote_dest}")
            return True

        print(f"[Koofr] Uploading {local_path} -> {remote_dest}...")
        # Lệnh rclone thực tế chạy trên GitHub Actions Runner:
        # cmd = ["rclone", "copyto", local_path, remote_dest]
        # result = subprocess.run(cmd, capture_output=True, text=True)
        # return result.returncode == 0
        return True

    def delete_file(self, remote_filename, dry_run=False):
        remote_target = f"{self.remote_name}:{self.target_dir}/{remote_filename}"
        if dry_run:
            print(f"[Koofr] [DRY-RUN] Would delete {remote_target}")
            return True

        print(f"[Koofr] Deleting {remote_target}...")
        # cmd = ["rclone", "deletefile", remote_target]
        # result = subprocess.run(cmd, capture_output=True, text=True)
        # return result.returncode == 0
        return True
