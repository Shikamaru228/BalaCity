from paho.mqtt.publish import single
single('vadim/one_message',
       payload='Ayaz loh!',
       hostname='mqtt.pi40.ru'
       port= ,
       client_id='python_gfg5',
       auth={'username':'vadim','password':kKRV2J})