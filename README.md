

# InstaBot

AI generated Instagram Messages

InstaBot is an AI powered chatbot which responds to Instagram Direct Messages, easily trainable to with any dataset.

## Installation

Firefox and [Firefox Web Driver](https://github.com/mozilla/geckodriver/releases) are required to run InstaBot

`export PATH=$PATH:/your/path/to/the/driver/driver`

Example:

`export PATH=$PATH:/Users/JohDoe/Downloads/geckodriver

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


## Usage

```instaBot.py [-h] [-t TIME] [-v] [-f FIRST_MESSAGE] username user chatbotType```

Username: Your instagram username
User: User to send messages to
Chatbot Type: Choose between generative chatbot (gen) or retrieval chatbot (ret)

Optional Arguments:

-t TIME: How much time between messages and refreshes (Default 20s)

-v: Display AI logging information

-f: Set the first message to send a user

Example:

```./instaBot myUserName targetUsername -t 10 -v -f "This is the first message that will be sent"```

This will send messages from myUserName to targetUsername every 10 seconds and will display AI logging information on the terminal, starting with the message "This is the first message that will be sent"

This information is available on the help page:

```./instaBot -h```

## Training the chatbots

### Training retrieval chatbot

A basic conversation file is provided (conversations.JSON), this file is used to train the retrieval bot. 

A model is already created with that JSON file.

Run the trainRetrievalBot.py script

`./trainRetrievalBot.py`

### Training generative chatbot

Different datasets are provided in the datasets directory, there are also scripts to clean up the data from different type of sets:

``` 
datasetFrom2Files.py
datasetFromTabFile.py
datasetFromYAMLFiles.py
datasetFromSeparatorFile.py
``` 

It is recommended to run the ``` shortenMovieCorpus.py``` script before training using the movie_lines.txt file.

Run the trainGenerativeBot.py script

`./trainGenerativeBot.py`

Modify the line that loads the dataset in the trainGenerativeBot script and the tokenizeData script

Example:

```
questions, answers = datasetFrom2Files.datasetFrom2Files("datasets/human_text.txt", "datasets/robot_text.txt")
``` 

### Testing chatbots

You can test the chatbots before running them in instagram using:
```
./generativeChatBot.py
./retreivalChatBot.py
```

## Running InstaBot

Whole program in its best version is ready to run as is using provided models, simply run the instaBot.py as shown in the usage section.

Let it run uninterrupted, no need to click on anything

Enjoy :)
