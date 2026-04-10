TOOLS = {
    "subfinder": "subfinder -d {domain} -all -silent",
    "assetfinder": "assetfinder --subs-only {domain}",
    "findomain": "findomain -t {domain} -q"
}

HTTPX = "httpx-toolkit -l {input} -silent -no-color -threads 50 -timeout 10 -status-code -title -follow-redirects"

RESOLVERS = "/usr/share/wordlists/resolvers.txt"  # update if needed

OUTPUT_DIR = "output"
TIMEOUT = 120
RETRIES = 2

