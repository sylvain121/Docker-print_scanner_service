FROM 	ubuntu:xenial
MAINTAINER 	sylvain121

ENV 	DEBIAN_FRONTEND=noninteractive
RUN	apt-get update
RUN	apt-get dist-upgrade
RUN	apt-get install avahi-daemon cups cups-pdf python-cups python3-sane python3-flask


