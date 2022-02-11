# Project info:

This project contains the program and supporting files to find SLCSP (see Original Problem Statement below for explanation).

The repository contains all required helper files to successfully run it.


# Program execution steps:

In order to run this program, clone the repo, change directory into project and run following at command line provided that 
Python interpreter can be found in the OS' search path:

# python slcsp.py

If Python interpreter is not in the path then provide absolute path to it, which normally is found under /usr/bin directory
on a unix system.




This program has been tested in Ubuntu 20.04 running in WSL on Windows 10 platform. Specifics are as follows (with commands to
verify against in parentheses at command prompt):

# Dependancies of tested enviornment

- OS platform (ver):
	Microsoft Windows 10 [Version 10.0.19044.1526]

- WSL (wsl --status):

	Default Distribution: Ubuntu-20.04
	Default Version: 1

	Kernel version: 5.10.60.1

- Python env (python --version): 
	version 2.7.18


# Program output:

Upon reaching proper setup, the execution of the program will be display following output:

zipcode,rate
64148,245.2 
67118,212.35
40813,      
18229,231.48
51012,252.76
79168,243.68
54923,      
67651,249.44
49448,221.63
27702,283.08
47387,326.98
50014,287.3 
33608,268.49
06239,      
54919,243.77
46706,      
14846,      
48872,      
43343,      
77052,243.72
07734,      
95327,      
12961,      
26716,291.76
48435,      
53181,306.56
52654,242.39
58703,297.93
91945,
52146,254.56
56097,
21777,
42330,
38849,285.69
77586,243.72
39745,265.73
03299,240.45
63359,
60094,209.95
15935,184.97
39845,325.64
48418,
28411,307.51
37333,219.29
75939,234.5
07184,
86313,292.9
61232,222.38
20047,
47452,
31551,290.6






#### Original Problem Statement (from https://homework.adhoc.team/slcsp/):

# SLCSP

## Calculate the second lowest cost silver plan

## Problem

You've been asked to determine the second lowest cost silver plan (SLCSP) for
a group of ZIP codes.

## Task

You've been given a CSV file, `slcsp.csv`, which contains the ZIP codes in the
first column. Fill in the second column with the rate (see below) of the
corresponding SLCSP and emit the answer on `stdout` using the same CSV format as
the input. Write your code in your best programming language.

### Expected output

The order of the rows in your answer as emitted on stdout must stay the same as how they
appeared in the original `slcsp.csv`. The first row should be the column headers: `zipcode,rate`
The remaining lines should output unquoted values with two digits after the decimal
place of the rates, for example: `64148,245.20`.

It may not be possible to determine a SLCSP for every ZIP code given; for example, if there is only one silver plan available, there is no _second_ lowest cost plan. Check for cases where a definitive answer cannot be found and leave those cells blank in the output (no quotes or zeroes or other text). For example, `40813,`.

## Additional information

The SLCSP is the so-called "benchmark" health plan in a particular area. It's
used to compute the tax credit that qualifying individuals and families receive
on the marketplace. It's the second lowest rate for a silver plan in the rate area.

For example, if a rate area had silver plans with rates of `[197.3, 197.3, 201.1, 305.4, 306.7, 411.24]`, the SLCSP for that rate area would be `201.1`,
since it's the second lowest rate in that rate area.

A plan has a "metal level", which can be either Bronze, Silver, Gold, Platinum,
or Catastrophic. The metal level is indicative of the level of coverage the plan
provides.

A plan has a "rate", which is the amount that a consumer pays as a monthly
premium, in dollars.

A plan has a "rate area", which is a geographic region in a state that
determines the plan's rate. A rate area is a tuple of a state and a number, for
example, NY 1, IL 14.

There are two additional CSV files in this directory besides `slcsp.csv`:

- `plans.csv` — all the health plans in the U.S. on the marketplace
- `zips.csv` — a mapping of ZIP code to county/counties & rate area(s)

A ZIP code can potentially be in more than one county. If the county can not be
determined definitively by the ZIP code, it may still be possible to determine
the rate area for that ZIP code. A ZIP code can also be in more than one rate area. In that case, the answer is ambiguous
and should be left blank.

We'll want to compile your code from source and run it from a Unix-like command line, so please include the complete instructions for doing so in a COMMENTS file.
