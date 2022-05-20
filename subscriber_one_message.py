from paho.mqtt.subscribe import simple
message = simple('vadim/message',
                 hostname='mqtt.pi40.ru',
                 port=1883,
                 client_id='python_rr22',
                 auth={'username':'vadim','password':'kKRV2J'})
print(message.payload.decode())