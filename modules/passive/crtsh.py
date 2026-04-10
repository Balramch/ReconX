import aiohttp

async def run(domain):
    # 🚨 HARD STOP if wrong type
    if not isinstance(domain, str):
        raise ValueError(f"[FATAL] crtsh received invalid domain: {domain}")

    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    print(f"[DEBUG] Fetching: {url}")

    subs = set()

    try:
        connector = aiohttp.TCPConnector(ssl=False)

        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as resp:
                data = await resp.json(content_type=None)

                for entry in data:
                    names = entry.get("name_value", "")
                    for sub in names.split("\n"):
                        if domain in sub:
                            subs.add(sub.strip())

    except Exception as e:
        print(f"[!] crt.sh error: {e}")

    return subs