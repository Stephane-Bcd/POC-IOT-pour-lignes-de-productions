
# Creating Vhosts
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT http://localhost:15672/api/vhosts/Client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT http://localhost:15672/api/vhosts/Client1-BackHome
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT http://localhost:15672/api/vhosts/Client2
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT http://localhost:15672/api/vhosts/Client2-BackHome

# Creating users
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"client1","tags":""}' \
    http://localhost:15672/api/users/client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"client2","tags":""}' \
    http://localhost:15672/api/users/client2
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"consumer1","tags":""}' \
    http://localhost:15672/api/users/consumer1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"consumer2","tags":""}' \
    http://localhost:15672/api/users/consumer2
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"transmitter1","tags":""}' \
    http://localhost:15672/api/users/transmitter1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"passsword":"transmitter2","tags":""}' \
    http://localhost:15672/api/users/transmitter2

# Put permissions to vhosts for each user
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client1/client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client1-BackHome/client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client2/client2
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client2-BackHome/client2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":"","read":".*"}' \
    http://localhost:15672/api/permissions/Client1/consumer1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":"","read":".*"}' \
    http://localhost:15672/api/permissions/Client2/consumer2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client1-BackHome/transmitter1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"configure":".*","write":".*","read":".*"}' \
    http://localhost:15672/api/permissions/Client2-BackHome/transmitter2

# Create Exchanges
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"fanout","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client1/Client1-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"fanout","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client1/Client1-Maison2

curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"fanout","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client2/Client2-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"fanout","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client2/Client2-Maison2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"direct","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client1-BackHome/Client1-BackHome

curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"type":"direct","auto_delete":false,"durable":true,"internal":false,"arguments":{}}' \
    http://localhost:15672/api/exchanges/Client2-BackHome/Client2-BackHome

# Create Queues
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client1/Client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client2/Client2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client1-BackHome/Client1-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client1-BackHome/Client1-Maison2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client2-BackHome/Client2-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPUT -d'{"auto_delete":false,"durable":true,"arguments":{}}' \
    http://localhost:15672/api/queues/Client2-BackHome/Client2-Maison2

# Creating bindings
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1/e/Client1-Maison1/q/Client1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1/e/Client1-Maison2/q/Client1


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"","arguments":{}}' \
    http://localhost:15672/api/bindings/Client2/e/Client2-Maison1/q/Client2
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"","arguments":{}}' \
    http://localhost:15672/api/bindings/Client2/e/Client2-Maison2/q/Client2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"client1maison1","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1-BackHome/e/Client1-BackHome/q/Client1-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"client1maison2","arguments":{}}' \
    http://localhost:15672/api/bindings/Client1-BackHome/e/Client1-BackHome/q/Client1-Maison2
q/Client2


curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"client2maison1","arguments":{}}' \
    http://localhost:15672/api/bindings/Client2-BackHome/e/Client2-BackHome/q/Client2-Maison1
curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"routing_key":"client2maison2","arguments":{}}' \
    http://localhost:15672/api/bindings/Client2-BackHome/e/Client2-BackHome/q/Client2-Maison2


# Send a message on an exchange:
# curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"properties":{},"routing_key":"","payload":"test from client","payload_encoding":"string"}' \
#     http://localhost:15672/api/exchanges/Client1/Client1-Maison1/publish

# result: works


# curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"properties":{},"routing_key":"client1maison1","payload":"test to client","payload_encoding":"string"}' \
#     http://localhost:15672/api/exchanges/Client1-BackHome/Client1-BackHome/publish

# result: works


# Get Messages:
# curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"count":5,"requeue":true,"encoding":"auto","truncate":50000,"ackmode":"ack_requeue_false"}' \
#     http://localhost:15672/api/queues/Client1/Client1/get


# curl -i -u rabbitmq:rabbitmq -H "content-type:application/json" -XPOST -d'{"count":5,"requeue":true,"encoding":"auto","truncate":50000,"ackmode":"ack_requeue_false"}' \
#     http://localhost:15672/api/queues/Client1-BackHome/Client1-Maison1/get

# Result: both worked fine !



