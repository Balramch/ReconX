import asyncio
from core.logger import log

WORDLIST = "/usr/share/wordlists/subdomains.txt"  # adjust path

async def run(domain, wordlist=None):
    log("[+] Running Gobuster...")

    try:
        process = await asyncio.create_subprocess_exec(
            "gobuster", "dns",
            "-d", domain,
            "-w", WORDLIST,
            "-q",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, _ = await process.communicate()

        subs = set()
        for line in stdout.decode().splitlines():
            if domain in line:
                subs.add(line.strip())

        log(f"[+] Gobuster found {len(subs)} subs")
        return subs

    except Exception as e:
        log(f"[!] Gobuster failed: {e}")
        return set()