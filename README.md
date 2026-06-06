# 🚀 FayazwillPush

**FayazwillPush** is a simple CLI tool that automates Git + GitHub workflow in one command.

No more repeated git commands like:
```bash
git init
git add .
git commit -m "message"
git push


⚡ Features
🔥 One-command Git automation
📦 Saves GitHub repo locally
⚡ Fast commit + push workflow
🧠 Simple CLI using Typer
🚀 Beginner-friendly tool for developers

📦 Installation
pip install fayazwillpush

🚀 Usage
1. Initialize project (first time only)
fayazwillpush init https://github.com/username/repo.git
2. Push code
fayazwillpush push --message "Added new feature"

Or default message: fayazwillpush push

🧠 How it works
Stores repo URL locally in ~/.fayazpush.json
Uses Git commands internally
Automates commit + push process

Full Workflow-
fayazwillpush init https://github.com/user/project.git
fayazwillpush push --message "Initial commit"
fayazwillpush push --message "Updated model"

🛠 Tech Stack
Python 🐍
Typer CLI ⚡
Git automation 🔧

📌 Future Improvements
Auto GitHub repo creation
AI commit messages
Single command push (fayazwilpush)
Multi-repo support

👨‍💻 Author: Fayaz Ali Muktadir

