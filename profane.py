import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--regexes", help="File with the profane regular expressions", required=True)
parser.add_argument("-s", "--source", help="Source file to be audited", required=True)
parser.add_argument("-d", "--destination", help="Destination file to write clean words to", required=True)
args = parser.parse_args()

f = open(args.source, "r")
w = open(args.destination, "w")
r = open(args.regex, "r")
badwords = []

for line in r:
    badwords.append(line)

for line in f:
    m = ""
    for regex in badwords:
        m = re.search(regex, line)
        if m is not None:
            print("Found! " + line)
            break
    if m is None:
        w.write(line)
