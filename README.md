# Readme for the Site_Capacity.py

The goal of this Python script is to write a function that reads certain values from an Excel file and calculates the sum. The script expects 3 inputs from the user. On the one hand the skill on the other hand the year and month. In this script the user is asked to enter the desired skill at the beginning. Then the desired year and then the month. The desired data is then read and the sum is calculated. 

By means of an example the functionality of the script shall be shown.

At the beginning the user is asked to enter the desired skill: 
	
	Please enter the skill:

Then the user has to make an entry and press enter 
	 
	User : DD

After this has been done, the user is asked again to make an entry but this time the desired year:
	
	Please enter the year:

Then the user has to make an entry and press enter. This time the input must not be a string, it can only be an integer.
	
	User : 2020

And one last time the user is asked to make an entry:
	
	Please enter the month:

Then the user has to make an entry and press enter.
	
	User: 12

After all three entries have been made, the total is calculated and returned.

	The sum of the skill: 2.3

##Error messages

If lower case letters are entered instead of upper case letters, the letters are automatically converted to upper case and the user does not have to take care of it actively. 

If values are entered for the month that are not between 1 and 12, an error message is displayed and the user is prompted to repeat his entry. The same applies to the years. If no valid year number is entered, an error message is displayed.

