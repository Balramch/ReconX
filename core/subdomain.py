import asyncio
import socket
from core.config import TOOLS


# -----------------------------
# CLEANING
# -----------------------------
def clean_subdomains(subs):
    cleaned = set()

    for s in subs:
        s = s.strip().lower()

        if not s:
            continue
        if "*" in s:
            continue
        if len(s.split(".")) < 2:
            continue

        cleaned.add(s)

    return cleaned


# -----------------------------
# RUN COMMAND
# -----------------------------
async def run_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    out, _ = await proc.communicate()
    return out.decode().splitlines()


async def run_retry(cmd, retries=2):
    for _ in range(retries):
        try:
            return await asyncio.wait_for(run_cmd(cmd), timeout=180)
        except:
            pass

    return []


# -----------------------------
# ENUMERATION (ALL TOOLS)
# -----------------------------
async def enumerate_subdomains(domain):
    print("[*] Running tools...")

    tasks = [
        run_retry(cmd.format(domain=domain))
        for cmd in TOOLS.values()
    ]

    results = await asyncio.gather(*tasks)

    subs = set()
    for r in results:
        subs.update(r)

    print(f"[+] Raw subs: {len(subs)}")

    return clean_subdomains(subs)


# -----------------------------
# RESOLVER
# -----------------------------
async def resolve(subs):
    print("[*] Resolving subdomains...")

    async def check(s):
        try:
            socket.gethostbyname(s)
            return s
        except:
            return None

    results = await asyncio.gather(*[check(s) for s in subs])

    resolved = {r for r in results if r}

    print(f"[+] Resolved: {len(resolved)}")

    return resolved