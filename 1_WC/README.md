# ccwc: Implementation of the `wc` Command

This project is an implementation of the Unix `wc` (word count) command in Python, called `wc` (Custom Word Count) . Tests taken from https://codingchallenges.fyi/challenges/challenge-wc

## Features

- Counts the number of **lines** (`-l`), **words** (`-w`), and **bytes** (`-c`) in a file or from **standard input (stdin)**.
- Supports multiple flags and can display multiple counts simultaneously.
- If no flag is provided, it outputs **all counts** (lines, words, and bytes) by default.
- Can read input from a **file** or **stdin** if no filename is specified.

## Usage
1. Using file
```bash
python wc.py [OPTIONS] [FILE]

python wc.py -l -w -c test.txt
```
### output:
```yaml
7143 test.txt  # Lines
60176 test.txt # Words
342181 test.txt # Bytes
```
2. using stdin

```bash
echo "This is a test" | python wc.py
```

```yaml
1       # Lines
4       # Words
15      # Bytes
```
## ToDO :
Explore how to call the script directly in the terminal without needing to type `python


