# @SI_Copyright@
# @SI_Copyright@
# @SI_Copyright@

import os
import os.path
import sys
import stack
import string
import stack.commands
import stack.text
import stack.api as api

class Command(stack.commands.HostArgumentProcessor,
		stack.commands.BoxArgumentProcessor,
		stack.commands.report.command):
	"""
	Output the Prometheus server configuration file.
	"""

	def getTargets(self,ports):
		targets = []
		host = self.getHostnames(['frontend'])
		targets.append('%s:9090' % host[0])

		hosts = self.getHostnames()
		allhosts = [ "%s:%s" % (target,port) for target in hosts for port in ports]
		return (targets + allhosts)
	
	def writePrometheusScrapeJobs(self,ports):
		# write the node exporter jobs and prometheus
		pdir = "/opt/prometheus/etc"
		if os.path.isfile(pdir + "/prometheus.job"):
			f = open(pdir + "/prometheus.job",'rb')
			stuff = (f.read())
			f.close()
			# and remove that pesky newline too
			self.addOutput('',stuff[0:len(stuff)-1])
			output = "      - targets: [\n          '"
			output += "',\n          '".join(self.getTargets(ports))
			self.addOutput('',output + "'")
			self.addOutput('',"         ]")
		
	def writePrometheusYAML(self):
		pdir = "/opt/prometheus/etc"
		self.addOutput('', '<stack:file stack:name="%s/prometheus.yml">' % pdir)
		if os.path.isfile(pdir + "/prometheus.main"):

			f = open(pdir + "/prometheus.main",'rb')
			stuff = (f.read())
			f.close()

			self.addOutput('',stuff)

	def getPorts(self):
		ports = ['9100']
		pallets = self.getBoxPallets()
		if 'stacki-docker' in [ x[0] for x in pallets]:
			ports.append('8080')
		if api.Call('list.attr',['docker.experimental==True']):
			ports.append('9323')

		if 'stacki-kubernetes' in [ x[0] for x in pallets]:
			ports.append('4194')

		return ports
		
	def run(self, params, args):
		ports = self.getPorts()
		self.beginOutput()
		self.writePrometheusYAML()
		self.writePrometheusScrapeJobs(ports)
		self.addOutput('', '</stack:file>')
		self.endOutput(padChar='')
