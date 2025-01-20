# community-finder

## tldr
```bash
brew install just
just setup
source .venv/bin/activate
just dev
just ping
code .env
```

## Setup Guide

### Tools Used
Python, [just](https://github.com/casey/just), [uv](https://docs.astral.sh/uv/)

### 1. Command Runner
Install *just* command runner, which will make it easier to remember the commands.

Use one of these of your choice, or refer to [the just docs](https://github.com/casey/just):

```bash
brew install just
npm install -g rust-just && alias just="rust-just"
apt install just
cargo install just
```

### 2. UV Package Manager + Virtual Environment
This project uses UV, a quick all-in-one Python package/environment tool. Using the `setup` recipe will install it, and you'll need to run the `source` program to activate the virtual environment.
```bash
just setup
source .venv/bin/activate
```

### 3. Generate BAML Client and Boot up Dev Server
We provide a shortcut to spin up the web server under the `dev` recipe.
```bash
just dev
```

### 4. Check the Server with a GET Request
Once the server is running, open a concurrent terminal and check whether it's up using the `ping` recipe.
```bash
just ping
```

### 5. Set up credentials and API keys
Open `.env` and add the keys for providers like OpenAI and Neo4J so you can access their API's.
```bash
code .env
```

## Coding Environment
VS Code + BAML Extension

### Modifications
The BAML devs suggest that you set in your VS Code's `settings.json`:
```
{
  "python.analysis.typeCheckingMode": "basic"
}
```
