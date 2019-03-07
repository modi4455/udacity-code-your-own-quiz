blanks = ['___1___','___2___','___3___','___4___']
easy_question = "we started the session by learning about two important things ___1___ and ___2___ .we use ___3___ with number and string with ___4___ source: mynote"  
medium_question= "we use ___1___ conditional to control the flow.it helps us know which get executed and when. another way to control flow is ___2___  used to ___3___  task preformed many '___4___' source: mynote"
hard_question= "function  .oppent used to ___1___  element at the ___2___ while len used to measure ___3___ function split work as ___4___ source: mynote"
answer_easy =["variable", "string","intiger","words"]
answer_medium= ["if", "while", "loop","time"]
answer_hard = ["add", "end", "length", "separator" ]
## all of my function to this code 
def greet():
	#To display initial player
	#input = name of the player
	#output = game greeting and player name
	#here is my function
	print"welcome to my quiz"
	user_name =raw_input("what is your name ")
	name = "hello "+ user_name
	print name 	
def level_choose(game_level):
	#To group all the paragraphs and answers together
	# input ueser current level 
	# output is the question and answer of chosen level 
	# the return is question and answer of specific level
	#here is my function 

	if game_level == "easy":		
		return easy_question, answer_easy
	if game_level== "medium":		
		return medium_question ,answer_medium
	if game_level== "hard":		
		return hard_question	,answer_hard
def word_in_blanks(word, blanks):
	#to find out every blank in question 
	#input is words for each blank and blank in the list  
	#output find the blanks and return word if that match with the current word
	#this is my finction
	for blank in blanks:
		if blank in word:
			return blank
	return None
def replace_blanks(word,replaced, blanks,user_answer,index):
	#to replace each blank with it's correct answer . part 2
	#input is  blanks list , the repleced paragraph that has correct answer 
	#the user answer for blank and the index number of that user answer to correctly match the right blank to fill
	 #output correctly repleced pragraph
	if word_in_blanks(word,blanks) == None: 
		if word not in replaced:
			replaced.append(word)
	else:
		replacement = word_in_blanks(word ,blanks)
		word = word.replace(replacement, user_answer.upper())
		if replacement== blanks[index]:
			if replacement not in replaced:
				replaced.append(word)
			else:
			  pos= replaced.index(replacement)
			  replaced[pos]= word    	   	
		else:
			replaced.append(replacement)		
	return replaced
def fill_blanks(paragraph, blanks, replaced, user_answer,index):
	#to replace each blank with it's correct answer . part 1
	#input is  blanks list , the repleced paragraph that has correct answer 
	#the user answer for blank and the index number of that user answer to correctly match the right blank to fill
	 #output correctly repleced pragraph
	 #this is my function 
	split_pragraph =paragraph.split() 
	if type(replaced)==str:
		replaced =replaced.split() 
	for word in split_pragraph:
		replace_blanks(word,replaced,blanks,user_answer ,index)
	replaced = " ".join(replaced)
	head ,separator,tail= replaced.partition("mynote") #i use this to remove the blanks at the end of each question
	replaced =head+separator
	return replaced
def correct_answer(level , paragraph,answer):
	#to collect the user answer
	#input current level ,it's pragraph and it's answer
	# output updated replaced , index for each answer\
	#this is my function  
	replaced= []
	user_answer= " "
	index =0
	score= 1
	for blank in blanks:
		user_answer= raw_input("what is your answer for" +blank +"?" "write it here: ")
		user_answer= user_answer.lower()   
		while user_answer!=answer[index]:			
			user_answer= raw_input("wrong ,try again:   ")
			user_answer= user_answer.lower() 
		print "right answer , keep going your score is " + str(int( score))
		print fill_blanks(paragraph, blanks,replaced, user_answer,index) 
		index+=1
		score+=1
	return replaced, index
def game ():
	#to start the game 
	#input = none 
	#the output is the game and move you to another level if you want to keep playing
	#this is my function to acheive that  
	greet()
	game_level=raw_input("Please choose a difficult level: easy, medium or hard:  ")
	game_level= game_level.lower()
	if game_level == "easy" or game_level == "hard" or game_level == "medium":
	    paragraph, answers= level_choose(game_level)
	    print paragraph 
	    replaced = correct_answer(game_level, paragraph, answers)
	    print "YaY, YOU WON !"
	    keep_playing = raw_input("would you like to continue? yes or no:   ")
	    if keep_playing =="yes":
	      print "now, you can choose another level"
	      game()
	    elif keep_playing=="no":
	        print "thank you"
	else:		
		print "WRONG! Please pick an actual level,  Game will now restart."
		game()
game()
