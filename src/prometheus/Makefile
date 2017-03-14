# @SI_Copyright@
# @SI_Copyright@

PKGROOT         = /opt/prometheus
TGZ 		= tar.gz
ROLLROOT	= ../..
URL		= https://github.com/prometheus/$(NAME)/releases/download/
RURL		= https://github.com/prometheus/$(NAME)/releases/latest
SHAREDOCDIR	= /usr/share/doc/$(NAME)/
TGZNAME		= $(NAME)-$(VERSION).linux-amd64.$(TGZ)
TARDIR		= $(NAME)-$(VERSION).linux-amd64
RPM.ARCH	= x86_64

include $(STACKBUILD)/etc/CCRules.mk

VERS=$(shell curl -s -k $(RURL) | sed "s/.*\(v.*\)\".*/\1/g" | cut -c 2-)

refresh::
	rm -f $(NAME)*-linux-amd64.$(TGZ)
	(						\
		echo "NAME=prometheus" > version.mk;		\
		echo "VERSION=$(VERS)" >> version.mk;	\
	)
	
	wget --no-check-certificate -O $(TGZNAME) $(URL)v$(VERS)/$(TGZNAME)

build::
	tar -xf $(TGZNAME)

install::
	mkdir -p $(ROOT)$(PKGROOT)/bin
	mkdir -p $(ROOT)$(PKGROOT)/etc
	mkdir -p $(ROOT)/usr/lib/systemd/system

	$(INSTALL) -m644 ./systemd/prometheus.service $(ROOT)/usr/lib/systemd/system/
	$(INSTALL) -m0644 $(TARDIR)/prometheus.yml $(ROOT)$(PKGROOT)/etc/prometheus.yml
	$(INSTALL) -m0755 $(TARDIR)/prometheus $(ROOT)$(PKGROOT)/bin/prometheus
	$(INSTALL) -m0755 $(TARDIR)/promtool $(ROOT)$(PKGROOT)/bin/promtool
	cp -a $(TARDIR)/consoles $(ROOT)$(PKGROOT)
	cp -a $(TARDIR)/console_libraries $(ROOT)$(PKGROOT)

clean::
