FROM jupyter/r-notebook

LABEL maintainer="illumination-k <illumination.k.27@gamil.com>"

USER root

RUN apt-get update --fix-missing && \
    apt-get install -y tmux less zsh git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN conda update -n base conda && \ 
    conda install \
        numpy \
        pandas \
        scipy \
        scikit-learn \
        biopython \
        plotly \
        psycopg2 

RUN conda install \
    bioconductor-biocinstaller \
    deeptools \
    pysam \
    pybedtools \
    homer \
    -c bioconda

RUN Rscript -e "install.packages(c('BiocManager', 'tidyverse', 'devtools', 'usethis', 'qgraph', 'bootnet', 'ASmap'), repos='http://cran.us.r-project.org')" 

RUN Rscript -e "BiocManager::install(c('edgeR', 'DEseq2', 'WGCNA', 'goseq', 'topGO', 'ALL', 'hgu95av2.db', 'Rgraphviz', 'genefilter'))"

USER jovyan

RUN pip install -U pip && \
    pip install cython && \
    pip install pyper matplotlib seaborn umap-learn skggm optuna statsmodels upsetplot networkx

