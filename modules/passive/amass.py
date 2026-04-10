import asyncio
from core.logger import log

async def run(domain, timeout=120):
    log("[+] Running Amass...")

    try:
        process = await asyncio.create_subprocess_exec(
            "amass",
            "enum",
            "-passive",
            "-d", domain,
            "-silent",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, _ = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )
        except asyncio.TimeoutError:
            log(f"[!] Amass exceeded {timeout}s → killing process")
            process.kill()  # 🔥 THIS IS THE REAL FIX
            return set()

        subs = set(stdout.decode().splitlines())
        log(f"[+] Amass found {len(subs)} subs")

        return subs

    except Exception as e:
        log(f"[!] Amass error: {e}")
        return set()