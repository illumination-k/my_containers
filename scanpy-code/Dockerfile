FROM codercom/code-server

USER root

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 build-essential git zsh make \
    && curl -fsSL https://starship.rs/install.sh -o /tmp/install.sh \
    && bash /tmp/install.sh --yes \
    && rm -rf /tmp/install.sh \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && mkdir -p /workspace \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH

WORKDIR /workspace
ADD . /workspace

RUN conda update -n base conda && \
    conda install -c bioconda -c conda-forge \
    --yes --file conda_requirements.txt && \
    conda clean --all --yes

RUN pip install -U pip && \
    pip install -r requirements.txt && \
    pip install git+https://github.com/chriscainx/mnnpy.git

USER coder

RUN code-server --install-extension donjayamanne.python-extension-pack && \
    code-server --install-extension coenraads.bracket-pair-colorizer-2 && \
    code-server --install-extension donjayamanne.githistory && \
    code-server --install-extension ibm.output-colorizer && \
    code-server --install-extension foxundermoon.shell-format && \
    code-server --install-extension remisa.shellman

RUN curl -L https://raw.githubusercontent.com/illumination-k/dotfiles/master/etc/install.sh | bash