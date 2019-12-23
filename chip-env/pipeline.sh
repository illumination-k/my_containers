#!/bin/bash

ref=$1
t=$2

for file in `ls *_1.fastq.gz`; do 
    basename=${file%_1.fastq.gz}
    name1=${basename}_1
    name2=${basename}_2
    fastp -i ${name1}.fastq.gz -I ${name2}.fastq.gz \
        -o ${name1}_trim.fastq.gz -O ${name2}_trim.fastq.gz \
        -w $t -h ${basename}.html -j ${basename}.json
    bowtie2 -x $ref \ 
        -1 ${name1}_trim.fastq.gz -2 ${name2}_trim.fastq.gz \
        -O ${basename}.sam
    samtools view -@ $t -q 10 -bS ${basename}.sam > ${basename}.bam
    samtools fixmate -@ $t ${basename}.bam fixmate.bam
    samtools sort -@ $t -o sorted.bam fixmate.bam 
    samtools markdup -s -@ $t sorted.bam ${basename}_sorted_dedup.bam
    samtools index ${basename}_sorted_dedup.bam
    rm ${basename}.sam fixmate.bam sorted.bam
done

multiqc .