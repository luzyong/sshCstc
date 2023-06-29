import paramiko

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
    """try:
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
        
            
    except paramiko.AuthenticationException:
            print(f"Fallo de autenticación SSH para el host {ip}")
    except paramiko.SSHException as e:
            print(f"Fallo de conexión SSH para el host {ip}: {str(e)}")
            
    except Exception as e:
            print(f"Error inesperado al conectar al host {ip}: {str(e)}")"""

# Ejemplo de uso
#ip = "10.10.50.40"
username = "voseda"
#password = "S4ndb0x"
password = "C1sc0123.."

# Abrir el archivo en modo de lectura
with open('ip.txt', 'r') as file:
    # Leer el contenido del archivo
    contenido = file.read()

contenido = contenido.split("\n")

# Intentar la conexión SSH con timeout y luego con credenciales locales
for ip in contenido:
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
    
df = pd.DataFrame(resultados,columns=["IP","Resultado"])
df.to_excel("resultados.xlsx")
