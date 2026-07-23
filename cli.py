import typer
from commands.inventory import app_inventory
from commands.ping import app_ping
app=typer.Typer()
app.add_typer(app_inventory,name="inventory")
app.add_typer(app_ping,name="ping")
if __name__=="__main__":
    app()
    