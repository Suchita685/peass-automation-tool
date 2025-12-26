import subprocess
import datetime
import re
import os

# Paths
LINPEAS_PATH = "./linpeas.sh"
RAW_OUTPUT_DIR = "output/raw"
FILTERED_OUTPUT_DIR = "output/filtered"

def run_linpeas():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_output_file = f"{RAW_OUTPUT_DIR}/linpeas_raw_{timestamp}.txt"
    filtered_output_file = f"{FILTERED_OUTPUT_DIR}/high_risk_findings_{timestamp}.txt"

    print("[+] Running linPEAS...")
    print("[+] This may take a few minutes. Please wait.\n")

    # Run linPEAS and capture output
    with open(raw_output_file, "w") as raw_file:
        subprocess.run(
            ["bash", LINPEAS_PATH],
            stdout=raw_file,
            stderr=subprocess.STDOUT
        )

    print(f"[+] Full linPEAS output saved to: {raw_output_file}")

    extract_high_risk(raw_output_file, filtered_output_file)

def extract_high_risk(raw_file, filtered_file):
    print("[+] Extracting high-risk privilege escalation findings...")

    high_risk_patterns = [
        r"SUID",
        r"sudo",
        r"Writable",
        r"cron",
        r"Capabilities",
        r"Password",
        r"shadow",
        r"passwd",
        r"root"
    ]

    with open(raw_file, "r", errors="ignore") as rf, open(filtered_file, "w") as ff:
        for line in rf:
            for pattern in high_risk_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    ff.write(line)
                    break

    print(f"[+] High-risk findings saved to: {filtered_file}")

if __name__ == "__main__":
    run_linpeas()

