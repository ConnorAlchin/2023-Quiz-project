

#allows user to choose what times table  they are quized on
times = int(input("Enter a timetable that you would like to be tested on:"))
max_num = int(input("Enter the maximum value for your timetable:"))
max_num += 1
score = 0

print("You will be tested on the {} times table".format(times))

#The code to see if the answer is correct
for item in range(1, max_num):
   answer = item * times
   guess = int(input("{} times {} is ".format(item, times)))
   if guess == answer:
       print("Correct")
       score += 1
   else:
       print("Incorrect")
       print("{} times {} is {}".format(item, times, answer))