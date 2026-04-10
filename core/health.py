import shutil
import subprocess

TOOLS = ["subfinder", "assetfinder", "findomain", "curl"]

def check_tool(tool):
    return shutil.which(tool) is not None


def run_tool_check():
    status = {}

    for t in TOOLS:
        status[t] = check_tool(t)

    return status


def print_health():
    status = run_tool_check()

    print("\n[+] TOOL HEALTH REPORT")
    for k, v in status.items():
        state = "OK" if v else "MISSING"
        print(f" - {k}: {state}")

    return status