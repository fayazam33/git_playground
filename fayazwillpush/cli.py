import subprocess
import typer
import json
import os

app = typer.Typer()

CONFIG_FILE = os.path.expanduser("~/.fayazpush.json")


def save_config(repo_url):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"repo": repo_url}, f)


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return None
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


@app.command()
def init(repo_url: str):

    save_config(repo_url)

    subprocess.run(["git", "init"])
    subprocess.run(["git", "branch", "-M", "main"])

    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", repo_url])

    print("✓ Repo initialized and saved! ")


@app.command()
def push(message: str = "Auto commit"):

    config = load_config()

    if not config:
        print("No repo found. Run: fayazpush init <repo_url>")
        return

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    print("Fayaz Pushed it successfully!")