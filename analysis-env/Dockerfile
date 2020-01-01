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
        psycopg2 \
        umap-learn \
        upsetplot \
        statsmodels \
        matplotlib \
        seaborn \
        numba \
        networkx \
        tqdm \
        -c conda-forge -c anaconda -c numba

RUN conda install \
    scanpy \
    leidenalg \
    ipywidgets \
    bioconductor-edger \
    bioconductor-deseq2 \
    bioconductor-goseq \
    bioconductor-topgo \
    bioconductor-rgraphviz \
    bioconductor-genefilter \
    r-vcfr \
    r-wgcna \
    r-tidyverse \
    r-devtools \
    deeptools \
    pysam \
    pybedtools \
    pypairs \
    homer \
    -c bioconda -c r -c conda-forge

RUN Rscript -e "install.packages(c('qgraph', 'bootnet', 'ASmap', 'onemap'), repos='http://cran.us.r-project.org')" 

RUN pip install -U pip && \
    pip install cython h5py click cmake && \
    pip install pyper \ 
                skggm \
                optuna \
                velocyto \
                MulticoreTSNE \
                phate \
                fa2 \
                magic-impute \
                bbknn \
                rpy2 && \
    pip install git+https://github.com/jacoblevine/phenograph.git && \
    pip install git+https://github.com/dpeerlab/Palantir.git


