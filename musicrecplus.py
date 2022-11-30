'''
Created on _11/18/22_
@authors:   __Aleksey Vinogradov, Gavin Lam, Dylan Espiritu, Ayan Mahmood__
Pledge:    _We pledge our honor that we have abided by the Stevens Honor System_

CS115 - Music Recommender Project
'''

dic = {}
newlist = {}
#Idk what this main function is doing ngl, so I tried to make a simpler one at the bottom
def main():
    try:
      artistList = []
      with open ("musicrecplus.txt", "r") as myfile:
          for line in myfile:
              barrier = list(line.strip().split(":"))
              temp = barrier[0]
              artistList = tuple((barrier[1]).split(","))
              dic[temp] = artistList
              
          name =(input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n"))
          if name == "":
            print("Please enter a name with at least 1 symbol.")
            main()
          else:
              if not name in dic:
                  preferences(name) 

    except OSError:
        name =(input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n"))

        if name == "":
            print("Please enter a name with at least 1 symbol.")
            main()
        else:
            preferences(name)

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
         stored in the file 'fileName'.
         Returns a dictionary containing a mapping
         of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
         # Read and parse a single line
         [userName, bands] = line.strip().split(":")
         bandList = bands.split(",")
         bandList.sort()
         userDict[userName] = bandList
    file.close()
    return userDict

def drop(list1, list2):
    ''' Returns a new list that contains only the elements in
    list2 that were not in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3
        
def menu(name):
    while True:
        option = input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit \n")
        if option == "e":
            preferences(name)
        elif option == "r":
            recommendations(name)
        elif option == "p":
            popular_artists()
        elif option == "h":
            most_popular()
        elif option == "m":
            most_likes()
        elif option == "q":
            quitnsave()
            break
        else:
            continue


def preferences(name):
    preferenceList = []
    artists = input("Enter an artist that you like (Enter to finish): \n")
    while artists != "":
        preferenceList += [artists.title()]
        artists = input("Enter an artist that you like (Enter to finish): \n")
        preferenceList.sort()
    dic[name] = tuple(preferenceList)


def recommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations
def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def popular_helper():
    """helper for popular_artist and most_popular functions"""
    artlist = []

    for x in dic.values():
        artlist.append(x)
    print(artlist)
    artlist = list(artlist[0])


    while artlist:
        counter = 0
        templist = []
        for artists in artlist:
            if artlist[0] == artists:
                counter += 1
            else:
                templist += [artists]
        newlist[artlist[0]] = counter
        artlist = templist
    sortedlst = sorted(dict(newlist).items(), key = lambda item: item[1])
    return sortedlst

def popular_artists():
    """f"""
    popular = popular_helper()
    print(popular)
    for name in dic:
        if name[-1] == "$":
                continue
        if (popular == []):
            print ("Sorry, no artists found.")
        else:
            if (len(popular) > 2):
                print(list(popular)[-1][0])
                print(list(popular)[-2][0])
                print(list(popular)[-3][0])
            elif(len(popular) == 2):
                print(list(popular)[-1][0])
                print(list(popular)[-2][0])
            elif(len(popular) == 1):
                print(list(popular)[-1][0])


def most_popular():
    """g"""
    popular = popular_helper()
    for name in dic:
        if name[-1] == "$":
            continue
        if (popular == []):
            print ("Sorry, no artists found.")
        else:
            print (popular[-1][1])

def most_likes():
    """l"""
    lst = []
    most = 0
    for key in dic:
        for name in dic:
            if name[-1] == "$":
                continue
        likes = len(dic[key])
        if likes >= most:
            if likes > most:
                lst.clear()
            lst.append(key)
            mostLikes = likes
    if mostLikes == 0:
        print("Sorry, no user found.")
    else:
        for name in sorted(lst):
            print(name)

def quitnsave():
    with open("musicrecplus.txt", "w") as myfile:
        for name in dic:
            myfile.write(name + ":")
            for artist in dic[name]:
                if artist == dic[name][len(dic[name])-1]:
                    myfile.write(artist)
                else:
                    myfile.write(artist + ",")
            myfile.write("\n")
    exit()
    
# simpler main
def main():
    ''' The main recommendation function '''
    userMap = loadUsers("musicrecplus.txt")
    userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    print ("Welcome,", userName)
    prefs = preferences(userName, userMap)
    recs = recommendations(userName, prefs, userMap)
    # Print the user's recommendations
    menu(userName)
    saveUserPreferences(userName, prefs, userMap, PREF_FILE)
if __name__ == "__main__":
        main()
   
