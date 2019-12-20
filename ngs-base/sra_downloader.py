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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, default=None, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input, index_col = 0)

    for idx in df.index:
        print("===", idx, "downloading...", "===")
        if df.loc[idx]["LibraryLayout"] == "SINGLE":
            fasterq = ["fasterq-dump", idx, "-p"]
            gzip = ["gzip", idx+".fastq"]
            fasterq_gzip(fasterq, gzip)
        elif df.loc[idx]["LibraryLayout"] == "PAIRED":
            fasterq = ["fasterq-dump", idx, "-p", "-S"]
            gzip = ["gzip", idx+"_1.fastq", idx+"_2.fastq"]
            fasterq_gzip(fasterq, gzip)
        else:
            raise ValueError("Invalid LibraryLayout")

if __name__ == "__main__":
    main()