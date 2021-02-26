# InstaBot

AI generated Instagram Messages

InstaBot is an AI powered chatbot which responds to Instagram Direct Messages, easily trainable to with any dataset.

# Installation

Firefox and [Firefox Web Driver](https://github.com/mozilla/geckodriver/releases) are required to run InstaBot

Python 3.7 and above (3.9 not recommended) and Pip 21.0.0+ is required

Check Python and Pip version with:

```python3 --version```

```pip --version```

Installing Python3.x using Homebrew:

```
brew install python@3.x
brew link python@3.x
```

Clone the repository:

```git clone https://github.com/nictoutoungis/InstaBot.git```

Go into the project folder:

```cd InstaBot```

It is recommended to create and run within a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
````

Updating pip

```python3 -m pip install --upgrade pip ```


Installing all modules, run:

```pip install -r requirements.txt```


# Usage

```./instaBot.py username user [-v][-t TIME]```

Username: Your instagram username
User: User to send messages to

Optional Arguments:

-t TIME: How much time between messages and refreshes (Default 20s)

-v: Display AI logging information

Example:

```./instaBot myUserName targetUsername -t 10 -v```

This will send messages from myUserName to targetUsername every 10 seconds and will display AI logging information on the terminal

This information is available on the help page:

```./instaBot -h```


# Running InstaBot

A JSON file is provided with template conversation topic and responses the AI will use to train.

Run the training script:

```./trainBot.py```

Run instaBot:

```./instaBot yourusername targetusername```

Let it run uninterupted, no need to click on anything

Enjoy :)
