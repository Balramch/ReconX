import aiohttp
import asyncio
from config.settings import CONCURRENCY, TIMEOUT

semaphore = asyncio.Semaphore(CONCURRENCY)

async def check(sub):
    async with semaphore:
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=TIMEOUT)) as session:
                async with session.get(f"http://{sub}") as resp:
                    if resp.status < 400:
                        return sub
        except:
            return None

async def run(subdomains):
    tasks = [check(s) for s in subdomains]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return {r for r in results if isinstance(r, str)}