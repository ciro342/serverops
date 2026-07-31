import typer
#import time
import logging
import yaml
from models.server import Server
from pathlib import Path
import core.logger
from rich.table import Table
from rich.console import Console
from rich.prompt import Confirm
console=Console()
server_config="config/servers.yml"
app_inventory=typer.Typer()

@app_inventory.command()
def listall():
    file=Path(server_config)
    if file.exists():
        with open("config/servers.yml") as f:
            data= yaml.safe_load(f) or {}
        if len(data) == 0:
            print("no hay nada en el archivo")
            logging.warning("No hay informacion en el archivo de servidores")
        else:
            table=Table("Nombre","IP","Usario","Puerto")
            for clave,valor in data.items():
              #  print(valor["name"],valor["ip"])
                table.add_row(f"{valor["name"]}",f"{valor["ip"]}",f"{valor["user"]}",f"{valor["port"]}")
            console.print(table)
            logging.info("Se han listado los servidores")
    else:
        print("No existe el archivo indicado")
        logging.warning("El achivo de los servers no existen")

@app_inventory.command()
def add(name:str,ip:str,user:str,port:int):
    try:
        New_Server=Server(name,ip,user,port)
        data_dict = New_Server.to_dict() 
        with open("config/servers.yml") as f:
            data=yaml.safe_load(f) or {}

        data[name]=data_dict
        with open("config/servers.yml","w") as f:
            yaml.safe_dump(data,f) 
        console.print(f"[bold green]✓ Servidor '{name}' agregado correctamente[/bold green]")
        logging.info(f" Se ha agregado {name} a el archivo de servudiores")
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
            if Confirm.ask(f"seguro que desea eliminar '{name}' ? "):
                del data[name]
                print(f"Se ah elimidado {name} correctamente") 
                logging.info(f"Se ah eliminado {name} de la lista de servidores") 
                with open("config/servers.yml","w") as file:
                    yaml.safe_dump(data,file)
            else:
                print("Cancelado")
    except FileNotFoundError:
        print("No se ah encontrado el archivo a la hora de eliminar")
        logging.error("No se ah encontrado el archivo de servidores al momento de eliminar")

@app_inventory.command()
def update(name_serv:str,key:str,value:str):
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
            console.print("[bold yellow]✓ update realizado correctamente porfavor asegurese en el archivo.[/bold yellow]")
            logging.info(f"Se ah modificado el servidor {name_serv}")
    except FileNotFoundError:
        print("No se ah encontrado el archivo de los servidores :v ")
        logging.error("No se ah encontrado el archivo de los servidores .")
