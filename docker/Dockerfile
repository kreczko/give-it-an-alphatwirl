FROM rootproject/root-ubuntu16

RUN sudo apt update && \
    sudo apt install -y python-pip

RUN pip install --user -U --no-cache-dir numpy pandas root_numpy root_pandas

COPY docker/cdw /usr/local/bin/cdw
