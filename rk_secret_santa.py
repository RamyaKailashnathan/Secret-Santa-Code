from pydoc import doc
import random
import json

def master_file_view():
    file1 = open("myfile.txt")  
    print(file1.read())
    file1.close() 
    return   

def assign_secret_santa():
    file1 = open("myfile.txt")
    
    friends_names_list=original_list=new_list=[]  #Intialiser tre tomme lister, og en dictionary
    santa_dict={}

    original_list=file1.readlines()                 #Brugte readlines()-funktionen, returnerer dette en liste over alle linjer i filen, 
                                                    # og de returnerede data er af listetype

    for element in original_list:                   #Brugte elements.strip()-funktion til at fjerne 
        new_list.append(element.strip())            # alle førende newline \n fra list elementerne        
    
    friends_names_list=new_list[:]                  #Kopiér indholdet (kun indholdet) af new_list til en friends_names_list

    random.shuffle(friends_names_list)              #Brug shuffle() fra random library til at blande alle elementerne
                                                    #i listen friends_names_list
    
    santa_dict=dict(zip(friends_names_list,new_list)) #Brug zip()-funktionen til at kombinere to lister (friends_names_list og new_list) 
                                                      # og type casting det som dictionary datatype

    with open('santa.txt', 'w') as convert_file:    #Skriv nu santa_dict-dictionary indhold i et læsbart format til en tekstfil.
                                                    #Sender nu Python-dictionary til json.dumps()-funktionen, som returnerer en string
     convert_file.write(json.dumps(santa_dict))

    f1=open("santa.txt","r+")                        #Åbn filen santa.txt i read mode
    input=f1.read()
    input=input.replace(':',' er secret santa for ')  #erstatte ":" med "er secret santa for"
    input=input.replace('"',' ')                      #erstatte "" med et tomt mellemrum
    
    input=input.replace(',','\n')                    #erstatte "," med et nyt linjetegn for hver post, der starter i en ny linje
    
    input=input.replace('{',' ')                     #erstatte "{" og "}" med et tomt mellemrum
    input=input.replace('}',' ')

    f2=open("santa.txt","w+")                       #Åbn filen santa.txt i write mode
                                                   
    f2.write(input)                                 #Skrive result i filen
    f1.close()                                      #Lukke filen
    f2.close()
    return

def view_secret_santa_file():
    file1 = open("santa.txt")
    print("Secret Santa anvisning")  
    print(file1.read())
    file1.close() 
    return   
  

# MAIN PROGRAM 
ans='y'
while ans=='y' :

    print ("\n" * 50)
    print("Secret Santa anvisning")
    print("\n")
    print("1.View Master File")
    print("2.Anvisning Secret Santa")
    print("3.View Secret Santa file for denne år")
    print("\n")
    choice=int(input("Enter choice: "))

    if (choice==1):
        master_file_view()     
    elif(choice==2):
        assign_secret_santa()
        print("Ho..Ho..Ho..Søg nu efter santa.txt-filen på din computer, og åbn for at se årets secret santa!") 
    elif(choice==3):
        view_secret_santa_file()
    print("\n")
    ans=input("Vil du fortsætte?(Tryk Y eller N) ")
    ans=ans.lower()