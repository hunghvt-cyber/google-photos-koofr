import argparse
from src.scanner.scanner import GooglePhotosScanner
from src.manifest.manifest import ManifestManager

def main():
    parser = argparse.ArgumentParser(description="Google Photos to Koofr Sync Engine")
    parser.add_argument("--step", choices=["scan", "manifest", "compare", "plan", "safety", "sync"])
    parser.add_argument("--dry-run", action="store_true")
    
    args = parser.parse_args()

    if args.dry_run:
        print("[INFO] Che do DRY-RUN: Khong co thay doi nao duoc thuc hien.")

    # [1] Step Scan & Manifest
    if args.step in ["scan", "manifest", None]:
        scanner = GooglePhotosScanner()
        if scanner.run():
            manifest_mgr = ManifestManager()
            manifest_mgr.build_manifest()

if __name__ == "__main__":
    main()
