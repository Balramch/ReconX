import asyncio
import subprocess
from core.logger import log

async def run(domain):
    """Run Assetfinder in subprocess, return set of subdomains"""
    log("[+] Running Assetfinder...")
    try:
        result = subprocess.run(
            ["assetfinder", "--subs-only", domain],
            capture_output=True,
            text=True,
            check=False
        )
        subs = set(result.stdout.splitlines())
        log(f"[+] Assetfinder found {len(subs)} subs")
        return subs
    except Exception as e:
        log(f"[!] Assetfinder failed: {e}")
        return set()