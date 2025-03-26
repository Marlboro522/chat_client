"""Console script for chat_for_us."""
import chat_for_us

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for chat_for_us."""
    console.print("Replace this message by putting your code into "
               "chat_for_us.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
