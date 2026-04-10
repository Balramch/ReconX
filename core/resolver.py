import asyncio
import socket


async def resolve_subdomains(subdomains):
    print("[*] Resolving subdomains...")

    resolved = set()

    async def check(sub):
        try:
            socket.gethostbyname(sub)
            return sub
        except:
            return None

    results = await asyncio.gather(*[check(s) for s in subdomains])

    for r in results:
        if r:
            resolved.add(r)

    print(f"[+] Resolved: {len(resolved)}")

    return list(resolved)