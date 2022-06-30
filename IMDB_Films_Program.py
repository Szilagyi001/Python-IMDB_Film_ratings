#Practice Assestment
#L.Silaghi
#10/03/21

print ("          Welcome this is a IMDB film ratings program")
print('          ***************Liviu Silaghi***************')


def readFile():
    
    import csv                              #Import csv function

    input("Press Enter to read the files")

    f=open("IMDB films3.csv")               #Opem file in read mode
    csvFile=csv.reader(f)

    Films=[]                                #Create empty arrays
    Ratings=[]

    
    for row in csvFile:                     #Loop through each row in the file
        Films.append(row[0])                #Append films and ratings to the arrays
        
        Ratings.append(float(row[1])) 

    f.close()                               #Close the file

    print("file handling success")
    return Films, Ratings                   #Return films and ratings

    

def displayFile(Films, Ratings):
    input("\nPress Enter to view the files")
    for i in range(len(Films)):             #Loop for each in films
        print(i+1,Films[i],Ratings[i])
    return Ratings[i]


def occurrence(Ratings):
    ratingsAbove =9.0                      #Set the searchvalue to target

    count = 0
    for i in Ratings:                       #Loop through ratings
        if i >= ratingsAbove:               #If bigger value was found add 1 to count
            count=count+1
            

    print("\nThere are",count ,"films that are scored 9.0 above")           #Print the count to display the number of films           
    f=open("IMDB-films-TheResult.txt","w")                                  #Open file in write mode
    input("Press Enter to save the file")                                   
    f.write("There was " +str(count)+" films scored 9.0 and above.")        #Write the count to the file
    print("\nThe file has been written successfully")
    f.close()                                                               #Close the file
    input("Press Enter to exit")
    
    
Films, Ratings=readFile()                   #Main program
displayFile(Films, Ratings)
occurrence(Ratings)

