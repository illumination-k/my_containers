import os
import sys 
import shutil
import subprocess
from command import Command


def main():
    t = sys.argv[1]
    if t == "salmon":
        os.makedirs("/local_volume/tmp_fa/", exist_ok=True)
        subprocess.run(["wget", "--quota=inf", "-O", "/local_volume/tmp_fa/salmon_ref.fa.gz", "http://marchantia.info/download/download/Mpolymorphav3.1.allTrs.gene.fa.gz"])
        subprocess.run(["gunzip", "/local_volume/tmp_fa/salmon_ref.fa.gz"])
        salmon_index_cmd = Command("salmon index")
        salmon_index_cmd_params = {"-t":"/local_volume/tmp_fa/salmon_ref.fa", "-i":"/local_volume/salmon_ref_index"}
        salmon_index_cmd.parse_params_dict(salmon_index_cmd_params)
        salmon_index_cmd.run()
        shutil.rmtree("/local_volume/tmp_fa")
    elif t == "hisat2":
        print("hisat2 ref index is not detected, now creating...")
        os.makedirs("/local_volume/tmp_fa/", exist_ok=True)
        os.makedirs("/local_volume/hisat2_ref_index", exist_ok=True)
        subprocess.run(["wget", "--quota=inf", "-O", "/local_volume/tmp_fa/hisat2_ref.fasta.gz", "http://marchantia.info/download/download/JGI_3.1.fasta.gz"])
        subprocess.run(["gunzip", "/local_volume/tmp_fa/hisat2_ref.fasta.gz"])
        subprocess.run(["hisat2-build", "/local_volume/tmp_fa/hisat2_ref.fasta", "/local_volume/hisat2_ref_index/genome_index"])
        shutil.rmtree("/local_volume/tmp_fa")
    else:
        raise ValueError("Invalid input")

if __name__ == "__main__":
    main()