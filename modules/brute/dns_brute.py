import asyncio
from modules.resolver import dns_resolver

WORDLIST = ["www", "api", "mail", "dev", "test", "stage"]  # extendable

async def run(domain, wordlist=None):
    subs = [f"{w}.{domain}" for w in WORDLIST]
    return await dns_resolver.run(subs)