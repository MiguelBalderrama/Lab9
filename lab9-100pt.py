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
while x == 1:
    print "what is your temperature?"
    userinput1 = int(raw_input())
    print "have you been sick in the last 24 hours?"
    userinput2 = raw_input()
    print "have you recently travelled to West Africa?"
    userinput3 = raw_input()
    if userinput1 >= 105 and userinput2 == "no":
        print "ok a doctor will visit you soon"
    elif userinput1 >= 102 and userinput2 == "yes":
        print "please wait for further diagnostics"
    elif userinput3 == "yes" and userinput1 >= 100:
        print "sounds like ebola dont touch anyone"
    print                                                                                                                                                                  
