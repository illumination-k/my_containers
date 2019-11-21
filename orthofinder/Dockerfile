FROM conda/miniconda2


RUN conda install orthofinder -c bioconda

RUN mkdir -p /workspace
WORKDIR /workspace

ADD ./add_files /workspace