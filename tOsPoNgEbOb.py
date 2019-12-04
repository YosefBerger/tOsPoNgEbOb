#!/usr/bin/env python3

import sys

##########################################################
# This is the function that actually does the conversion #
##########################################################
def tOsPoNgEbOb(string):
    output = ""
    _count = 0
    
    # We want to start lowercase and switch back and fourth only on
    # the charecters that have the ability to switch case
    for c in string:
        if _isCased(c):
            if _count % 2 == 0:
                output = output + c.lower()
            else:
                output = output + c.upper()
            _count = _count + 1
        else:
            output = output + c
    return output


#####################################################
# Returns if the bassed char is able to swich cases #
#####################################################
def _isCased(c):
    if c.upper() == c.lower():
        return False
    else:
        return True


########################################################
# This is the main function called by the command line #
########################################################
if __name__ == "__main__":
    output = ""

    # If not arguments
    if len(sys.argv) == 1:
        print(tOsPoNgEbOb("Please provide an input"))
        exit()
    
    # If the user passed the file flag
    if sys.argv[1] == "-f":
        for i in range(2, len(sys.argv)):
            try:
                with open(sys.argv[i], 'r') as file_contents:
                    # If there is more than one file, add the file name to output
                    if len(sys.argv) > 3:
                        output = output + sys.argv[i] + ":\n"

                    # Add the spongebobified contents of the file to output
                    output = output + tOsPoNgEbOb(file_contents.read())

                    # If there is more than one file and this is not the last file, add some new lines
                    if i != len(sys.argv) - 1 and len(sys.argv) > 3:
                        output = output + "\n\n"
            
            # If one of the provided files fails, output error and fail
            except IOError:
                # Quote SpongeBob, season 2, episode 34a, "Welcome to the Chum Bucket"
                print("You: Open file " + sys.argv[i] + "\nPython: " + tOsPoNgEbOb("No, I don't really feel like it."))
                exit()
    
    # If the user asks for help, mock them
    elif (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("Me: Can you help me?\nThe programmer: " + tOsPoNgEbOb("Can you help me?"))

    # Or just use the arguments as the input
    else:
        for i in range(1, len(sys.argv)):
            output = output + sys.argv[i] + " "
        output = tOsPoNgEbOb(output)
    
    print(output)
