#!/usr/bin/env python

from Bio import SeqIO
import argparse

"""
This script parses the output of antismash from the antismash gbk file
"""

parser = argparse.ArgumentParser(description="This script parses the output of antismash from the antismash gbk file")
required = parser.add_argument_group('required arguments')
required.add_argument("-i", "--input-file", help="Input genbank file(s)", action="store", dest="input_file", required=True, nargs="*")
args = parser.parse_args()
files = args.input_file

for file in files:
    filename = file.split('_')[0]
    tsv_out = str(filename + "_antismash_clusters.tsv")
    with open(tsv_out, "wt") as f:
        f.write("contig\tcluster_number\tcluster_type\tcategory\n")
        for seq_record in SeqIO.parse(file, "genbank"):
            contig = seq_record.name
            for seq_feat in seq_record.features:
                if seq_feat.type == "protocluster":
                    number = seq_feat.qualifiers["protocluster_number"][0]
                    cluster = seq_feat.qualifiers["product"][0]
                    category = seq_feat.qualifiers["category"][0]
                    f.write(contig + "\t" + number + "\t" + cluster + "\t" + category + "\n")