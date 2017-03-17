# @SI_Copyright@
# @SI_Copyright@

ROLLROOT       = ../../
RPM.STRATEGY	= copy

include $(STACKBUILD)/etc/CCRules.mk

build:
	mkdir -p $(REDHAT.RPMS)/x86_64/
	mkdir -p $(REDHAT.RPMS)/noarch/

rpm::
	cp -p ./RPMS/*noarch.rpm $(REDHAT.RPMS)/noarch/
	cp -p ./RPMS/*x86_64.rpm $(REDHAT.RPMS)/$(ARCH)

clean::
