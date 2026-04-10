import asyncio

async def run(domain):
    print("[+] Running Subfinder...")

    process = await asyncio.create_subprocess_exec(
        "subfinder",
        "-d", domain,
        "-all",
        "-recursive",
        "-silent",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    print("STDOUT:", stdout.decode())
    print("STDERR:", stderr.decode())
    print("RETURN CODE:", process.returncode)

    subs = set(stdout.decode().splitlines())
    return subs