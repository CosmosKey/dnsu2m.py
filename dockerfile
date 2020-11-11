FROM alpine:latest
ENV PYTHONUNBUFFERED=1

COPY dnsu2m.py /app/dnsu2m.py

RUN apk update \
    && apk add python3 \
    && python3 -m ensurepip \
    && ln -sf python3 /usr/bin/python \
    && pip3 install --no-cache --upgrade pip setuptools \
    && pip3 install dnslib \
    && rm -rf /var/cache/apk/* \
    && chmod 755 /app/dnsu2m.py \
    && echo 'Done'

EXPOSE 5353/udp
EXPOSE 53/udp

ENTRYPOINT ["python","/app/dnsu2m.py"]


