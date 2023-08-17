
## Introduction:
This project is a Python implementation of a chatbot that can respond to user inputs on a variety of topics in tunisian dialect. The chatbot uses the ChatterBot library and is trained on multiple conversation corpora to improve its response quality. The chatbot has additional features such as retrieving weather information for a specific location, searching for news on a particular topic, and looking up definitions on Wikipedia.

## Installation:
To use the chatbot, you must have Python 3 installed. Install the necessary libraries by running the following command in the terminal:

Copy code
``` pip install chatterbot, chatterbot-corpus, newsapi-python, wikipedia ```

### Important !!!
When running the code you might have issues related to the python version you're using 
in my case i use python 3.9.12 and when installing chatterbot you might find yourself using an older version of the sqlalchemy module which causes an error.

In order to fix it you have to use the command : ```pip install --upgrade sqlalchemy```
et change the line 46 from  the file user\anaconda3(in my case)\lib\site-packages\chatterbot\storage\sql_storage.py in your user folder
from 
```
if not self.engine.dialect.has_table(self.engine, 'Statement'):
```
 to
```
if not sqlalchemy.inspect(self.engine).has_table('Statement'):
```
and import the sqlalchemy module in sql_storage.py
bu adding this line `import sqlalchemy`
