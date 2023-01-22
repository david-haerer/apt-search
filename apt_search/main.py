import httpx
import typer
from bs4 import BeautifulSoup

BASE_URL = "https://packages.ubuntu.com/search"

app = typer.Typer()


@app.command()
def main(filename: str, suite: str = "jammy", arch: str = "any"):
    r = httpx.get(
        BASE_URL,
        params={
            "mode": "exactfilename",
            "suite": suite,
            "section": "all",
            "arch": arch,
            "keywords": filename,
            "searchon": "contents",
        },
    )

    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    
    if soup.table is None:
        typer.echo(f"No package found for file '{filename}'!")
        raise typer.Exit(code=1)

    items = []
    start = True
    item = None

    for tr in soup.table.children:
        if tr.name != "tr":
            continue
        for td in tr.children:
            if td.name != "td":
                continue
            if start:
                item = td
                start = False
            else:
                items.append((item, td))
                start = True

    for file, package in items:
        package_name = typer.style(package.a.text, bold=True)
        typer.echo(package_name + ": " + file.text)


if __name__ == "__main__":
    app()
