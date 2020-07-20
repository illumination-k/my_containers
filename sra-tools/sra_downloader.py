import argparse
import subprocess

from Bio import Entrez
from xml.etree import ElementTree


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sra_id", type=str, required=True)
    parser.add_argument("-n", "--n_threads", type=str, default="1")
    parser.add_argument("--email", type=str, default="illumination.k.27@gmail.com")
    parser.add_argument("--layout", type=str, default=None, choices=["SINGLE", "PAIRED"])
    args = parser.parse_args()

    Entrez.email = args.email
    Entrez.tool = "sra_downloader"

    id_handle = Entrez.efetch(db='sra', id=args.sra_id, rettype='xml', retmode='xml')
    id_record = id_handle.read()
    elem = ElementTree.fromstring(id_record)

    if args.layout is None:
        flag = ""
        for e in elem.iter():
            if e.tag == "SINGLE":
                flag = "SINGLE"
            elif e.tag == "PAIRED":
                flag = "PAIRED"
            else:
                continue

        if flag == "":
            raise ValueError("Fetching library layout is failed! Please confirm sra id manually from https://www.ncbi.nlm.nih.gov/sra/ and use layout tags")

        layout = flag
    else:
        layout = args.layout

    



if __name__ == "__main__":
    main()
