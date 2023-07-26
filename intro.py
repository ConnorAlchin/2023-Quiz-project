print("welcome to a math quiz")


#functios go here
def yes_no(question):
    valid = False
    while not valid:
        response = input (question) .lower()

        #Makes it so user can use each response for a yes/no response
        if response == "yes" or response == "y":
         response = "yes"
         return response
    
        elif response == "no" or response == "n":
            response = "no"
            return response
        #makes sure user will say yes/no
        else:
           print("please awnser yes/no")

#function to display instructions
def instructions():
  print("welcome to the math quiz")
  print("Awnser as many questions as you can without losing all three of your lives")


# *** MAIN ROUTINE ***
# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
# if user hasn't played before instructions are displayed
if played_before == "no":
  instructions()
