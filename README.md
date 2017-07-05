# News-APP
A simple CommandLine application that consumes a public API using an HTTP library.

This is day 3 Task for the Andela Remote Learning Week. 
My app consumes the https://newsapi.org with the /articles endpoint
The app uses the requests HTTP library. http://docs.python-requests.org/en/latest/
I chose newsapi.org from a list of public apis compiled here https://github.com/toddmotto/public-apis/blob/master/README.md

Basically the app is implemented by two functions,

head_lines function 
Provides the core functionality to the api. 
It sends a request to the webservice, depending on user input, and receives back a response which it processes to print news items to the console accordingly.

main function
Acts as the entry point to the app and handles capturing input from the user and passing it on to the head_lines function

What next ?
Implementation of the UI using docopt
Writing tests for the app. (I need to learn MOcking in python) 


