import argparse
import sys
from src.scanner.scanner import GooglePhotosScanner
from src.manifest.manifest import ManifestManager
from src.compare.compare import PhotoComparer
from src.planner.planner import SyncPlanner
from src.safety.safety import SafetyGuardrail

def main():
    parser = argparse.ArgumentParser(description="Google Photos to Koofr Sync Engine")
    parser.add_argument("--step", choices=["scan", "manifest", "compare", "plan", "safety", "sync"])
    parser.add_argument("--dry-run", action="store_true")
    
    args = parser.parse_args()

    if args.dry_run:
        print("[INFO] Che do DRY-RUN: Khong ghi/xoa du lieu tren Koofr.")

    # [1] Scan & Manifest
    if args.step in ["scan", "manifest", None]:
        scanner = GooglePhotosScanner()
        if not scanner.run():
            sys.exit(1)
        manifest_mgr = ManifestManager()
        manifest_mgr.build_manifest()

    # [2] Compare & Plan
    if args.step in ["compare", "plan", None]:
        comparer = PhotoComparer()
        diff = comparer.compare()
        planner = SyncPlanner()
        planner.create_plan(diff)

    # [3] Safety Check
    if args.step in ["safety", None]:
        safety = SafetyGuardrail()
        if not safety.validate():
            print("[CRITICAL] Dung chu trinh vi nguy co mat an toan du lieu!")
            sys.exit(1)

if __name__ == "__main__":
    main()
