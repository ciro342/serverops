from rich.console import Console
from core.ssh_client import conecct
from core.ssh_client import ejecutar_comando
import typer
from core import logger
import logging

console=Console()
comandos=["status","stop","start","restart"]

app_service=typer.Typer()

@app_service.command()
def serv(name:str,action:str,deamon:str):
    comando_complt=f"supervisorctl {action} {deamon} "
    if action not in comandos:
        console.print(f"[bold red]x El comando {action} no esta dispobible [/bold red]")
    else:
        console.print(f"[bold yellow]Ejecutando comando {action}.... [/bold yellow]")
        res=ejecutar_comando(name,comando_complt)
        console.print("[bold green] Comando ejecutado correctamente [/bold green]")
        logging.info(f"Se ah ejecutado un comando en el servidor {name}")
        print("="*70)
        print(res)





        

    
    

