FROM alpine
LABEL \
	maintainer="Davide Alberani <da@erlug.linux.it>"

RUN \
	apk add --no-cache \
		python3 \
		py3-cffi \
		py3-six \
		py3-requests \
		py3-tz \
		py3-dateutil \
		py3-decorator \
		py3-cryptography && \
	pip3 install Mastodon.py
COPY cthulhusay.py mastodon-cthulhusay.py /
RUN chmod +x /mastodon-cthulhusay.py

WORKDIR /

ENTRYPOINT ["python3", "/mastodon-cthulhusay.py"]


