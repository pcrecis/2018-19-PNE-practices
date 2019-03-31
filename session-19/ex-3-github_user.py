import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/" # First endpoint
GITHUB_ID = input("Introduce the github username you want to know information about: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)
real_name = repos['name']
print("The real name of the github user {} is: {}".format(GITHUB_ID, real_name))

ENDPOINT = "/users/{}/repos".format(GITHUB_ID)    # Second endpoint
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)
repos_name = []

for i in range(len(repos)):
    repos_name.append(repos[i]['name'])

repos_int = ', '.join(repos_name)
print("The names of the repositories of {} are: {}".format(GITHUB_ID, repos_int))

ENDPOINT = "/repos/{}/2018-19-PNE-practices/commits".format(GITHUB_ID)    # Second endpoint
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)
#if repos['message'] == "not found":
    #print("The 2018-2019-PNE-repo does not exist in {} user.".format(GITHUB_ID))
print("The total number of commits to the 2018-2019-PNE-repo of {} is: {}".format(GITHUB_ID, len(repos)))

