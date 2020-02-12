import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--regexes", help="File with the profane regular expressions", required=True)
parser.add_argument("-s", "--source", help="Source file to be audited", required=True)
parser.add_argument("-d", "--destination", help="Destination file to write clean words to", required=True)
parser.add_argument("-v", "--verbose", help="Display clean lines as well", action="store_true")
args = parser.parse_args()

f = open(args.source, "r")
w = open(args.destination, "w")
r = open(args.regexes, "r")
badwords = []

for line in r:
    badwords.append(line)

for line in f:
    m = ""
    for regex in badwords:
        m = re.search(regex, line)
        if m is not None:
            print("\033[31m[-] Found: \033[0m" + line)
            break
    if m is None:
        if args.verbose:
            print("\033[32m[+] Clean: \033[0m" + line) 
        w.write(line)
