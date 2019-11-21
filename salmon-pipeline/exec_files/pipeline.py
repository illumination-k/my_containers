import os
import sys 

import argparse
import shutil 
from function import print_end_logo, print_start_logo, exec_pipeline, make_salmon_index, make_hisat2_index

def main():
    parser = argparse.ArgumentParser(description='Execute pipeline for RNA-seq(fastQC -> fastp -> salmon -> tximport) or (fastQC -> fastp -> hisat2 -> samtools -> salmon -> tximport) and export general report by multiQC')
    parser.add_argument("--input", "-i", type=str, default=None, required=True, help='Path of input directory which contains fastq files')
    parser.add_argument("--output", "-o", type=str, default=".", help='Output directory. Defalut is current directory.')
    parser.add_argument("--salmon_ref", "-r", type=str, default=None, help='Path of salmon index directory. Default is "/local_volume/salmon_ref_index"')
    parser.add_argument("--salmon_ref_dl", type=str, defalut="http://marchantia.info/download/download/Mpolymorphav3.1.allTrs.gene.fa.gz")
    parser.add_argument("--hisat2_ref", type=str, default=None, help="Path of hisat2 index directory. Default is /local_volume/hisat2_ref_index")
    parser.add_argument("--hisat2_ref_dl", type=str, default="http://marchantia.info/download/download/JGI_3.1.fasta.gz")
    parser.add_argument("--use_hisat2", action='store_true', help="If you would like to use hisat2, please use this option")
    parser.add_argument("--thread", "-t", type=str, default="2", help='Number of core you want to use, default is 2')
    parser.add_argument("--fastq_type", type=str, default=".fastq.gz", choices=[".fastq", ".fq", ".fastq.gz", ".fq.gz"], help='Input fastq type. You can select from [.fastq, .fq, .fastq.gz, .fq.gz], defalut is ".fastq.gz"')
    parser.add_argument("--method", type=str, default="scaledTPM", choices=["scaledTPM", "lengthScaledTPM"], help="Normalized method of tximport. You can select from scaledTPM and lengthScaledTPM")
    parser.add_argument("--fastp", type=str, nargs="*", default=None, help='overwrite fastp parameter, now testing')
    parser.add_argument("--salmon", type=str, nargs="*", default=None, help='overwrite salmon parameter, now testing')
    parser.add_argument("--hisat2", type=str, nargs="*", default=None, help='overwrite hisat2 parameter, now testing')
    parser.add_argument("--keep_ref", action='store_true', help="If you would like to keep index files in local, please use this args")
    args = parser.parse_args()
    
    print_start_logo()

    # make directtory
    out_dir = args.output
    os.makedirs(os.path.join(out_dir, "reports"), exist_ok=True)

    # make index files

    if args.salmon_ref is None:
        make_salmon_index(args)
    if args.use_hisat2 and args.hisat2_ref is None:
        make_hisat2_index(args)

    # exec pipeline
    exec_pipeline(args)

    # delete index files
    if not args.keep_ref:
        if args.salmon_ref is None:
            shutil.rmtree("/local_volume/salmon_ref_index")
        if args.use_hisat2 and args.hisat2_ref is None:
            shutil.rmtree("/local_volume/hisat2_ref_index")

    print_end_logo()

if __name__ == "__main__":
    main()

