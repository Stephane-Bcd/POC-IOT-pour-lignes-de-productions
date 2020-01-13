
# Creating Vhosts
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT http://localhost:15672/api/vhosts/Client1

# Creating users
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"client1","tags":""}' \
    http://localhost:15672/api/users/client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"consumer1","tags":""}' \
    http://localhost:15672/api/users/consumer1
	
# Put permissions to vhosts for each user
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client1/client1


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":"","read":".*"}' \
    http://localhost:15672/api/permissions/Client1/consumer1

# Create Exchanges
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"direct","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client1/Client1-Usine1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"fanout","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client1/Client1-Usine2

# Create Queues
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client1/Client1-Usine1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client1/Client1-Usine2


# Creating bindings
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"usine1","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1/e/Client1-Usine1/q/Client1-Usine1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"usine2","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1/e/Client1-Usine2/q/Client1-Usine2





