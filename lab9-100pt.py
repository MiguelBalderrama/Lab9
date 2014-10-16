############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
x = 1
while x == 1:
    print "What is your temperature?"
    userinput1 = int(raw_input())
    print "Have you been sick in the last 24 hours?"
    userinput2 = raw_input()
    print "Have you recently travled traveled to Africa?"
    Africa = raw_input()
    if userinput1 < 105:
        x = 1
    if userinput1 > 102 and userinput2 == "yes":
        print "Go to the hospital."
        x = x - 1
    if userinput2 == "yes" and Africa == "yes":
        print "Go to the hospital."
    if userinput1 > 100 and Africa == "yes":
        print "Go to the hospital" 
    print "Are you the last patient?"
    patient = raw_input()
    if patient == "yes":
        print ""