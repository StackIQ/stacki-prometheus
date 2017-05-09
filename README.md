<h3>Stacki Prometheus for Monitoring</h3>

By default, stacki doesn't have monitoring built-in, which looks really crappy when you're doing demos for people who like pretty graphs with colors. 

It's also a problem if you're like me and don't want to have to check on every little thing to see if something is working like you think it should. So you build in monitoring, and if you have pretty graphs with colors, everything is working. Call me lazy or call me a philosopher, the end result is this pallet. 

<h3>The stacki-prometheus pallet</h3>
Monitoring is done on the frontend. I have not adapted this pallet to run the graphical pieces on a backend node. 

Software installed:
- prometheus 1.6.1
- grafana 4.2.0-1
- node_exporter 0.14.0 (provides physical machine metrics)
- stacki-dashboards (pre-populated dashboards for node_exporter, plain-old Docker, Docker Swarm mode, and Kubernetes)
- stacki-prometheus-commands (provides command to sync prometheus yaml config file.)

When you add and run the pallet, a config file, /opt/prometheus/etc/prometheus.yml, is created with the hosts listed in your database. If you add nodes, rerun the "stack sync prometheus" to add the new hosts to the file. 

<h3>Add the pallet</h3>

Get the pallet:
```
wget https://s3.amazonaws.com/stacki/public/pallets/4.0/open-source/stacki-prometheus-1.6.1-7.x.x86_64.disk1.iso
```

I'm assuming you have hosts, they're not installed yet. You either are running only bare metal machines, stacki-docker, or stacki-docker+stacki-kubernetes. I'm assuming you have run those pallets already. (If you're only doing this on bare metal machines with no docker and no kubernetes, you'll get machine monitoring without running any pallet other than the stacki-prometheus pallet.)

So what I'm saying here is run the stacki-prometheus pallet last, right before you power cycle your nodes.

It looks like this:

```

[root@stackdock ~]# stack list pallet
NAME              VERSION              RELEASE    ARCH   OS     BOXES
CentOS            7                    7.x        x86_64 redhat default
stacki            4.0_20170414_c4aff2a 7.x        x86_64 redhat default
CentOS-Updates    4.0_20170414_c4aff2a 7.x        x86_64 redhat default
stacki-docker     17.03.1              7.x_phase2 x86_64 redhat default
stacki-prometheus 1.6.1                7.x        x86_64 redhat default


# stack run pallet stacki-prometheus | bash
CentOS-7-7.x                                                                                                                                                       | 3.6 kB  00:00:00
CentOS-Updates-4.0_20170414_c4aff2a-7.x                                                                                                                            | 2.9 kB  00:00:00
site-custom-cart                                                                                                                                                   | 2.9 kB  00:00:00
stacki-4.0_20170414_c4aff2a-7.x                                                                                                                                    | 2.9 kB  00:00:00
stacki-docker-17.03.1-7.x_phase2                                                                                                                                   | 2.9 kB  00:00:00
stacki-prometheus-1.6.1-7.x                                                                                                                                        | 2.9 kB  00:00:00
(1/7): CentOS-7-7.x/primary_db                                                                                                                                     | 5.6 MB  00:00:00
(2/7): CentOS-7-7.x/group_gz                                                                                                                                       | 155 kB  00:00:00
(3/7): CentOS-Updates-4.0_20170414_c4aff2a-7.x/primary_db                                                                                                          | 1.4 MB  00:00:00
(4/7): site-custom-cart/primary_db                                                                                                                                 | 5.3 kB  00:00:00
(5/7): stacki-4.0_20170414_c4aff2a-7.x/primary_db                                                                                                                  |  30 kB  00:00:00
(6/7): stacki-docker-17.03.1-7.x_phase2/primary_db                                                                                                                 | 851 kB  00:00:00
(7/7): stacki-prometheus-1.6.1-7.x/primary_db                                                                                                                      | 3.0 kB  00:00:00
Resolving Dependencies
--> Running transaction check
---> Package node_exporter.x86_64 0:0.14.0-7.x will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================================
 Package                                    Arch                                Version                                    Repository                                                Size
==========================================================================================================================================================================================
Installing:
 node_exporter                              x86_64                              0.14.0-7.x                                 stacki-prometheus-1.6.1-7.x                              2.4 M

Transaction Summary
==========================================================================================================================================================================================
Install  1 Package

Total download size: 2.4 M
Installed size: 8.5 M
Downloading packages:
node_exporter-0.14.0-7.x.x86_64.rpm                                                                                                                                | 2.4 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : node_exporter-0.14.0-7.x.x86_64                                                                                                                                        1/1
  Verifying  : node_exporter-0.14.0-7.x.x86_64                                                                                                                                        1/1

Installed:
  node_exporter.x86_64 0:0.14.0-7.x

Complete!
Package foundation-py-requests-2.5.0-7.x.x86_64 already installed and latest version
Nothing to do
Resolving Dependencies
--> Running transaction check
---> Package grafana.x86_64 0:4.2.0-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================================
 Package                                 Arch                                   Version                                 Repository                                                   Size
==========================================================================================================================================================================================
Installing:
 grafana                                 x86_64                                 4.2.0-1                                 stacki-prometheus-1.6.1-7.x                                  44 M

Transaction Summary
==========================================================================================================================================================================================
Install  1 Package

Total download size: 44 M
Installed size: 128 M
Downloading packages:
grafana-4.2.0-1.x86_64.rpm                                                                                                                                         |  44 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : grafana-4.2.0-1.x86_64                                                                                                                                                 1/1
### NOT starting on installation, please execute the following statements to configure grafana to start automatically using systemd
 sudo /bin/systemctl daemon-reload
 sudo /bin/systemctl enable grafana-server.service
### You can start grafana-server by executing
 sudo /bin/systemctl start grafana-server.service
POSTTRANS: Running script
  Verifying  : grafana-4.2.0-1.x86_64                                                                                                                                                 1/1

Installed:
  grafana.x86_64 0:4.2.0-1

Complete!
Resolving Dependencies
--> Running transaction check
---> Package prometheus.x86_64 0:1.6.1-7.x will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================================
 Package                                  Arch                                 Version                                    Repository                                                 Size
==========================================================================================================================================================================================
Installing:
 prometheus                               x86_64                               1.6.1-7.x                                  stacki-prometheus-1.6.1-7.x                                10 M

Transaction Summary
==========================================================================================================================================================================================
Install  1 Package

Total download size: 10 M
Installed size: 49 M
Downloading packages:
prometheus-1.6.1-7.x.x86_64.rpm                                                                                                                                    |  10 MB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : prometheus-1.6.1-7.x.x86_64                                                                                                                                            1/1
  Verifying  : prometheus-1.6.1-7.x.x86_64                                                                                                                                            1/1

Installed:
  prometheus.x86_64 0:1.6.1-7.x

Complete!
Resolving Dependencies
--> Running transaction check
---> Package stacki-dashboards.x86_64 0:1.0-7.x will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================================
 Package                                        Arch                                Version                                Repository                                                Size
==========================================================================================================================================================================================
Installing:
 stacki-dashboards                              x86_64                              1.0-7.x                                stacki-prometheus-1.6.1-7.x                               13 k

Transaction Summary
==========================================================================================================================================================================================
Install  1 Package

Total download size: 13 k
Installed size: 158 k
Downloading packages:
stacki-dashboards-1.0-7.x.x86_64.rpm                                                                                                                               |  13 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : stacki-dashboards-1.0-7.x.x86_64                                                                                                                                       1/1
  Verifying  : stacki-dashboards-1.0-7.x.x86_64                                                                                                                                       1/1

Installed:
  stacki-dashboards.x86_64 0:1.0-7.x

Complete!
Resolving Dependencies
--> Running transaction check
---> Package stacki-prometheus-commands.x86_64 0:3.2-7.x will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==========================================================================================================================================================================================
 Package                                               Arch                              Version                             Repository                                              Size
==========================================================================================================================================================================================
Installing:
 stacki-prometheus-commands                            x86_64                            3.2-7.x                             stacki-prometheus-1.6.1-7.x                            4.3 k

Transaction Summary
==========================================================================================================================================================================================
Install  1 Package

Total download size: 4.3 k
Installed size: 4.6 k
Downloading packages:
stacki-prometheus-commands-3.2-7.x.x86_64.rpm                                                                                                                      | 4.3 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : stacki-prometheus-commands-3.2-7.x.x86_64                                                                                                                              1/1
  Verifying  : stacki-prometheus-commands-3.2-7.x.x86_64                                                                                                                              1/1

Installed:
  stacki-prometheus-commands.x86_64 0:3.2-7.x

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
adding stack40k8s-prometheus datasource...
{"id":1,"message":"Datasource added","name":"stack40k8s-prometheus"}
adding node_exporter metrics...
<Response [200]>
200
{"slug":"node-exporter-server-metrics","status":"success","version":0}
adding docker monitoring
<Response [200]>
200
{"slug":"docker-monitoring","status":"success","version":0}
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

The stacki-dashboards prepopulate machine, docker, and kubernetes dashboards for Grafana. If you don't want/like them, you're free to download whatever you need and adapt from grafana.net. Just remove the ones already loaded.

The prometheus datasource is also preloaded and defaults to `hostname-prometheus`. You should see this on the Grafana page.

You should now be able to reach your grafana and promethes pages at:

Prometheus: http://frontend.ip:9090 
Grafana: http://frontend.ip:3000

If you want these to ports open to the world, use the following firewall rules:
```
export HOST=`hostname`

/opt/stack/bin/stack add host firewall ${HOST} network=all table=filter rulename=PROMETHEUS service="9090" protocol="tcp" action="ACCEPT" chain="INPUT" flags="-m state --state NEW" comment="Prometheus"

/opt/stack/bin/stack add host firewall ${HOST} network=all table=filter rulename=GRAFANA service="3000" protocol="tcp" action="ACCEPT" chain="INPUT" flags="-m state --state NEW" comment="Prometheus"
```

Then these ports will be available for anyone hitting your frontend.

There's lots of work that can be done here in terms of sync configuration, scrape_configs in prometheus etc. We are more than happy to have help to make this better. 

