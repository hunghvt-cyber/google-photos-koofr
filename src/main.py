import argparse

def main():
    parser = argparse.ArgumentParser(description="Google Photos to Koofr Sync Engine")
    parser.add_argument("--step", choices=["scan", "manifest", "compare", "plan", "safety", "sync"])
    parser.add_argument("--dry-run", action="store_true")
    
    args = parser.parse_args()

    if args.dry_run:
        print("[INFO] Che do DRY-RUN: Khong co thay doi nao duoc thuc hien.")

    print(f"[OK] Khoi tao khung he thong thanh cong. Buoc: {args.step or 'ALL'}")

if __name__ == "__main__":
    main()
