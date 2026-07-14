import sys
import subprocess

# The user's typed-in text arrives here from the command line
user_input = sys.argv[1]

# Risky: builds a system command straight from that untrusted input
subprocess.call("generate_report " + user_input, shell=True)
