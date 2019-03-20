import json
import termcolor

f = open("people-ex1.json", "r")

people = json.load(f)

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

