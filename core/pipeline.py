import asyncio
from core.probe import (
    build_httpx_input,
    write_httpx_input,
    probe_httpx,
    filter_live
)

from core.config import OUTPUT_DIR


# -----------------------------
# MAIN PIPELINE
# -----------------------------
async def run_pipeline(domain, OUTPUT_DIR):
    """
    Full recon flow:
    subs → merge → clean → httpx → live
    """

    # print(f"[+] Starting pipeline for: {domain}")

    subs_file = f"{OUTPUT_DIR}/subs.txt"
    resolved_file = f"{OUTPUT_DIR}/resolved.txt"

    # STEP 1: MERGE INPUTS
    domains = build_httpx_input(subs_file, resolved_file)

    print("[DEBUG] Total cleaned domains:", len(domains))
    # print("[DEBUG] Sample:", domains[:10])

    if not domains:
        print("[-] No domains found. STOPPING.")
        return []

    # STEP 2: WRITE CLEAN INPUT
    httpx_input = write_httpx_input(domains)

    print("[+] HTTPX input file created:", httpx_input)

    # STEP 3: RUN HTTPX
    raw_results = await probe_httpx(httpx_input)

    print("[DEBUG] Raw httpx lines:", len(raw_results))

    # STEP 4: FILTER LIVE
    live = filter_live(raw_results)

    print(f"[+] Live hosts found: {len(live)}")

    # STEP 5: SAVE OUTPUT
    live_file = f"{OUTPUT_DIR}/live.txt"

    with open(live_file, "w") as f:
        for l in live:
            f.write(l + "\n")

    print("[+] Saved:", live_file)

    return live












    