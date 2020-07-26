FROM debian

RUN apt-get update && \
    apt-get install -y wget git curl build-essential pkg-config make clang-6.0 golang-1.11-go libz-dev libbz2-dev liblzma-dev cython python-pip && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    mkdir -p /cellranger

ENV PATH=/usr/lib/go-1.11/bin:$PATH
ENV PATH=/root/.cargo/bin:$PATH

RUN rustup install 1.28.0 && \
    rustup default 1.28.0 

RUN pip install numpy docopt && \
    ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy /usr/include/numpy

WORKDIR /cellranger

RUN curl -o ranger-3.0.2.tar.gz "http://cf.10xgenomics.com/releases/developers/ranger-3.0.2.tar.gz?Expires=1590315393&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9kZXZlbG9wZXJzL3Jhbmdlci0zLjAuMi50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1OTAzMTUzOTN9fX1dfQ__&Signature=SVmge3JPzIIYfhszzUjw7Dv9ilbAWVcNTyFSrjtfUZhjyW0p11zAhqPD1PzK04pm5wJDwhzG5GNfsY8hSPbrGliGBsrBTj8MhguBQu7O2DYMOk5ej-5VKFtskZ3CbM5YU~aS1rbTsru6u6y33M2g9ceokI1teZnf0JdA690AuC8VM1fNLIbq8iRRoNOdz7DsG6-B6j5Iao2q4lRt2NnRc976iTO-lvB728jyKqFYQQBiMTEQkMKi21hI8PW~aRSXtvLCab3EchTeXC7OnuMKnYwyXAh-NFEH3qI12bG7sGSc9oJBxLQCJ9ZFXh9iTbSR~YeZCsrUn6oM8EnTFXvFOQ__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" && \
    tar zxvf ranger-3.0.2.tar.gz && \
    wget "https://github.com/martian-lang/martian/releases/download/v3.2.5/martian-v3.2.5-linux-x86_64.tar.gz" && \
    tar zxvf martian-v3.2.5-linux-x86_64.tar.gz && \
    rm -f *.tar.gz