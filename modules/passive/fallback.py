# modules/passive/fallback.py

async def run(domain):
    print("[!] Using fallback module only")  # debug message
    # fallback subdomains
    return {
        f"www.{domain}",
        f"api.{domain}",
        f"mail.{domain}"
    }