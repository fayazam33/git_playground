import subprocess
import typer

app = typer.Typer()

@app.command()
def push(
    repo_url: str,
    message: str = "Initial Commit"
):


    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Auto commit"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "remove", "origin"],
        ["git", "remote", "add", "origin", repo_url],
        ["git", "push", "-u", "origin", "main"]
    ]

    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
            print("✓", " ".join(cmd))
        except:
            pass

if __name__ == "__main__":
    app()