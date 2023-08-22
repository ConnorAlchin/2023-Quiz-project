print("*** Welcome to a math quiz ***")
print()

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
  print() 
  print("Awnser as many questions as you can without losing more than you   get right")
  print()



# assess number is valid and within range
def int_check(question):
  error = "Please enter a whole number between 0 and 100"
  valid = False
  while not valid:
    try:
      response = int(input(question))

      if response <= 0 or response > 100:
        print(error)
      else:
        valid = True
        return response
    except ValueError:
      print(error)


# *** MAIN ROUTINE ***
# ask user if played before using yes no function
played_before = yes_no("Have you played the game before? ")
print()
# if user hasn't played before instructions are displayed
if played_before == "no":
  instructions()
  

#allows user to choose what times table they are quized on
times = int_check("Enter a timetable that you would like to be tested on:")  

print()
max_num = int(input("Enter the maximum value for your timetable:"))
max_num += 1
score = 0

print()


print("You will be tested on the {} times table".format(times))

#The code to see if the given answer is correct
for item in range(1, max_num):
   answer = item * times
   guess = int(input("{} times {} is ".format(item, times)))
   if guess == answer:
       print("Correct")
       score += 1
   else: 
      print("Incorrect")
      print("{} times {} is {}".format(item, times, answer))

   