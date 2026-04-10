import argparse
import asyncio
import sys

# Import your core runner
from core.runner import run
#from core.runner import enumerate_subdomains, resolve
from core.pipeline import run_pipeline
from core.utils import ensure_dir, save_txt
from core.config import OUTPUT_DIR


def banner():
    print("=" * 50)
    print("        ReconX - Recon Automation Tool")
    print("=" * 50)


def parse_args():
    parser = argparse.ArgumentParser(
        description="ReconX - Automated Recon Tool"
    )

    parser.add_argument(
        "-d",
        "--domain",
        required=True,
        help="Target domain (e.g. example.com)"
    )

    # parser.add_argument(
    #     "-p",
    #     "--platform",
    #     required=True,
    #     choices=["bugcrowd", "hackerone", "others"],
    #     help="Platform name"
    # )

    # parser.add_argument(
    #     "-t",
    #     "--type",
    #     required=True,
    #     help="Program type (bpp / vdp / misc)"
    # )

     # 🔥 NOW OPTIONAL
    parser.add_argument(
        "-p",
        "--platform",
        choices=["bugcrowd", "hackerone", "others"],
        default="others",
        help="Platform (default: others)"
    )

    # 🔥 NOW OPTIONAL
    parser.add_argument(
        "-t",
        "--type",
        default="misc",
        help="Program type (default: misc)"
    )

    return parser.parse_args()


async def main():
    banner()

    args = parse_args()

    domain = args.domain.strip()
    platform = args.platform.strip().lower()
    program_type = args.type.strip().lower()

    # Basic validation
    if not domain:
        print("[-] Domain cannot be empty")
        sys.exit(1)

    print(f"[+] Target       : {domain}")
    print(f"[+] Platform     : {platform}")
    print(f"[+] Program Type : {program_type}")
    print("-" * 50)

    try:
        # 🔥 Call your main pipeline
        await run(domain, platform, program_type)

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(0)

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


# ✅ ENTRY POINT
if __name__ == "__main__":
    asyncio.run(main())