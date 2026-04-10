import asyncio
from core.logger import log

WORDLIST = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"

async def run(domain, wordlist):
    log("[+] Running PureDNS with smart wordlist...")

    process = await asyncio.create_subprocess_exec(
        "puredns",
        "bruteforce",
        wordlist,
        domain,
        "--quiet",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, _ = await process.communicate()

    return set(stdout.decode().splitlines())