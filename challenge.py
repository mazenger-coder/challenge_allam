import pandas as pd
import xlrd

try:
	# open excel file
	site_capacity = pd.read_excel('Site_Capacity.xlsx', sheet_name='Sheet1')
	# parse user input as strings
	skill_input = input("Please enter the skill: ")
	year = input("Please enter the year: ")
	month = input("Please enter the month: ")
	index = 0
	# calculate the sum of the skills
	sum = 0
	for skill in site_capacity["Skill"]:
		if(skill == skill_input):
			# extract the column with the right date
			entry = site_capacity[pd.to_datetime(year + month, format='%Y%m')][index]
			# prevent that nan is added to the sum
			if(pd.notna(entry)):
				sum += entry
		index += 1
	print("The sum of the skill: " + str(sum))

# exceptions
except FileNotFoundError as file_error:
	print(file_error)
except xlrd.XLRDError as xlrd_error:
	print(xlrd_error)
except ValueError:
	print("Please enter valid input"git )