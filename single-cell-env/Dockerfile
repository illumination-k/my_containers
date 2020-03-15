FROM illumination27/my-notebook:latest

LABEL illumination-k <illumination.k.27@gmail.com>

RUN conda update -n base conda && \
    conda install -c bioconda -c conda-forge \
        lxml \
        bioservices \
        pandas \
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
    pip install optuna \
                MulticoreTSNE \
                phate \
                fa2 \
                magic-impute \
                bbknn && \
    pip install git+https://github.com/chriscainx/mnnpy.git

RUN mkdir -p /workspace /local_volume 
WORKDIR /workspace


CMD ["fish"]