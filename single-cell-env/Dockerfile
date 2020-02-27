FROM jupyter/r-notebook

LABEL illumination-k <illumination.k.27@gmail.com>

USER root

RUN apt-get update --fix-missing && \
    apt-get install -y \ 
        less fish git curl wget locales && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

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
        pandas \
        perl-xml-libxml \
        perl-uri \
        picard \ 
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
        networkx \
        tqdm \
        scanpy \
        leidenalg \
        ipywidgets \
        pypairs && \
    conda clean --all --yes

RUN pip install -U pip && \
    pip install cython h5py click cmake && \
    pip install skggm \
                optuna \
                velocyto \
                MulticoreTSNE \
                phate \
                fa2 \
                magic-impute \
                bbknn \
                scvelo \
                pyscenic && \
    pip install git+https://github.com/chriscainx/mnnpy.git

RUN mkdir -p /workspace /local_volume 
WORKDIR /workspace
ADD ./sra_downloader.py /workspace

#  言語設定
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

ADD ./ /workspace

CMD ["fish"]