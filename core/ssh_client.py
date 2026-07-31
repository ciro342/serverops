import paramiko
servs="config/serves.yml"
client=paramiko.SSHClient()
import time
from typing  import Optional
import yaml
servs = "config/servers.yml"

def conecct(name: str):
    with open(servs) as f:
        data = yaml.safe_load(f)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=data[name]["ip"],
        username=data[name]["user"],
        port=data[name]["port"],
        key_filename="/home/cyber/.ssh/id_ed25519"
    )
    return client

def ejecutar_comando(name: str, comando: str):
    client = conecct(name)
    stdin, stdout, stderr = client.exec_command(comando)
    resultado = stdout.read().decode()
    client.close()
    return resultado

def abrir_canal(name: str):
    client = conecct(name)
    canal = client.invoke_shell()
    return client, canal

