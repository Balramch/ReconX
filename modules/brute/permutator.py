def mutate(subdomains):
    prefixes = ["dev", "test", "stage", "prod", "beta"]

    new = set()

    for sub in subdomains:
        try:
            parts = sub.split(".")
            name = parts[0]

            for p in prefixes:
                new.add(f"{p}-{name}")
                new.add(f"{name}-{p}")

        except:
            continue

    return new