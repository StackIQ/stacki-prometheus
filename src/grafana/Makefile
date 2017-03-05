# @SI_Copyright@
# @SI_Copyright@

ROLLROOT       = ../../
RPM.STRATEGY	= copy

include $(STACKBUILD)/etc/CCRules.mk

refresh::
	rm -f ./RPMS/*;
	(						\
		reposync -c ./grafana.repo -r grafana -p ./RPMS -n --norepopath; \
		VERS=$(shell rpm -qp --qf %{VERSION} ./RPMS/grafana*.rpm); \
		echo "NAME=grafana" > version.mk;		\
		echo "VERSION=$$VERS" >> version.mk;	\
	)

rpm::
	cp -p ./RPMS/$(NAME)*.x86_64.rpm $(REDHAT.RPMS)/$(ARCH)

clean::
