# apt-search

*Search Ubuntu packages.*

## Motivation

I needed a way to find the right package for missing header files.
I tried `apt-file`, but for some reason it was constantly complaining with

```
E: The cache is empty. You need to run "apt-file update" first.
```

The alternative was to search the Ubuntu packages in the browser, but I wanted a tool for the CLI.
So I had the idea to parse the HTML search result and give a nice terminal output.

## Installation

Use `pip` or `pipx` for installation:

```bash
pip install --user apt-search
# or
pipx install apt-search
```

## Usage

Just execute the `apt-search` command with the filename you are looking for:

```bash
apt-search --help
# Usage: main.py [OPTIONS] FILENAME
#
# Arguments:
#   FILENAME  [required]
#
# Options:
#   --suite TEXT                    [default: jammy]
#   --arch TEXT                     [default: any]
#   --help                          Show this message and exit.
```
