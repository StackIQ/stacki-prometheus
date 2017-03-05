# @SI_Copyright@
# @SI_Copyright@

PKGROOT         = /opt/prometheus
TGZ 		= tar.gz
ROLLROOT	= ../..
URL		= https://github.com/prometheus/$(NAME)/releases/download/
RURL		= https://github.com/prometheus/$(NAME)/releases/latest
TGZNAME		= $(NAME)-$(VERSION).linux-amd64.$(TGZ)
TARDIR		= $(NAME)-$(VERSION).linux-amd64

include $(STACKBUILD)/etc/CCRules.mk

VERS=$(shell curl -s -k $(RURL) | sed "s/.*\(v.*\)\".*/\1/g" | cut -c 2-)

refresh::
	rm -f $(NAME)*-linux-amd64.$(TGZ)
	(						\
		echo "NAME=$(NAME)" > version.mk;		\
		echo "VERSION=$(VERS)" >> version.mk;	\
	)
	
	wget --no-check-certificate -O $(TGZNAME) $(URL)v$(VERS)/$(TGZNAME)

build::
	tar -xf $(TGZNAME)

install::
	mkdir -p $(ROOT)$(PKGROOT)/bin
	mkdir -p $(ROOT)/usr/lib/systemd/system

	$(INSTALL) -m755 $(TARDIR)/node_exporter $(ROOT)$(PKGROOT)/bin
	$(INSTALL) -m644 ./systemd/node_exporter.service $(ROOT)/usr/lib/systemd/system/

clean::
