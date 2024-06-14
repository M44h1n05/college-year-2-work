#variables
score_rate = 0
total_string = 0
upper_count = 0
upper_score = 0
lower_count = 0
lower_score = 0
num_count = 0
num_score = 0


#requirement subroutine
def main ():
    print ("*** Password must include 8 - 15 characters ***")
    print ("*** Password must include upper and lower case characters***")
    print ("*** Password must include special characters (eg: !%&*+=) ***")


main ()


# score rating subroutine
def score_ratings ():
    print ("*** very low == 20 points or less ***")
    print ("*** Low == 21- 40 points  ***")
    print ("*** Medium == 41- 70 points  ***")
    print ("*** High == 71- 80 points  ***")
    print ("*** Very High == 81 points and above ***")


score_ratings()

    
#userinput password and length counter for password characters
password = input ("Enter a password : ")
length = len (password)


#min and max requirement repeat loops
while length < 8 :
    password = input ("Re-Enter a password with more character: ")
    length = len (password)
    print ("characters in password = " , length)
while length > 15:
     password = input ("Re-Enter a password with less character: ")
     length = len (password)
     print ("characters in password = " , length)
else:
    length = len (password)
    print("password contains 8-15 characters")
    print ("your password contains a total characters of : " , length)


#variables assigned boolean value
lowercase = False
uppercase = False 
num = False
symbol = False


# if password is boolean true and matches valid inputs
for character in password: 
  if character in "abcdefghijklmnopqrstuvwxyz":
    lowercase = True
  elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    uppercase = True
  elif character in "0123456789":
      num = True
  elif character in "!%&*+-=":
      symbol = True


#*** check for numbers in string = +1 to num count
for i in password:
    if i.isdigit():
        num = True
        num_count = num_count+1
        num_score = num_count * 10

print(num_count)

# check for upper and lower characters = +1 to counter for upper and lower
for i in password :
    if i.isupper():
        uppercase = True
        upper_count+=1
        upper_score = upper_count * 5


for i in password:
    if i.islower():
        lowercase = True
        lower_count+=1
        lower_score = lower_count * 5


score_rate = upper_score + lower_score + num_score

print(score_rate)

if score_rate <= 21 or score_rate <= 40:
    print("Your password is rated low5")
elif score_rate >= 41 or score_rate <= 70:
    print("Your password is rated medium")
elif score_rate >=71 or score_rate <= 80:
    print("Your password is rated high")
else:
    print("You have a very secure password")



