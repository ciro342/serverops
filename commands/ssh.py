import paramiko
import yaml
import typer


app__ssh=typer.Typer()

servs="config/serves.yml"
client=paramiko.SSHClient()
def conecct(name:str,port:int,ip:str,user:str,command:str,):
    with open(servs) as f:
        data=yaml.safe_load(f)   
    print("Iniciando conexion...")
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #for  a real server xd
    #client.connect(hostname=data[name],username=user,port=data[port],key_filename=f"/home/cyber/.ssh/id_ed25519")
    client.connect(hostname=data[name],username=user,port=data[port],key_filename=f"/home/cyber/.ssh/id_ed25519")

    #    client.close()


