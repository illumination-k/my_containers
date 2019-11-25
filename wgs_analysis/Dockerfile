FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get install -y unzip tmux && \
    apt-get -qq -y autoremove && \
    apt-get autoclean 

RUN conda update -n base conda

RUN conda install \
        samtools \
        bwa \
        Mummer \
        kwip \
        bedtools \
        vcftools \
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

RUN wget -O /workspace/bin/gatk4.zip https://github.com/broadinstitute/gatk/releases/download/4.1.4.0/gatk-4.1.4.0.zip && \
    unzip /workspace/bin/gatk4.zip -d /workspace/bin && \
    rm -f /workspace/bin/gatk4.zip

# PATH TO files for nasp
ENV PATH="${PATH}:/workspace/bin"
ENV PATH="${PATH}:/workspace/bin/gatk-4.1.4.0"

ADD ./exec_qc.py /workspace/bin

WORKDIR /local_volume



