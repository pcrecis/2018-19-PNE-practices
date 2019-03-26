# Example of accessing to the RandomCAT service for getting an URL
# of a random image of a CAT. This clients just print it on
# the console

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = ["/jokes/count, /categories, /jokes/random"]
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

count = 0
categories = []
count_cat = 0
joke_random = ""


for i in ENDPOINT:
    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    jokes = json.loads(text_json)

    if i == '/jokes/count':

        # -- Print the received URL
        print("Number of jokes: ", jokes['value'])

    elif i == '/categories':

        print("Names of the different categories: ", jokes['type'])
        print("There are {} categories.".format(len(jokes)))

