#variables
score_rate = 0
total_string = 0
upper_count = 0
lower_count = 0
num_count = 0 

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

# check for upper and lower characters = +1 to counter for upper and lower
for i in password :
    if i.isupper():
        uppercase = True
        upper_count+=1
    elif i.islower():
        lowercase = True
        lower_count+=1

# outputs if requirements are met
if lowercase == True:
    print("Your password contains atleast one lowercase character ")
    print("Password has total lowercase of :",lower_count )
    score_rate = score_rate + lower_count / 3
    print ("score : " , (score_rate))
if uppercase == True:
    print("Your password contains atleast one uppercase character")
    print("Password has total uppercase character of :",upper_count )
    score_rate = score_rate + upper_count / 3
    print ("score : " , (score_rate))
if num == True:
    print("Your password contains atleast one number")
    score_rate = num_count/5
    print ("num counter is ", num_count)
    print ("score : " , (score_rate))
if symbol == True:
    print("Your password contains atleast one special symbol")

# points added to each individual variable if it is true password is ONLY
    

if symbol == True :
  score_rate = score_rate + 1

if lowercase and uppercase and num and symbol ==True:
    score_rate = score_rate + lower_count*5 + upper_count +10 + num_count*10

score_ratings()

if score_rate <= 20:
    print("Your password is rated very low")
elif score_rate >= 21 or score_rate <= 40:
    print("Your password is rated low")
elif score_rate >=41 or score_rate <= 70:
    print("Your password is rated medium")
elif score_rate >= 71 or score_rate <= 80:
    print("Your score is rated high")
else:
    print("You have a very secure password")

