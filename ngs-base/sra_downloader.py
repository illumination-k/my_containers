import os
import io
import requests
import argparse
import pandas as pd
import subprocess

def timer(func):
    """
    実効時間を表示するデコレータ
    """
    import functools
    import datetime
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.today()
        print('-------------------------------------------------------------')
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        print()
        print('running:', end - start)
        print()
        return result
    return wrapper

@timer
def fasterq_gzip(fasterq, gzip):
    subprocess.run(fasterq)
    subprocess.run(gzip)

def add_dl_info(idx, df, args):
    if args.use_dl_info:
        df.loc[idx]["dl_info"] = ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, default=None, required=True)
    parser.add_argument("--output", "-o", type=str, default="/local_volume")
    parser.add_argument("--thread", "-t", type=str, default="6")
    parser.add_argument("--initialize", action="store_true")
    parser.add_argument("--use_dl_info", action="store_true")
    parser.add_argument("--use_url", type=str, default=None)
    args = parser.parse_args()

    if args.use_url is None:
        df = pd.read_csv(args.input, index_col = 0)
    else:
        URL = args.input
        if "open" in URL:
            URL = URL.replace("open", "uc")
        r = requests.get(URL)
        df = pd.read_csv(io.BytesIO(r.content))

    if args.initialize:
        df["dl_info"] = [[]*len(df.index)]

    for idx in df.index:
        print("===", idx, "downloading...", "===")
        if df.loc[idx]["LibraryLayout"] == "SINGLE":
            fastq = os.path.join(args.output, idx+".fastq")
            fasterq = ["fasterq-dump", idx, "-p", "-e", args.thread, "-O", args.output]
            gzip = ["gzip", fastq]
            fasterq_gzip(fasterq, gzip)
        elif df.loc[idx]["LibraryLayout"] == "PAIRED":
            fastq_1 = os.path.join(args.output, idx+"_1.fastq")
            fastq_2 = os.path.join(args.output, idx+"_2.fastq")
            fasterq = ["fasterq-dump", idx, "-p", "-S", "-e", args.thread, "-O", args.output]
            gzip = ["gzip", fastq_1, fastq_2]
            fasterq_gzip(fasterq, gzip)
        else:
            raise ValueError("Invalid LibraryLayout")

if __name__ == "__main__":
    main()