from core.ssh_client import conecct
from core.ssh_client import ejecutar_comando
import core.logger
import typer
from rich.console import Console
console=Console()
app_log=typer.Typer()

@app_log.command()
def logs(name:str,logtype:str,service:str):
    try:
        match logtype:
            case "error":
                print("viendo logs de errores")
                comand_complt=f"tail -n 50 /var/log/{service}/error.log "
                res=ejecutar_comando(name,comand_complt)
                if len(res)==0:
                    print("")
                    console.print("[bold red]X No hay logs de error ---- [/ bold red]")
                else:
                    print("="*50)
                    print("")
                    print(res)
                    print("="*50)
    except Exception as e:
        print("ERROR: ",e)