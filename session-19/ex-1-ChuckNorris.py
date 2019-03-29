import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count", "/categories", "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
conn = http.client.HTTPSConnection(HOSTNAME)

for i in ENDPOINT:
    conn.request(METHOD, i, None, headers)
    r1 = conn.getresponse()

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()
    # -- Generate the object from the json file
    jokes = json.loads(text_json)

    if 'count' in i:
        print("Number of jokes: ", jokes['value'])
    elif 'categories' in i:
        print("Names of the different categories: ", jokes['value'])
        print("There are {} categories.".format(len(jokes['value'])))
    elif 'random' in i:
        print("Random joke: {}".format(jokes['value']['joke']))
    else:
        print("Error")