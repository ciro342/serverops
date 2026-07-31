import typer
from typing  import Optional
from core.ssh_client import conecct
import time
app_ssh=typer.Typer()
from core.ssh_client import ejecutar_comando, abrir_canal

@app_ssh.command()
def conection(name: str, command: Optional[str] = None):
    if command is None:
        print(f"Abriendo shell para {name}..")
        client, canal = abrir_canal(name)
        while True:
            comando = input(">> ")
            if comando == "exit":
                print("chau")
                break
            canal.send(comando + "\n")
            time.sleep(0.5)
            print(canal.recv(9999).decode())
        client.close()
    else:
        print(f"Ejecutando '{command}' en '{name}'....")
        print(ejecutar_comando(name, command))