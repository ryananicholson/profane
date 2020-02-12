# profane

## Description

Very simple (and probably inefficient) Python script to crawl a plaintext file and look for profanity. What is deemed profane is in a regex file (**regexes.txt** is a good one to start with for *most* English profanity).

Has been tested with both Python2 and Python3.

## Usage

Very easy to use

```
python profane.py -r regexes.txt -s potential-bad-words.txt -d clean.txt
```

| Command-line Option       | Description               |
|---------------------------|---------------------------|
| `-r` / `--regexes`        | File with profane regexes |
| `-s` / `--source`         | File to be audited        |
| `-d` / `--destination`    | Clean file to save to     |
| `-v` / `--verbose`        | Show clean lines as well  |
