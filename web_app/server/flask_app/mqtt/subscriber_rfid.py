import paho.mqtt.client as mqtt

global indices
indices = ('temp','has_mask','has_studentCard','has_alcohol','has_covidCard')
global n_paso
n_paso = 0
global diccionario
diccionario = {}
global rfid_data

def conectado(cliente,userdata,flags,rc):
    if rc == 0:
        print("Cliente conectado OK")
        cliente.subscribe("rfid")
    else:
        print("Cliente no se pudo conectar")
def receptor(cliente,userdata,mensaje):
    global indices
    global n_paso
    global diccionario
    global rfid_data
    rfid_data = mensaje.payload.decode()
    print(rfid_data)
    #diccionario[indices[n_paso]] = mensje
    #n_paso = n_paso + 1
    cliente.disconnect()
    if n_paso==5:
        n_paso = 0
        print(diccionario)
        cliente.disconnect()
        #cliente.loop_stop()
        
        '''diccionario = {
        'temp':37.4,
        'has_mask':true,
        'has_studentCard':false,
        'has_alcohol':false,
        'has_covidCard': true
        }
        '''
def main():
    global n_paso
    global diccionario
    global rfid_data
    cliente = mqtt.Client()
    cliente.connect("172.20.10.5",1883)

    cliente.on_connect = conectado
    cliente.on_message = receptor

    print("AQUI")
    
    
    cliente.loop_forever()
    print("Fin de programa")
    return rfid_data


if __name__=='__main__':
    main()