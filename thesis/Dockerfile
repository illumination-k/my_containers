FROM jupyter/r-notebook

LABEL illumination-k <illumination.k.27@gmail.com>

USER root

RUN apt-get update --fix-missing && \
    apt-get install -y \ 
        less fish git curl wget locales && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 
    
RUN curl -L https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.0/setup-apt.sh | sh

RUN jupyter labextension install @lckr/jupyterlab_variableinspector \
                                 @jupyterlab/git \
                                 @jupyterlab/toc \
                                 @jupyter-widgets/jupyterlab-manager \
                                 jupyterlab-plotly \
                                 plotlywidget \
                                 --no-build && \
    pip install jupyterlab-git && \
    jupyter serverextension enable --py jupyterlab_git && \
    jupyter lab build

# black background
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
RUN echo '{"theme":"JupyterLab Dark"}' > \
  /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

RUN conda install -c conda-forge -c bioconda \
    numpy \
    pandas \
    scipy \
    networkx \
    scikit-learn \
    scanpy \
    umap-learn \
    plotly \
    bioconductor-edger \
    bioconductor-clusterprofiler \
    bioconductor-tximport \
    r-reader \
    r-jsonlite \
    r-tidyverse \
    r-wgcna \
    homer \
    fastp \
    subread \
    salmon \
    hisat2

RUN pip install -U pip && \
    pip install cython h5py click cmake && \
    pip install pyscenic \
                bctpy