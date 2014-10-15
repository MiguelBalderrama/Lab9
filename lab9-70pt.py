############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer
print "what number would you like to convert to fahrenheit?"
uinput = int(raw_input())
temp1 = uinput * 9
temp2 = temp1 / 5
temp3 = temp2 + 32
print temp3
