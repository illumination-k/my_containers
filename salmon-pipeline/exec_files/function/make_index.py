import os
import shutil
import subprocess
from function import Command

def make_salmon_index(args):
    print("salmon ref index is not detected, now creating...")
    os.makedirs("/local_volume/tmp_fa/", exist_ok=True)
    subprocess.run(["wget", "--quite", "--quota=0", "-O", "/local_volume/tmp_fa/salmon_ref.fa.gz", args.salmon_ref_dl])
    subprocess.run(["gunzip", "/local_volume/tmp_fa/salmon_ref.fa.gz"])
    salmon_index_cmd = Command("salmon index")
    salmon_index_cmd_params = {"-t":"/local_volume/tmp_fa/salmon_ref.fa", "-i":"/local_volume/salmon_ref_index"}
    salmon_index_cmd.parse_params_dict(salmon_index_cmd_params)
    salmon_index_cmd.run()
    shutil.rmtree("/local_volume/tmp_fa")
         
def make_hisat2_index(args):
    print("hisat2 ref index is not detected, now creating...")
    os.makedirs("/local_volume/tmp_fa/", exist_ok=True)
    subprocess.run(["wget", "--quite", "--quota=0", "-O", "/local_volume/tmp_fa/hisat2_ref.fa.gz", args.hisat2_ref_dl])
    subprocess.run(["gunzip", "/local_volume/tmp_fa/hisat2_ref.fa.gz"])
    subprocess.run(["hisat2", "/local_volume/tmp_fa/hisat2_ref.fa", "/local_volume/genome_index"])
    shutil.rmtree("/local_volume/tmp_fa")