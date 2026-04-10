from core.utils import get_output_dir, save_txt
from core.subdomain import enumerate_subdomains
from core.resolver import resolve_subdomains
from core.pipeline import run_pipeline
from modules.resolver.dns_resolver import resolve, run

async def run(domain, platform, program_type):
    print(f"[+] Starting ReconX for {domain}")

    # 🔥 CREATE STRUCTURED OUTPUT DIR
    OUTPUT_DIR = get_output_dir(platform, program_type, domain)

    print(f"[+] Output directory: {OUTPUT_DIR}")

    # ==============================
    # 1. SUBDOMAIN ENUMERATION
    # ==============================
    print("[*] Enumerating subdomains...")
    subs = await enumerate_subdomains(domain)

    if not subs:
        print("[-] No subdomains found")
        return

    print(f"[+] Found: {len(subs)}")
    save_txt(f"{OUTPUT_DIR}/subs.txt", subs)

    # ==============================
    # 2. RESOLUTION
    # ==============================
    print("[*] Resolving subdomains...")
    resolved = await resolve_subdomains(subs)

    if not resolved:
        print("[-] No resolved domains")
    else:
        print(f"[+] Resolved: {len(resolved)}")

    save_txt(f"{OUTPUT_DIR}/resolved.txt", resolved)

    # ==============================
    # 3. LIVE HOST PROBING (HTTPX)
    # ==============================
    print("[*] Probing live hosts...")
    live = await run_pipeline(domain, OUTPUT_DIR)

    if not live:
        print("[-] No live hosts found")
    else:
        print(f"[+] Live hosts found: {len(live)}")

    save_txt(f"{OUTPUT_DIR}/live.txt", live)

    print("[+] Recon Completed 🚀")