FROM conda/miniconda3


RUN apt update --fix-missing


# conda forge need for dependencies
RUN conda install -c bioconda -c conda-forge \
        repeatmodeler \
        repeatmasker