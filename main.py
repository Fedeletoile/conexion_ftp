from ftplib import FTP
from cred import host, user, password

#REALIZO LA CONEXION AL FTP
try:    
    with FTP(host) as ftp:
        ftp.login(user=user, passwd=password)
        print("[+] Conexion exitosa al FTP\n")
        ftp.cwd("/")
        for f in ftp.nlst():
            ftp.rename(f,f.upper())
                       
except Exception as e:
    print(f"[-] Por algun motivo fallo la conexion, a continuacion muestro el error \n{e}")

print("[+] Ha terminado correctamente")


