FROM illumination27/analysis-env:latest

USER root 

RUN jupyter labextension install @lckr/jupyterlab_variableinspector && \
    jupyter labextension install @jupyterlab/git && \
    jupyter labextension install @jupyterlab/toc 



RUN pip install jupyterlab-git
RUN jupyter serverextension enable --py jupyterlab_git

# black background
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
RUN echo '{"theme":"JupyterLab Dark"}' > \
  /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

EXPOSE 8888