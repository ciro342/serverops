import yaml
import paramiko
import time
#server_config="config/servers.yml"
#with open(server_config) as f:
 #       data=yaml.safe_load(f)
#print(data["httpd"]) 
# 
# prueba de paramiko  
client=paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="localhost",username="ciro",port=2222,key_filename=f"/home/cyber/.ssh/id_ed25519")
canal=client.invoke_shell()
print("generando shell..")
time.sleep(1)
while True:
    comando = input(">> ")
    if comando == "exit":
        break
    canal.send(comando + "\n")
    time.sleep(0.5)
    print(canal.recv(9999).decode())
client.close()