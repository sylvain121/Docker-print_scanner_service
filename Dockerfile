FROM 	ubuntu:xenial
MAINTAINER 	sylvain121

ENV 	DEBIAN_FRONTEND=noninteractive
RUN	apt-get update -y
RUN	apt-get dist-upgrade -y
RUN	apt-get install avahi-daemon cups cups-pdf cups-client python-cups python3-sane python3-flask -y


ADD 	etc-cups /etc/cups
RUN 	mkdir -p /etc/cups/ssl
VOLUME 	/etc/cups/
VOLUME 	/var/log/cups
VOLUME 	/var/spool/cups
VOLUME 	/var/cache/cups

ADD 	etc-pam.d-cups /etc/pam.d/cups

EXPOSE 	631

ADD 	start.sh /root/start.sh
RUN 	chmod +x /root/start.sh
CMD 	["/root/start.sh"]

