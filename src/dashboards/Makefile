# @SI_Copyright@
# @SI_Copyright@

PKGROOT         = /opt/prometheus/share
ROLLROOT	= ../..

include $(STACKBUILD)/etc/CCRules.mk

build::

install::
	mkdir -p $(ROOT)$(PKGROOT)
	$(INSTALL) -m644 ./files/* $(ROOT)$(PKGROOT)

clean::
