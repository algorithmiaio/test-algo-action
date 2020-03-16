from ubuntu:16.04

RUN pip install algorithmia==1.2.0

COPY entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]