FROM conda/miniconda3

LABEL illumination-k <illumination.k.27@gmail.com>

RUN apt-get update --fix-missing && \
    apt-get install -y less fish git curl wget && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda update -n base conda && \
    conda install -c bioconda -c conda-forge \
        fastqc \
        fastp \
        multiqc \
        picard && \
    conda clean --all --yes

RUN mkdir -p /workspace /local_volume

CMD ["fish"]