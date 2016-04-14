amountofseconds = input("Give me a number of seconds in the range of 0 to 86,400: ") #asking for a number
hours = amountofseconds / 60 / 60  
minutes = amountofseconds / 60 % 60 
seconds =  amountofseconds % 60 % 60

if 86400 >= amountofseconds >= 3600 : #if amountofseconds is in this range do this. Hours starts at 3600 (60*60) if amount of seconds is divisible by 3600 it will output an hour.
	print "The time is" , hours, "hours," , minutes , "minutes, and" , seconds , "seconds"
if 60 <= amountofseconds < 3600 : #if amount of seconds is within this range it will ignore hours because when you divide by hours you will get 0 and no remainder. This will output the division of the minutes and the remainder for the seconds
	print "The time is" , hours, "hours," , minutes , "minutes, and" , seconds , "seconds"
if 0 <= amountofseconds < 60 : #this is only for seconds and will only output 0 -> 60 seconds it will output 0,0 for minutes and hours because the division is still 0 and will show the remainder of the hours and miniutes
	print "The time is" , hours, "hours," , minutes , "minutes, and" , seconds , "seconds"
