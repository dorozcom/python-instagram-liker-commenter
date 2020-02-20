"""
This script is intenteded for someone who is
looking to promote their Instagram activity automatically
through likes and comments.
To use it, go to instagram.com, enter a publication (not from the feed)
but from the search and run the script.

In order to use this code, the x/y coordinates have to be set
according to your monitor's resolution.
To do this, you can use the minilog.py or logger.py scripts on this directory

Make sure that you know Instagram's rules before using it. 

"""

import time
import keyboard
from pynput.mouse import Button, Controller
mouse = Controller()


""" Basic Actions """
def like_publication():
	mouse.position = (581, 389)
	wait(2)
	mouse.click(Button.left,2)
	
def click_next():
	mouse.position = (1127, 395)
	wait(1)
	mouse.click(Button.left,1)
	
def wait(seconds):
	time.sleep(seconds)

def click_search():
	mouse.position = (630, 130)
	mouse.click(Button.left,1)
	wait(1)
	
def choose_first_hashtag():
	mouse.position = (638, 210)
	wait(2)
	mouse.click(Button.left,1)
	
def type_hashtag(hashtag):
	mouse.click(Button.left,1)
	keyboard.write("#" + str(hashtag))
	wait(2)
	
def type_comment(comment):
	mouse.click(Button.left,1)
	keyboard.write(str(comment))
	wait(2)
	
def click_out_publication():
	mouse.position = (1157, 177)
	
def select_first_publication():
	mouse.position = (368, 573)
	wait(5)
	mouse.click(Button.left,1)


""" High Level Actions """
def like_twelve_publications():
	for i in range(0,12):
		like_publication()
		click_next()
		wait(1)

def search_new_hashtag(hashtag):
	#Requires to be in a publication already
	click_out_publication()
	wait(1)
	click_search()
	wait(1)
	type_hashtag(hashtag) #provide it	
	choose_first_hashtag()
	wait(2)
	


print("Script will begin, you have 5 Seconds to redirect to Instagram")
time.sleep(5)

"""
Hashtags.txt includes 100 of the most popular hashtags online
"""
with open('hashtags.txt') as f:
    content = f.readlines()
hashtags = [x.strip() for x in content]


wait(10)

for i in hashtags:
	wait(2)#I would recommend to add higher delays
	like_twelve_publications()
	search_new_hashtag(i)
	wait(5)
	mouse.scroll(0,-1200) #scroll to most recent
	wait(2)
	select_first_publication()
	
like_twelve_publications() #has to be in a publication already
search_new_hashtag()
wait(5)
mouse.scroll(0,-1200) #scroll to most recent
wait(2)
select_first_publication()
like_twelve_publications()


	
"""
#Simple commenting demo
#Requires tune-up

#in a publication (to comment)
mouse.scroll(0,-300)
wait(2)
mouse.position = (771, 615) #to commment
wait(1)
mouse.click(Button.left,1)
mouse.click(Button.left,1)
wait(1)
type_comment('Great work, love it!')
wait(2)
mouse.position = (993, 611) #publish
mouse.click(Button.left,1)

"""
