FROM conda/miniconda3

RUN apt-get update --fix-missing && \
    apt-get install -y wget

# v1.10 2020/3/4
RUN conda update --all && \
        conda install -c bioconda homer


RUN mkdir -p /resources && \
    wget -O /resources/mpolymorpha.gtf https://marchantia.info/download/tak1v5.1/MpTak1v5.1_r1.gtf && \
    wget -O /resources/mpolymorpha.fasta https://marchantia.info/download/tak1v5.1/MpTak1v5.1.fasta && \
    loadGenome.pl --name Mpolymorpha -org null -fasta /resources/mpolymorpha.fasta -gtf /resources/mpolymorpha.gtf
        
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume