# profane

## Description

Very simple (and probably inefficient) Python script to crawl a plaintext file and look for profanity. What is deemed profane is in a regex file (**regexes.txt** is a good one to start with for *most* English profanity).

Has been tested with both Python2 and Python3.

## Usage

Very easy to use

```
python profane.py -r regexes.txt -s potential-bad-words.txt -d clean.txt
```

| Command-line Option       | Required? | Description               |
|---------------------------|-----------|---------------------------|
| `-r` / `--regexes`        | Yes       | File with profane regexes |
| `-s` / `--source`         | Yes       | File to be audited        |
| `-d` / `--destination`    | Yes       | Clean file to save to     |
| `-v` / `--verbose`        | No        | Show clean lines as well  |
