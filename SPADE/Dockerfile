FROM conda/miniconda3

LABEL illumination-k <illumination.k.27@gmail.com>

USER root

RUN apt-get update --fix-missing && \
    apt-get install -y \ 
        less fish git curl wget locales && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda install -c bioconda -c conda-forge \
        blast \
        mafft \
        matplotlib==2.2.3 \
        seaborn==0.8.1 \
        weblogo==3.6.0 \
        biopython

RUN mkdir -p /workspace /local_volume
WORKDIR /workspace
RUN git clone https://github.com/yachielab/SPADE