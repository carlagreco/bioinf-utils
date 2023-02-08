#!/usr/bin/env python

"""
This script converts genbank to embl
"""

import pandas as pd
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(description="This script converts genbank to embl")

required = parser.add_argument_group('required arguments')

required.add_argument("-i", "--input-file", help="Input genbank file(s)", action="store", dest="input_file", required=True, nargs="*")

args = parser.parse_args()

files = args.input_file

for file in files:
    records = SeqIO.parse(file, "genbank")
    filename = file.split('.')[0]
    count = SeqIO.write(records, filename + ".embl", "embl")
    print("Converted %i records" % count)