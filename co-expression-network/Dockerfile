FROM jupyter/r-notebook

LABEL maintainer="illumination-k <illumination.k.27@gamil.com>"

USER root

RUN apt-get update --fix-missing && \
    apt-get install -y tmux less zsh git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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

RUN conda update -n base conda && \ 
    conda install -c bioconda -c conda-forge \
        biopython \
        pandas \
        numpy \
        matplotlib \
        seaborn \
        scipy \
        scikit-learn \
        plotly \
        networkx \
        bioconductor-edgeR \
        bioconductor-deseq2 \
        bioconductor-clusterprofiler \
        bioconductor-do.db \
        bioconductor-go.db \
        bioconductor-kegg.db \
        bioconductor-annotationdbi \
        bioconductor-sva \
        r-wgcna \
        r-tidyverse \
        homer \
        pybedtools 

RUN pip install pyscenic bctpy

EXPOSE 8888