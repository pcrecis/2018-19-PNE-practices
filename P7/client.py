import http.client
import json
import termcolor
from P1.Seq import Seq

#PORT = 8001
#SERVER = 'rest.ensembl.org'

#print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
#conn = http.client.HTTPConnection(SERVER, PORT)
conn = http.client.HTTPConnection('rest.ensembl.org')

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
FRAT1_data = json.loads(data1)

seq = FRAT1_data["seq"]

termcolor.cprint("Type of molecule: {}".format(FRAT1_data['molecule']), 'yellow')
termcolor.cprint("The sequence for the FRAT1 gene is: {}".format(seq), 'green')
print("")

seq = Seq(seq)

# Total length of the sequence:
tl = seq.len()

counter_A = seq.count_bases('A')
counter_C = seq.count_bases('C')
counter_T = seq.count_bases('T')
counter_G = seq.count_bases('G')
num_max = max(counter_A, counter_C, counter_T, counter_G)

dict_bases = dict(zip(['A', 'C', 'T', 'G'],[counter_A, counter_C, counter_T, counter_G]))

for key, value in dict_bases.items():
    if value == num_max:
        b_popular = key

termcolor.cprint("  CONTENT: ", 'blue')

print("There are {} bases in the FRAT1 gene.".format(tl))
print("Of the ({}) bases of the FRAT1 gene, {} are T bases.".format(tl, counter_T))
print("The most popular base in the FRAT1 gene is: {}, and its percentage: {}%".format(b_popular, seq.perc(b_popular)))

# Percentage of all bases:
for b in dict_bases:
    print("The percentage of {}, is: {}%".format(b, seq.perc(b)))
