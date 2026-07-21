import typer
from commands.inventory import app_inventory

app=typer.Typer()
app.add_typer(app_inventory,name="inventory")

if __name__=="__main__":
    app()
    