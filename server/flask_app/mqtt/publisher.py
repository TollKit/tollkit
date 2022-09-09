import paho.mqtt.client as mqtt
cliente = mqtt.Client()
cliente.connect("localhost",1883)

data = "HOLA TOLLKIT - PUBLICADOR"

cliente.publish("demo",data)

print("Fin de programa")