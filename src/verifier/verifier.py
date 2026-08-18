import os

class FileVerifier:
    def verify_and_cleanup(self, local_path, success_upload=True):
        if success_upload:
            print(f"[Verifier] VERIFIED: File {local_path} da upload thanh cong. Dang xoa file tam...")
            if os.path.exists(local_path):
                os.remove(local_path)
            return True
        else:
            print(f"[Verifier] FAILED: Upload {local_path} thất bại. Giu lai file tam!")
            return False
