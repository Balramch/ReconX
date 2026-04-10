def generate(domain):
    base = domain.split(".")[0]

    common = [
        "dev", "test", "stage", "staging", "prod",
        "api", "admin", "beta", "internal",
        "vpn", "mail", "gateway", "dashboard"
    ]

    words = set()

    for word in common:
        words.add(word)
        words.add(f"{word}-{base}")
        words.add(f"{base}-{word}")

    return words