POC iot et cloud pour lignes de production


# Description

Project at ESILV School.
It regroups these IOT big subjects:
- Ingestion
- Storage
- Data routing
- Data visualisation
- API and managment

Mainly used technologies:
- docker
- shell
- data mocker
- rabbitmq
- mongodb
- apache nifi
- influxdb
- Chronograph
- Graphana
- Swagger API
- FTP


# How to test it

in "launch_all.sh", change path to the project root folder

install docker and docker-compose if not already done

Simply launch in terminal "launch_all.sh" shell script that will launch all containers and scripts to load data inside of it as well

Put needed templates into nifi.
You can find them here:
https://github.com/Stephane-Bcd/Dev-app-web-service-for-IOT---Fil-rouge/tree/master/nifi/templates

Configure yourself Grafana to have your own panels
