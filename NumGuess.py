Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> secret = random.randint(1, 99)
>>> guess = 0
>>> tries = 0
>>> print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
AHOY! I'm the Dread Pirate Roberts, and I have a secret!
>>> print "It is a number from 1 to 99. I'll give you 6 tries."
It is a number from 1 to 99. I'll give you 6 tries.
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
		elif guess > secret:
			
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
		elif guess > secret:
			
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

		
What's yer guess? 

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    guess = input("What's yer guess? ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> >>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		
SyntaxError: invalid syntax
>>> >>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"
	tries = tries + 1
if guess == secret:
	
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	
What's yer guess? \

Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    guess = input("What's yer guess? ")
  File "<string>", line 1
    \
    ^
SyntaxError: unexpected character after line continuation character
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"
	tries = tries + 1
if guess = secret:
	
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	
What's yer guess? s

Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    guess = input("What's yer guess? ")
  File "<string>", line 1, in <module>
NameError: name 's' is not defined
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"
tries = tries + 1
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	tries = tries + 1

What's yer guess? 

Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    guess = input("What's yer guess? ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	tries = tries + 1
if guess == secret:
	
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	tries = tries + 1
	
if guess == secret:
	
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	tries = tries + 1
	
if guess == secret:
	
SyntaxError: invalid syntax
>>> while guess != secret and tries < 6 :
	guess = input("What's yer guess? ")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	if guess > secret:
		print "Too high, landlubber!"

	tries = tries + 1
	
        if guess == secret:
		print "Avast! Ye got it! Found my secret, ye did!"
	else:
		print "No more guesses! Better luck next time, matey!"
		print "The secret number was", secret

		
What's yer guess? 5
Too low, ye scurvy dog!
No more guesses! Better luck next time, matey!
The secret number was 70
What's yer guess? 
