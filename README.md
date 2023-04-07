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

Also, run this pre-commit setup script so that code quality 
can be enforced using `black` before contributions are added to version control

```bash
pre-commit install
```

Make an account with [openai](https://chat.openai.com/auth/login) 
and then copy your [api key](https://platform.openai.com/account/api-keys) 
and [organization id](https://platform.openai.com/docs/api-reference/authentication)
into a `.env` file like so:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_API_ORG=org-xxxxxxxxxxxxxxxxxxxxxxxx
```

## To Run

Run `app.py`  and navigate to http://127.0.0.1:5000
in your browser to output a list of models 
you have access to with your account:

```bash
python app.py
```
