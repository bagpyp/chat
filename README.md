# Chat

Using ChatGPT

## Requirements

If you haven't already, 
install Python 3.11 using brew

```bash
brew install python@3.11
```

Inside the directory for this repo, 
create and activate a virtual environment called `venv`
and load the dependencies needed for these scripts therein

```bash
/usr/local/bin/python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make an account with [openai](https://chat.openai.com/auth/login) 
and then copy your [api key](https://platform.openai.com/account/api-keys)
into a `.env` file like so:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Finally, run `main.py` to output a list of models 
you have access to with your account like so:

```bash
python main.py
```
