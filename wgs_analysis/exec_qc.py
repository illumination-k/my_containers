import os
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, default=".")
    parser.add_argument("--output", "-o", type=str, default=".")
    parser.add_argument("--fastq_type", type=str, default=".fastq.gz", choices=[".fastq", ".fq", ".fastq.gz", ".fq.gz"], help='Input fastq type. You can select from [.fastq, .fq, .fastq.gz, .fq.gz], defalut is ".fastq.gz"')
    parser.add_argument("--thread", "-t", type=str, default="2")
    args = parser.parse_args()

    report_path = os.path.join(args.output, "report")
    os.makedirs(report_path, exist_ok=True)
    files = [file for file in os.listdir(args.input) if file.endswith(args.fastq_type)]
    
    for file in files:
        basename = file.split(".")[0]
        trim_file = basename + "_trim.fastq.gz"
        fastqc_cmd = ["fastqc", "-o", report_path, "-t", args.thread, "-k", "7", file]
        print(fastqc_cmd)
        subprocess.run(" ".join(fastqc_cmd), shell=True)

        fastp_cmd = ["fastp", "-i", file, "-o", trim_file, "-w", args.thread, "-h", os.path.join(report_path, basename+"_fastp.html"), "-j", os.path.join(report_path, basename+"_fastp.json")]
        print(fastp_cmd)
        subprocess.run(" ".join(fastp_cmd), shell=True)

    multqc_cmd = ["multiqc", args.output, "-o", args.output]
    subprocess.run(" ".join(multqc_cmd), shell=True)
    print("finish!")


if __name__ == "__main__":
    main()
    

