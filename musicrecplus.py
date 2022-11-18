'''
Created on _11/18/22_
@authors:   __Aleksey Vinogradov, Gavin Lam, Dylan Espiritu, Ayan Mahmood__
Pledge:    _We pledge our honor that we have abided by the Stevens Honor System_

CS115 - Music Recommender Project
'''

def greeting():
  """
    prompts user for their name and stores it in a userName variable
    Written by Aleksey, Gavin, Dylan, Ayan
  """
  userName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")


def write_file(filename):
  """
    creates an empty txt file 
  """
  myFile = open(filename, "w")
  myFile.close()

def loadPrefs(filename):
  """
    creates a dictionary with keys as username and lists as values, for ex {Joe: [artist, ]}
  """
  dictionary = {}
  with open(filename, "r") as f:
    for line in f:
      [username, artists] = line.strip().split(":")
      artistList = artists.split(",")
      dictionary[username] = artistList
  return dictionary

