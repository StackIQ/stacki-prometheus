<h3>Stacki Prometheus for Monitoring</h3>

By default, stacki doesn't have a monitoring built-in, which looks really crappy when you're doing demos for people who like pretty graphs with colors. 

It's also a problem if you're like me and don't want to have to check on every little thing to see if something is working like you think it should, so you build in monitoring and if you have pretty graphs with colors, everything is working. Call me lazy or call me a philosopher, the end result is this pallet. 

<h3>The stacki-prometheus pallet</h3>
Monitoring is done on the frontend. I have not adapted this pallet to run on a backend node. 

Software installed:
- prometheus 1.5.2
- grafana 4.1.2-1486989747 (tell me what kind of version is that, seriously?)
- node_exporter 0.13.0 (provides physical machine metrics)
- stacki-dashboards (pre-populated dashboards for node_exporter, plain-old Docker, Docker Swarm mode, and Kubernetes)
- stacki-prometheus-commands (provides command to sync prometheus yaml config file.)

When you add and run the pallet, a config file, /opt/prometheus/etc/prometheus.yml, is created with the hosts listed in your database. If you add nodes, rerun the "stack sync prometheus" to add the new hosts to the file. 

<h3>Add the pallet</h3>

Get the pallet:
```
wget http://stacki.s3.amazonaws.com/public/pallets/3.2/open-source/stacki-prometheus-1.5.2-7.x.x86_64.disk1.iso

md5sum is:

MD5 (stacki-prometheus-1.5.2-7.x.x86_64.disk1.iso) = 004a9dce05197a669feb47bc49ab7cce
```

I'm assuming you have hosts, they're not installed yet. You either are running only bare metal machines, stacki-docker, or stacki-docker+stacki-kubernetes. I'm assuming you have run those pallets already. (If you're only doing this on bare metal machines with no docker and no kubernetes, you'll get machine monitoring without running any pallet other than the stacki-prometheus pallet.)

So what I'm saying here is run the stacki-prometheus pallet last, right before you power cycle your nodes.

It looks like this:

```
[root@stackdock ~]# stack list pallet
NAME               VERSION RELEASE    ARCH   OS     BOXES
os:                7.2     7.x        x86_64 redhat base
stacki:            3.2     7.x        x86_64 redhat default base
CentOS:            7       ---------- x86_64 redhat default
CentOS-Updates:    7.3     7.x        x86_64 redhat default
stacki-docker:     17.03.0 3.2_phase2 x86_64 redhat default
stacki-prometheus: 1.0     7.x        x86_64 redhat default
[root@stackdock ~]# stack run pallet stacki-prometheus | bash
Resolving Dependencies
--> Running transaction check
---> Package foundation-py-requests.x86_64 0:2.5.0-7.x will be installed
---> Package grafana.x86_64 0:4.1.2-1486989747 will be installed
---> Package node_exporter.x86_64 0:0.13.0-7.x will be installed
---> Package prometheus.x86_64 0:1.5.2-7.x will be installed
---> Package stacki-dashboards.x86_64 0:1.0-7.x will be installed
---> Package stacki-prometheus-commands.x86_64 0:3.2-7.x will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================
 Package                                    Arch                   Version                             Repository                             Size
===================================================================================================================================================
Installing:
 foundation-py-requests                     x86_64                 2.5.0-7.x                           stacki-3.2                            528 k
 grafana                                    x86_64                 4.1.2-1486989747                    stacki-prometheus-1.0                  43 M
 node_exporter                              x86_64                 0.13.0-7.x                          stacki-prometheus-1.0                 2.3 M
 prometheus                                 x86_64                 1.5.2-7.x                           stacki-prometheus-1.0                 9.6 M
 stacki-dashboards                          x86_64                 1.0-7.x                             stacki-prometheus-1.0                  13 k
 stacki-prometheus-commands                 x86_64                 3.2-7.x                             stacki-prometheus-1.0                 4.3 k

Transaction Summary
===================================================================================================================================================
Install  6 Packages

Total download size: 55 M
Installed size: 184 M
Downloading packages:
(1/6): foundation-py-requests-2.5.0-7.x.x86_64.rpm                                                                          | 528 kB  00:00:00
(2/6): node_exporter-0.13.0-7.x.x86_64.rpm                                                                                  | 2.3 MB  00:00:00
(3/6): prometheus-1.5.2-7.x.x86_64.rpm                                                                                      | 9.6 MB  00:00:00
(4/6): stacki-dashboards-1.0-7.x.x86_64.rpm                                                                                 |  13 kB  00:00:00
(5/6): stacki-prometheus-commands-3.2-7.x.x86_64.rpm                                                                        | 4.3 kB  00:00:00
(6/6): grafana-4.1.2-1486989747.x86_64.rpm                                                                                  |  43 MB  00:00:00
---------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                               68 MB/s |  55 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : node_exporter-0.13.0-7.x.x86_64                                                                                                 1/6
  Installing : stacki-dashboards-1.0-7.x.x86_64                                                                                                2/6
  Installing : grafana-4.1.2-1486989747.x86_64                                                                                                 3/6
### NOT starting on installation, please execute the following statements to configure grafana to start automatically using systemd
 sudo /bin/systemctl daemon-reload
 sudo /bin/systemctl enable grafana-server.service
### You can start grafana-server by executing
 sudo /bin/systemctl start grafana-server.service
  Installing : foundation-py-requests-2.5.0-7.x.x86_64                                                                                         4/6
  Installing : prometheus-1.5.2-7.x.x86_64                                                                                                     5/6
  Installing : stacki-prometheus-commands-3.2-7.x.x86_64                                                                                       6/6
  Verifying  : stacki-prometheus-commands-3.2-7.x.x86_64                                                                                       1/6
  Verifying  : prometheus-1.5.2-7.x.x86_64                                                                                                     2/6
  Verifying  : foundation-py-requests-2.5.0-7.x.x86_64                                                                                         3/6
  Verifying  : grafana-4.1.2-1486989747.x86_64                                                                                                 4/6
  Verifying  : stacki-dashboards-1.0-7.x.x86_64                                                                                                5/6
  Verifying  : node_exporter-0.13.0-7.x.x86_64                                                                                                 6/6

Installed:
  foundation-py-requests.x86_64 0:2.5.0-7.x         grafana.x86_64 0:4.1.2-1486989747          node_exporter.x86_64 0:0.13.0-7.x
  prometheus.x86_64 0:1.5.2-7.x                     stacki-dashboards.x86_64 0:1.0-7.x         stacki-prometheus-commands.x86_64 0:3.2-7.x

Complete!
Created symlink from /etc/systemd/system/multi-user.target.wants/node_exporter.service to /usr/lib/systemd/system/node_exporter.service.
RCS file: /opt/prometheus/bin/RCS/grafana_config,v
done
RCS file: /opt/prometheus/etc/RCS/prometheus.main,v
done
RCS file: /opt/prometheus/etc/RCS/prometheus.job,v
done
Created symlink from /etc/systemd/system/multi-user.target.wants/prometheus.service to /usr/lib/systemd/system/prometheus.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/grafana-server.service to /usr/lib/systemd/system/grafana-server.service.
Breathe...
Configuring Grafana...
Deleting datasources and dashboards.
adding stackdock-prometheus datasource...
{"id":1,"message":"Datasource added","name":"stackdock-prometheus"}
adding node_exporter metrics...
<Response [200]>
200
{"slug":"node-exporter-server-metrics","status":"success","version":0}
adding docker monitoring
<Response [200]>
200
{"slug":"docker-monitoring","status":"success","version":0}
adding docker swarm monitoring
<Response [200]>
200
{"slug":"docker-swarm-and-container-overview","status":"success","version":0}
<Response [200]>
200
{"slug":"docker-engine-metrics","status":"success","version":0}
Syncing prometheus.yml...
RCS file: /opt/prometheus/etc/RCS/prometheus.yml,v
done
active
```

What just happened here?

Well, we installed grafana, prometheus, node_exporter, and stacki-dashboards on the frontend. 

We created an /opt/prometheus/etc/prometheus.yml file that will get metrics from several ports on backend nodes depending on what pallets you have.

The following watched ports are cumulative:

If you only have bare metal you just get: 
node_exporter for metrics: port 9100

If you have Docker: port 8080

If you have Docker Swarm: port 9323

If you have Kubernetes: port 4194

Which are the default ports listed for metrics. If you have different ports, edit the /opt/prometheus.yml to do what you want to do and then don't ever run "stack sync prometheus" again. 

If you add hosts and want to sync prometheus to reflect that run:

```
stack sync prometheus
```

The stacki-dashboards prepopulate machine,docker, and kubernetes dashboards for Grafana. If you don't want/like them, you're free to download whatever you need and adapt from grafana.net. Just remove the ones already loaded.

The prometheus datasource is also preloaded and defaults to `hostname-prometheues`. You should see this on the Grafana page.

You should now be able to reach your grafana and promethes pages at:

Prometheus: http://frontend.ip:9090 
Grafana: http://frontend.ip:3000

If you want these to ports open to the world, use the following firewall rules:

```
There's lots of work that can be done here in terms of sync configuration, scrape_configs in prometheus etc. We are more than happy to have help to make this better. 

