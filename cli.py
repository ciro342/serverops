import typer
from commands.inventory import app_inventory
from commands.ping import app_ping
from commands.ssh import app_ssh
from commands.service import app_service
from commands.logs import app_log
app=typer.Typer()

app.add_typer(app_inventory,name="inventory")
app.add_typer(app_ssh,name="ssh")
app.add_typer(app_ping,name="ping")
app.add_typer(app_service,name="service")
app.add_typer(app_log,name="log")
if __name__=="__main__":
    app()
    
