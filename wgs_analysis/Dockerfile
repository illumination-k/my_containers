FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get install -y unzip tmux && \
    apt-get -qq -y autoremove && \
    apt-get autoclean 

RUN conda update -n base conda

RUN conda install \
        samtools=1.2* \
        bwa \
        bowtie2 \
        Mummer \
        bedtools \
        VarScan \
        bcftools \
        snpeff \
        -c bioconda -c conda-forge && \
        conda clean --all --yes

RUN mkdir -p /workspace/bin

WORKDIR /workspace/bin

# download SolSNP
RUN wget -O /workspace/bin/SolSNP.zip https://sourceforge.net/projects/solsnp/files/SolSNP-1.11/SolSNP-1.11.zip && \
    unzip /workspace/bin/SolSNP.zip -d /workspace/bin && \
    rm -f /workspace/bin/SolSNP.zip

# PATH TO files for nasp
ENV PATH="${PATH}:/workspace/bin"

ADD ./exec_qc.py /workspace/bin

WORKDIR /local_volume



