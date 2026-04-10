import asyncio
from config.settings import CONCURRENCY

semaphore = asyncio.Semaphore(CONCURRENCY)

async def resolve(sub):
    async with semaphore:
        try:
            loop = asyncio.get_event_loop()
            await loop.getaddrinfo(sub, None)
            return sub
        except:
            return None


async def run(subdomains):
    tasks = [resolve(s) for s in subdomains]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    return {r for r in results if isinstance(r, str)}