FROM conda/miniconda3

RUN apt-get update --fix-missing && \
    apt-get clean

# v1.10 2020/3/4
RUN conda update --all && \
    conda install -c bioconda -c conda-forge \
        bioconductor-tximport \
        r-reader \
        r-jsonlite
        
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume /workspace
ADD ./quant2csv.R /workspace
WORKDIR /local_volume