#!/usr/bin/env python3
import sys

#initialize dictionary:
fav_dict = {}

#add entries to dictionary:
fav_dict['book'] = 'To Kill A Mockingbird'
fav_dict['tree'] = 'maple'
fav_dict['juice'] = 'red grapefruit'
fav_dict['dog'] = 'Pinkerton'
fav_dict['cats'] = 'black'
fav_dict['organism'] = 'howler'

#print full dictionary
print(fav_dict)

#print entry for favorite book:
print(fav_dict['book'])

#allow entry of fav_thing from command line:
#fav_thing = sys.argv[1]

#print all keys for user to choose item:
for key in fav_dict:
	print(key)

#prompt user to input item:
fav_thing = input("Enter your item: ")

print(fav_dict[fav_thing])

print(fav_dict['organism'])
#change entry for favorite organism:
fav_dict['organism'] = 'capuchin'

print(fav_dict['organism'])

fav_category = input("What fav category do you want to add? ")

fav_item = input("Enter your favorite item: ")

#add new key and value from user input:
fav_dict[fav_category] = fav_item

for fav in fav_dict:
	item = fav_dict[fav]
	print(fav,item)

#fav_thing2 = 'tree'

#print(fav_dict[fav_thing2])

#fav_dict['organism'] = 'howler'

#fav_thing3 = 'organism'

#print(fav_dict[fav_thing])
