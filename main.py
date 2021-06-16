import random
def get_tof_statements():
  statements =  [] 
  statements.append(["Canada has the longest coastline in the world","T" ]) 
  statements.append(["The currency of Sweden is euro","F"])
  statements.append(["Berlin is the capital of germany","T"])
  statements.append(["The UK is about the same size as France","F"])
  statements.append(["Brasília is the capital city of Brazil","T"])
  statements.append(["The capital of Switzerland is Bern","T"])
  statements.append(["The name 'Monkey' is banned in Denmark","T"])
  statements.append(["The word 'Europe' originates from Rome","F"])
  statements.append(["Iceland is mosquito free","T"])
  statements.append(["The French flag was designed by Napoleon","F"])
  statements.append(["Paris is the capital of France. ","T"])
  statements.append(["There are no McDonald's restaurants in Jamaica.","T"])
  statements.append(["Switzerland has the highest rate of twins born in the world","F"])
  return statements

def play_truefalse_quiz():
  tof_statements= get_tof_statements()
  random.shuffle(tof_statements)
  score= 0
  for s in tof_statements:

    print("Print True and False:"  + s[0])
    guess= input("Enter T or F:  ")
    if guess == s[1]:
      print("Correct!")
      score = score + 1
    else:
      print ("Incorrect!")    
  print("Your final score is " + str(score)) 
  

def main_menu():
   print("***************************************")
   print("-------Welcome to Quiz!---------------- ")
   print("*--------------------------------------*")
   print("-------Please select an option:--------")
   print("----------------------------------------")
   print("*****1. Play True or False quiz*********")
   print("*****2. Play General Knowledge*********")
   print("*****3. Quit****************************")
   print("*****************************************")
   choice = input("Enter 1,2,3:")
   if choice=="1":
    play_truefalse_quiz()

    quit()
   elif choice== "3":
    print("Thankyou for playing!")  
    quit()
   elif choice=="2":
     general_knowledge

def general_knowledge():
  gkscore=0
  print("What is the capital of Germany? \n a.Paris\n b.Rome\n c.Berlin\n d.Munich")
  useranswer1= input("Your answer is: ") 
  actualanswer1= "c"
  if (useranswer1  != actualanswer1):
    print("sorry, incorrect answer")
  else:
    print("welldone")  
    gkscore= gkscore + 1

  print("Which of these countries does not have a monarchy?\n a.Liechtenstein\n b.Belgium \n c.Finland\n d.Norway")
  useranswer2=input("Your answer is: ") 
  actualanswer2= "c"
  if (useranswer2  != actualanswer2):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1

  print("Which of these countries is Europe’s smallest (by area)? \n a.Monacc \n b.San Marino \n c.Liechtenstein \n d.Vatican city")
  useranswer3=input("Your answer is: ") 
  actualanswer3= "d"
  if (useranswer3  != actualanswer3):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1             

  print("Which of these languages is the most commonly spoken first language in Europe? \n a.Germany\n b.English\n c.French\n d.Italian")
  useranswer4=input("Your answer is: ") 
  actualanswer4= "a"
  if (useranswer4  != actualanswer4):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1                

  print("What is the Capital of China?\n a.HongKong\n b.Beijing\n c.Harbing\n d.Jining")
  useranswer5=input("Your answer is: ") 
  actualanswer5= "a"
  if (useranswer5  != actualanswer5):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1   

  print("Which of these European countries does NOT currently have a monarchy?\n a.Andara\n b.Swedwn\n c.Hungary\n d.Nice try! None of them")
  useranswer6=input("Your answer is: ") 
  actualanswer6= "c"
  if (useranswer6  != actualanswer6):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1 

  print("Which of these European country's flags has the most different colours on it?\n a.Finland \n b.Estonia\n c.Greece\n ")
  useranswer7=input("Your answer is: ") 
  actualanswer7= "b"
  if (useranswer7  != actualanswer7):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1
    
  print("Which of these European countries does not have a border with Germany??\n a.Austria\n b.Italy\n c.France\n d.Denmark")
  useranswer8=input("Your answer is: ") 
  actualanswer8= "b"
  if (useranswer8  != actualanswer8):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1
    
  print("Where can you find Claude Monet's gardens?\n a.In the French region of Normandy\n b.In Paris,France\n c.In Amsterdam,the Netherlands\n d.In Portlligat,Catalonia,Spain")
  useranswer9=input("Your answer is: ") 
  actualanswer9= "a"
  if (useranswer9  != actualanswer9):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1
    
  print("Warsaw is the capital of which country?\n a.Austria\n b.Poland\n c.Hungary\n d.Lithuania")
  useranswer10=input("Your answer is: ") 
  actualanswer10= "b"
  if (useranswer10  != actualanswer10):
    print("sorry, Your answer is incorrect!")
  else:
    print("Welldone!")  
    gkscore= gkscore + 1 
  print("Your final score is"+ str(gkscore))           
    
    
     
main_menu()   
general_knowledge() 
play_truefalse_quiz()
