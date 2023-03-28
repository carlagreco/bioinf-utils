# Useful one-liners to deal with sequencing data

### calculate mean read lengths
```
awk 'NR%4==2{sum+=length($0)}END{print sum/(NR/4)}' sequences.fastq
```

### maxbin2 contigs to MAG
```
grep --initial-tab  ">c_" m* | awk '{ t=$1 ; $1=$2; $2=t; print }' | sed 's/[>:]//g' | sed 's/ /\t/g' > maxbin_tmp.txt
sed 's/\./_/g' maxbin_tmp.txt > maxbin_contig_2_bin.txt
```

### get fasta by search in prokka outout (example psaA)
```
pcregrep -Mo '(>[\S]* Photosystem I P700 chlorophyll a apoprotein A1[ 0-9\nA-Z]*)' sequences.faa > psaA_protein.faa
```

### clean up fasta header - removed everything after space in header
```
cut -d ' ' -f1 sequences.faa > sequences_cleanup.faa
```

### give files name of directory (appends directory name to name of file)
```
for f in */*.gbff ;do fp=$(dirname "$f"); fl=$(basename "$f"); mv "$fp/$fl" "$fp/$fp"_"$fl"; done
```

### count reads and gb in fastq.gz file - quite slow
```
zcat sequences.fastq.gz|paste - - - -|cut -f2|wc -c -l|awk -v OFS="\n" '{print "reads: "$1, "bases: "$2-$1}'
```

### same but just fastq
```
cat sequences.fq|paste - - - -|cut -f2|wc -c -l|awk -v OFS="\n" '{print "reads: "$1, "bases: "$2-$1}'
```

### in loop, add filenames to start
```
for i in $(ls */*sequences.fq); do echo -n -e $i "\t"; cat $i|paste - - - -|cut -f2|wc -c -l|awk -v OFS="\t" '{print "reads: "$1, "bases: "$2-$1}'; done
```

### fastq histogram 
```
cat sequences.fq | awk '{if(NR%4==2) print length($1)}' | sort -n | uniq -c > read_length.txt
```

### alternative histogram 
```
awk 'NR%4 == 2 {lengths[length($0)]++} END {for (l in lengths) {print l, lengths[l]}}' sequences.fq > read_length.txt
```
