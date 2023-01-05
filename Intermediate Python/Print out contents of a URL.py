#!/usr/bin/python

#Takes in a url and print out its contents. You need internet connection and http module

from http.client import HTTPConnection
url = input("Enter a valid URL: https://") #Takes url from user
conn = HTTPConnection(url) # Establish an HTTP connection to the URL
result = conn.getresponse() # Store the response returned from the URL
contents = result.read()
print(contents)
