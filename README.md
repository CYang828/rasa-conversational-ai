# A simple example of Chinese chatbot using RASA framework (developing...)

## Getting Started
Command line demo:
![](asset/example_1.png)

## Usage 

1. Install require packages
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
python -m pip install -U pip
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

refer to: [poetry documentation](https://python-poetry.org/docs/) and newest [official Rasa NLU document](https://rasa.com/docs/)


2. Train model by running:

   If you specify your project name in configure file, this will save your model at /models/your_project_name. 

   Otherwise, your model will be saved at /models/default

```
rasa train --num-threads 4 % multi-threads for efficient computation
```

5. Run the raas action server and interact with the bot on the command line interfact:

```
rasa run actions & rasa shell
```


6. Open a new terminal and now you can curl results from the server, for example:

```
rasa x
```

7. Chat with your Conversational AI and Enjoy/Develop it.
