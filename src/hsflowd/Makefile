# @SI_Copyright@
# @SI_Copyright@

ROLLROOT       = ../../
RPM.STRATEGY	= copy

include $(STACKBUILD)/etc/CCRules.mk

build:
	mkdir -p $(REDHAT.RPMS)/x86_64/

rpm::
	cp -p ./RPMS/$(NAME)-*x86_64.rpm $(REDHAT.RPMS)/$(ARCH)

clean::
