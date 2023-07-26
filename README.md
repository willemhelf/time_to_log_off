# Time to Log Off
#### Python script that lets you tweet straight from your code editor or teminal.

##### How to use it

1) Create and set up a Twitter Developer account and get your API key and consumer secret. [Here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) are some good instructions.
2) Make sure your Python version is up-to-date and then install ```tweepy``` in the command line with ```pip install tweepy```.
3) Clone this repo into any folder you'd like – you can run this either from the terminal or directly through your code editor.
4) Place your API and client keys in a ```config.py``` file, making sure to name the variables the same as the ones in the ```tweet_poster.py``` file. I <em>highly</em> recommend adding the ```config.py``` file to a ```.gitignore``` file, as this contains private information about the Twitter account you'll be posting from.
5) In the ```update_status``` function write out whatever tweet you want. 
6) Run the code straight from your text editor or terminal and check if the tweet posted. Yay :)
