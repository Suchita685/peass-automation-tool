PEASS Automation Tool (linPEAS Wrapper)
======================================
This tool automates Linux privilege escalation enumeration by running linPEAS and extracting only the high-risk findings into a separate, easy-to-read file. 
Instead of manually running linPEAS and scrolling through thousands of lines of output, this tool helps you quickly focus on the most promising privilege escalation paths.
During post-exploitation on a Linux system, privilege escalation is a critical step.  
Although linPEAS performs extensive checks, its output can be overwhelming and time-consuming to analyze manually.

This tool was created to:
- Reduce manual effort during privilege escalation enumeration
- Automatically highlight high-risk misconfigurations
- Improve efficiency during penetration testing and lab environments

What does this tool do
======================
When executed, the tool performs the following actions:

1. Automatically runs `linpeas.sh`
2. Saves the complete linPEAS output for full reference
3. Parses the output and extracts high-risk indicators, including:
   - SUID binaries
   - sudo permissions
   - Writable files and directories
   - Cron jobs
   - Potential root-level misconfigurations
4. Stores results in a structured and organized format

This allows faster identification of privilege escalation opportunities.

Directory Structure
===================
peass-automation-tool/
├── linpeas.sh
├── peass_runner.py
├── output/
│ ├── raw/
│ │ └── linpeas_raw_<timestamp>.txt
│ └── filtered/
│ └── high_risk_findings_<timestamp>.txt
└── README.md

How to use
==========
1. Ensure linPEAS is executable
   chmod +x linpeas.sh
   
2. Run the automation script
   python3 peass_runner.py
The script will automatically execute linPEAS and generate output files.

Viewing the results
===================
Full linPEAS output:
less output/raw/linpeas_raw_<timestamp>.txt

Use this file when a detailed inspection is required.

Filtered high-risk findings (recommended)
less output/filtered/high_risk_findings_<timestamp>.txt

This file contains only the most important privilege escalation indicators and is the primary file to review during analysis.

Typical use cases
=================

Post-exploitation during penetration testing
Red team operations
Capture-the-Flag (CTF) challenges
Learning Linux privilege escalation techniques
Automating repetitive enumeration tasks
   
