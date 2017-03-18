# @SI_Copyright@
# @SI_Copyright@

ROLLROOT       = ../../
RPM.STRATEGY	= copy

include $(STACKBUILD)/etc/CCRules.mk

build:
	mkdir -p $(REDHAT.RPMS)/noarch/

rpm::
	cp -p ./RPMS/$(NAME)-*noarch.rpm $(REDHAT.RPMS)/noarch/

clean::
