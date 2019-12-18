FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get install -y unzip tmux build-essential autoconf autogen make zlib1g-dev && \
    apt-get -qq -y autoremove && \
    apt-get autoclean 

RUN conda update -n base conda

RUN conda install \
        samtools \
        bwa \
        Mummer \
        kwip \
        bedtools \
        VarScan \
        bcftools \
        snpeff \
        -c bioconda -c conda-forge && \
        conda clean --all --yes

RUN mkdir -p /workspace/bin

WORKDIR /workspace/bin

# download and install SolSNP # server error 191127
# RUN wget -O /workspace/bin/SolSNP.zip https://sourceforge.net/projects/solsnp/files/SolSNP-1.11/SolSNP-1.11.zip && \
#     unzip /workspace/bin/SolSNP.zip -d /workspace/bin && \
#     rm -f /workspace/bin/SolSNP.zip

# download and install GATK4
RUN wget -O /workspace/bin/gatk4.zip https://github.com/broadinstitute/gatk/releases/download/4.1.4.0/gatk-4.1.4.0.zip && \
    unzip /workspace/bin/gatk4.zip -d /workspace/bin && \
    rm -f /workspace/bin/gatk4.zip

# download and install vcftools
RUN git clone https://github.com/vcftools/vcftools.git
WORKDIR /workspace/bin/vcftools 

RUN ./autogen.sh && \
    ./configure make && \
    make install

# PATH TO files for tools
ENV PATH="${PATH}:/workspace/bin"
ENV PATH="${PATH}:/workspace/bin/gatk-4.1.4.0"

ADD ./exec_qc.py /workspace/bin

WORKDIR /local_volume



