import asyncio
from core.config import HTTPX, OUTPUT_DIR


# -----------------------------
# BUILD CLEAN HTTPX INPUT
# -----------------------------
def build_httpx_input(*files):
    """
    Merge subs + resolved → clean domains only
    """

    clean = set()

    for file in files:
        try:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    # remove junk formats like:
                    # domain | curl-live
                    if "|" in line:
                        line = line.split("|")[0].strip()

                    # normalize URLs
                    line = line.replace("http://", "").replace("https://", "")
                    line = line.strip("/")

                    if "." in line:
                        clean.add(line.lower())

        except FileNotFoundError:
            continue

    return sorted(clean)


# -----------------------------
# WRITE CLEAN INPUT FILE
# -----------------------------
def write_httpx_input(domains, path=f"{OUTPUT_DIR}/httpx_input.txt"):
    with open(path, "w") as f:
        for d in domains:
            f.write(d + "\n")

    return path


# -----------------------------
# HTTPX PROBE ENGINE
# -----------------------------
async def probe_httpx(input_file):
    """
    Run httpx-toolkit on clean input file
    """

    cmd = HTTPX.format(input=input_file)

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    out, err = await proc.communicate()

    # DEBUG (IMPORTANT)
    if err:
        print("[HTTPX ERROR]", err.decode())

    raw_output = out.decode().splitlines()
    return raw_output


# -----------------------------
# PARSER (OPTIONAL CLEAN FORMAT)
# -----------------------------
def parse_httpx_line(line):
    """
    Convert: domain status → domain [status]
    """

    parts = line.strip().split()
    if not parts:
        return None

    host = parts[0]

    status = None
    for p in parts:
        if p.isdigit() and len(p) == 3:
            status = p
            break

    if host and status:
        return f"{host} [{status}]"

    return None


# -----------------------------
# FILTER LIVE RESULTS
# -----------------------------
def filter_live(results):
    clean = set()

    for r in results:
        r = r.strip()

        if not r:
            continue

        if "http" in r:
            host = r.split()[0]
            host = host.replace("https://", "").replace("http://", "").strip("/")

            clean.add(host)

    return sorted(clean)

# -----------------------------
# OPTIONAL: ONLY DOMAINS
# -----------------------------
def extract_domains_only(results):
    """
    Strip everything → only domains
    """

    clean = set()

    for r in results:
        if not r:
            continue

        domain = r.split()[0].strip().lower()

        if "." in domain:
            clean.add(domain)

    return sorted(clean)