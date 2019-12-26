FROM conda/miniconda3

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

RUN apt-get update --fix-missing && \
    apt-get install -y locales && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

#  言語設定
RUN echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8
ENV LC_CTYPE=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8

RUN conda install -c conda-forge \
    numpy \
    scipy \
    pandas \
    plotly \
    dash \
    dash-bio \
    networkx \
    django \
    psycopg2 \
    r-base

RUN Rscript -e "install.packages(c('BiocManager', 'tidyverse'), repos='http://cran.us.r-project.org')" 
RUN Rscript -e "BiocManager::install(c('edgeR', 'DEseq2', 'WGCNA', 'goseq', 'topGO', 'ALL', 'Rgraphviz', 'genefilter'))"

RUN pip install django-plotly-dash django-pandas django-crispy-forms pyper