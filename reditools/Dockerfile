FROM conda/miniconda2

RUN apt-get update --fix-missing && \
    apt-get install -y git && \
    apt-get clean


RUN conda install -c bioconda -c conda-forge \
        pysam \
        fisher


RUN mkdir -p /workspace

WORKDIR /workspace

RUN git clone https://github.com/BioinfoUNIBA/REDItools

WORKDIR /workspace/REDItools

RUN cp README.md README

RUN python setup.py install


