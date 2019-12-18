FROM conda/miniconda3

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

RUN mkdir -p /workspace
WORKDIR /workspace
ADD ./requirements.txt /workspace
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN conda install r-base

RUN Rscript -e "install.packages(c('tidyverse', 'BiocManager'), repos='http://cran.us.r-project.org')" 
RUN Rscript -e "BiocManager::install(c('edgeR', 'DEseq2', 'WGCNA', 'goseq'))"

