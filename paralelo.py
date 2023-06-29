import threading
import paramiko
import time
import pandas as pd


resultados = []
def connect_ssh(ip, username, password, timeout=45):
    # Crear una instancia del cliente SSH
    client = paramiko.SSHClient()
            
    # Agregar la clave del host automáticamente (solo para fines de prueba,
    # en producción se debe manejar de manera segura)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
    # Establecer el timeout para intentar establecer la conexión
    client.connect(ip, username=username, password=password, timeout=timeout)
            
    # Realizar operaciones SSH aquí...
            
    # Cerrar la conexión SSH
    client.close()
            
    print(f"Conexión SSH exitosa al host {ip}")
    global resultados
    resultados.append([ip,"Correcto"])

def conection(ip,timeout=0):
    # Ejemplo de uso
    #ip = "10.10.50.40"
    username = "voseda"
    password = "S4ndb0x"
    #password = "C1sc0123.."
    

    try:
            # Intentar la conexión con timeout de 5 segundos
            connect_ssh(ip, None, None, timeout=15)
    except:
            print("a")
            # Si el timeout ocurre, intentar la conexión con credenciales locales

            try:

                connect_ssh(ip, username, password)
                
                
                    
            except paramiko.AuthenticationException:
                    print(f"Fallo de autenticación SSH para el host {ip}")
                    global resultados
                    resultados.append([ip,"Fail"])
                    # Abrir el archivo en modo de escritura para agregar contenido
                    with open('archivo.txt', 'a') as file:
                        # Escribir nuevos datos en el archivo
                        file.write(ip+'\n')
                        

            except paramiko.SSHException as e:
                    print(f"Fallo de conexión SSH para el host {ip}: {str(e)}")
                    with open('error.txt', 'a') as file:
                        # Escribir nuevos datos en el archivo
                        file.write(ip+'\n')
            except Exception as e:
                    print(f"Error inesperado al conectar al host {ip}: {str(e)}")
                    with open('error.txt', 'a') as file:
                        # Escribir nuevos datos en el archivo
                        file.write(ip+'\n')


# Abrir el archivo en modo de lectura
with open('IPs.txt', 'r') as file:
        # Leer el contenido del archivo
    contenido = file.read()

contenido = contenido.split("\n")
intervalo = 52
i = 0
f = intervalo
# Crear una lista para almacenar los hilos
hilos = []
conteo2 = 0
# Crear y ejecutar un hilo para cada parámetro
for _ in range(0,7):
    
    #print(contenido[i:f])
    print(i,f,intervalo,"antes")
    for ip in contenido[i:f]:
        conteo2+=1
        #print(i,f,contenido[i:f])
        hilo = threading.Thread(target=conection, args=(ip,))
        hilo.start()
        hilos.append(hilo)

    
    i = f
    if f+intervalo > len(contenido):
         f = -1
    else:
         f+= intervalo
    print(i,f,intervalo,"despues")
    time.sleep(60)
    
    # Esperar a que todos los hilos terminen su ejecución
for hilo in hilos:
    hilo.join()



df = pd.DataFrame(resultados,columns=["IP","Resultado"])
df.to_excel("resultados.xlsx")