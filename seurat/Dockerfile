FROM illumination27/my-notebook:latest

LABEL illumination-k <illumination.k.27@gmail.com>


RUN conda install -c bioconda -c conda-forge -c r \
        udunits2 \
        r-seurat \
        r-here \
        r-tidyverse \
        r-ontologyindex \
        r-devtools \
        bioconductor-biocgenerics \
        bioconductor-delayedarray \
        bioconductor-delayedmatrixstats \
        bioconductor-limma \
        bioconductor-s4vectors \
        bioconductor-singlecellexperiment \
        bioconductor-summarizedexperiment \
        bioconductor-batchelor

# remoteを入れないとdevtoolsがエラーになる (remote=>2.2.1以上が必要らしい)
# furrrのためにudunits2が必要らしい
# futureのbinaryが古いらしい
# sfが必要らしい
# sfのためにgdal >= 2.0.1が必要らしい -> anoconda cloudではversion3.0.4なのにエラーする。なぜ。
# RUN Rscript -e "install.packages(c('useful', 'remotes', 'future', 'sf'), repos='https://cran.ism.ac.jp/')" && \
#     Rscript -e "devtools::install_github('cole-trapnell-lab/leidenbase')" && \
#     Rscript -e "devtools::install_github('cole-trapnell-lab/monocle3')"