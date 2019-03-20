import http.client
import json
import termcolor

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

people = json.loads(data1)

print("CONTENT: ")

print("Total people in the database: ".format(len(people)))

for person in people:

    print()
    termcolor.cprint("Name: ", 'green', end='') # end='' to have the information in the same line
    print(person['Name'])
    termcolor.cprint("Age: ", 'green', end='')
    print(person['Age'])

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(person['Phone_numbers']))

    for i,num in enumerate(person['Phone_numbers']):
        termcolor.cprint("  Phone {}".format(i), 'blue')

        termcolor.cprint("      Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("      Number: ", 'red', end='')
        print(num['number'])
