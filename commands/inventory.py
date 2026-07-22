import typer
import time
import logging
import yaml
from models.server import Server
from pathlib import Path
import core.logger

app_inventory=typer.Typer()

@app_inventory.command()
def listall():
    file=Path("config/servers.yml")
    if file.exists():
        with open("config/servers.yml") as f:
            data= yaml.safe_load(f) or {}
        if len(data) == 0:
            print("no hay nada en el archivo")
            logging.warning("No hay informacion en el archivo de servidores")
        else:
            for clave,valor in data.items():
                print(valor["name"],valor["ip"])
            logging.info("Se han listado los servidores")
    else:
        print("No existe el archivo indicado")
        logging.warning("El achivo de los servers no existen")

@app_inventory.command()
def add(name:str,ip:str,user:str,port:int):
    try:
        print("..")
        New_Server=Server(name,ip,user,port)
        data_dict = New_Server.to_dict() 
        with open("config/servers.yml") as f:
            data=yaml.safe_load(f) or {}

        data[name]=data_dict
        with open("config/servers.yml","w") as f:
            yaml.safe_dump(data,f)

        data[name]=data_dict
        with open("config/servers.yml","w") as f:
            yaml.safe_dump(data,f) 
        logging.info(f"Se ha agregado {name} a el archivo de servudiores")

    except FileNotFoundError:
        print("El archivo no existe ")
        data={}
        logging.warning("El archivo de servidores no existe / no se encuentra disponible")


@app_inventory.command()
def remove(name:str):
    try:
        with open("config/servers.yml") as f:
            data=yaml.safe_load(f) or {}
        if name not in data :
            print(f"{name} No existe  en la lista")
            logging.warning(f"No existe el server {name} en la lista de servidores")
        else:
            del data[name]
            print(f"Se ah elimidado {name} de forma correcta") 
            logging.info(f"Se ah eliminado {name} de la lista de servidores") 
            with open("config/servers.yml","w") as file:
                yaml.safe_dump(data,file)
    except FileNotFoundError:
        print("No se ah encontrado el archivo a la hora de eliminar")
        logging.error("No se ah encontrado el archivo de servidores al momento de eliminar")


@app_inventory.command()
def update(name_serv:str,key:str,value):
    try:
        with open("config/servers.yml") as f:
            data=yaml.safe_load(f) or {}
        if name_serv not in data:
            print("ese servidor no existe en el archivo")
            logging.warning(f"No existe el server en el archivo  {name_serv} ")
        else:
            #name_serv[f"{key}"]=f"{value}"
            data[name_serv][key]=value
            with open("config/servers.yml","w") as file:
                yaml.safe_dump(data,file)
            print("update hecho correctamente porfavor asegurese en el archivo.")
            logging.info(f"Se ah modificado el servidor {name_serv}")
           
    except FileNotFoundError:
        print("No se ah encontrado el archivo de los servidores :v ")
        logging.error("No se ah encontrado el archivo de los servidores .")