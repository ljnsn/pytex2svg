
pytex2svg
===

A simple command line tool written in Python to convert TeX equations to SVG. Input can be read from `stdin`, provided directly as command line argument, or read from a file.

Installation
---

`pip install pytex2svg`

Dependencies
---

-   `matplotlib`

Usage
---

```
usage: pytex2svg [-h] [-o OUTFILE] [-v] [input]

converts a TeX string to an SVG file

positional arguments:
  input                 The TeX equation or file to be converted to svg,
                        defaults to stdin

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Path or name of the output file, defaults to
                        "equation.svg". If more than one equation is provided,
                        the output files are numbered.
  -v, --verbose         Enable verbose output
```

Examples:
```bash
# from stdin
echo "\log_{2}10 \approx 3.322" | pytex2svg -o whybinary.svg
# as command line argument
pytex2svg "\log_{2}10 \approx 3.322" -o whybinary.svg
# from a file
pytex2svg examples/integral.tex -o whybinary.svg
```
