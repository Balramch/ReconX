import os
import json

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def save_txt(path, data):
    with open(path, "w") as f:
        for item in sorted(data):
            if item:
                f.write(item + "\n")


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(list(data), f, indent=2)


def clean(data):
    return {
        x.strip().lower()
        for x in data
        if x and "." in x
    }

def extract_domain(line):
    """
    Extract only domain from:
    api.bugcrowd.com | http://api.bugcrowd.com | curl-live
    """
    try:
        return line.split("|")[0].strip()
    except:
        return None


def get_output_dir(platform, program_type, domain):
    """
    Create:
    output/platform/program_type/domain/
    """

    domain_clean = domain.replace(".", "_")

    path = os.path.join(
        "output",
        platform,
        program_type,
        domain_clean
    )

    os.makedirs(path, exist_ok=True)

    return path


    