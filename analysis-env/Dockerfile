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
        anndata \
        scikit-learn \
        biopython \
        plotly \
        umap-learn \
        upsetplot \
        statsmodels \
        matplotlib \
        seaborn \
        networkx \
        tqdm \
        bioconductor-annotationforge \
        bioconductor-sva \
        bioconductor-edger \
        bioconductor-deseq2 \
        bioconductor-rgraphviz \
        bioconductor-genefilter \
        bioconductor-annotationdbi \
        bioconductor-clusterprofiler \
        bioconductor-do.db \
        r-tidyverse \
        r-devtools \
        deeptools \
        pysam \
        pybedtools \
        homer \
    -c bioconda -c r -c conda-forge -c anaconda

# RUN Rscript -e "install.packages(c('qgraph', 'bootnet', 'ASmap', 'onemap'), repos='http://cran.us.r-project.org')" 

RUN pip install -U pip && \
    pip install pyper \ 
                bctpy \
                rpy2 

