import subprocess
import typer
import yaml
import subprocess
import logging
import core.logger

server_config="config/servers.yml"
app_ping=typer.Typer()
@app_ping.command()
def choose(name:str):
    print("escaneando...")
    try:
        with open(server_config) as f:
            data=yaml.safe_load(f) or {}
        serv=data.get(name)
        if name not in data:
            print("El servidor seleccionado no se encuentra en la lista ")
            logging.error(f"El servidor {name} no se enceuntra en la lista")
        else:
            ip=serv["ip"]
            print(ip)
            resul=subprocess.run(["ping","-c","3",f"{ip}"],capture_output=True,text=True)
            if resul.returncode==0:
                print(f"Si hay conexion con {name}")
                logging.info(f"Si hay conexion con ping para : {name}")
            else:
                print(f"No hay conexion para {name}")
                logging.error(f"No hay conexion para {name}")
    except FileExistsError:
        print("NO existe el archivo ")
    

