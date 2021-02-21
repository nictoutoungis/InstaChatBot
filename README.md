# InstaBot

AI generated Instagram Messages

InstaBot is an AI powered chatbot which responds to Instagram Direct Messages, easily trainable to with any dataset.

# Installation

Firefox and [Firefox Web Driver](https://github.com/mozilla/geckodriver/releases) are required to run InstaBot

Python 3.7 is required

Clone the repository:

```git clone https://github.com/nictoutoungis/InstaBot.git```

Go into the project folder:

```cd InstaBot```

It is recommended to create and run within a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
````

Installing all modules, run:

```pip install -r requirements.txt```

Making files executables:

```chmod +x trainBot.py instaBot.py```

# Usage

```./instaBot.py username user [-v][-t TIME]```

Username: Your instagram username
User: User to send messages to

Optional Arguments:

\-t TIME: How much time between messages and refreshes
\-v: Display logging information

# Running first example

A JSON file is provided with template conversation topic and responses the AI will use to train.

Run the training script:

```./trainBot.py```

Run 
