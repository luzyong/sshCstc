with open('ipp.txt', 'r') as file:
    # Leer el contenido del archivo
    contenido = file.read()

contenido = contenido.split("\n")
mi_lista_sin_vacios = [valor for valor in contenido if valor != '']
#print(mi_lista_sin_vacios)

with open('IPs.txt', 'a') as file:
    for ip in mi_lista_sin_vacios:
        print(ip)
        # Escribir nuevos datos en el archivo
        file.write(ip.replace(" ","")+'\n')
