#!/bin/bash

ref=$1
t=5

for file in `ls *.fastq.gz`; do 
    echo $file
    basename=${file%.fastq.gz}
    fastp -i $file -o ${basename}_trim.fastq.gz -w $t
    bowtie2 -x $ref/tak1_ver5_hek239 -U ${basename}.sam
    samtools view -@ $t -q 10 -bS ${basename}.sam > ${basename}.bam
    samtools fixmate -@ $t ${basename}.bam fixmate.bam
    samtools sort -@ $t -o sorted.bam fixmate.bam 
    samtools markdup -s -@ $t sorted.bam ${basename}_sorted_dedup.bam
    samtools index ${basename}_sorted_dedup.bam
    rm ${basename}.bam fixmate.bam sorted.bam
done