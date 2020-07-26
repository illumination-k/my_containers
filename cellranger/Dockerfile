FROM illumination27/cellranger-base

ADD ./cellranger /cellranger

RUN make

# from /cellranger/sourceme.bash and /cellranger/ranger-3.0.2/sourceme.bash
# PATH
ENV PATH=/cellranger/ranger-3.0.2/miniconda-cr-cs/4.3.21-miniconda-cr-cs-c10/bin:/cellranger/ranger-3.0.2/lz4/v1.8.1.2:/cellranger/ranger-3.0.2/STAR/5dda596:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/lib/bin:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/lib/bin:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/bin:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/bin:/cellranger/ranger-3.0.2/martian-cs/v3.2.0/bin:/cellranger/bin:/cellranger/lib/bin:/cellranger/bin:/cellranger/lib/bin:/cellranger/tenkit/bin/:/cellranger/martian-v3.2.5-linux-x86_64/bin/:$PATH

# MROPATH
ENV MROPATH=/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/mro:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/mro:/cellranger/mro:/cellranger/mro:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/mro:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/mro:$MROPATH

# PYTHON PATH
ENV PYTHONPATH=/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/lib/python:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/lib/python:/cellranger/ranger-3.0.2/martian-cs/v3.2.0/adapters/python:/cellranger/lib/python:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/lib/python:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/tenkit/lib/python:/cellranger/ranger-3.0.2/martian-cs/v3.2.0/adapters/python:/cellranger/ranger-3.0.2/ranger-cs/3.0.2/lib/python:/cellranger/lib/python:$PYTHONPATH
ENV PYTHONUSERBASE=/cellranger/ranger-3.0.2/ranger-cs/3.0.2/lib                                                    
ENV LD_LIBRARY_PATH=/cellranger/ranger-3.0.2/ranger-cs/3.0.2/../../miniconda-cr-cs/4.3.21-miniconda-cr-cs-c10/lib:$LD_LIBRARY_PATH 

# others
ENV MROFLAGS=--vdrmode=rolling
ENV LC_ALL=C
