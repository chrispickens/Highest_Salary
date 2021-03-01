import csv
#This program determines the highest listed salary in the Lehmans MLB dataset...
def playerFinder(salary):
	file = '/home/chris/Documents/2019 Lehmans Database/baseballdatabank-master/core/Salaries.csv' 

	with open(file) as csv_file:
		players = csv.DictReader(csv_file, delimiter = ',')

		for player in players:
			if int(player['salary']) == int(salary):
				playerName = player['playerID']
				return playerName

def infoFetcher(playerID):
	infoFile = '/home/chris/Documents/2019 Lehmans Database/baseballdatabank-master/core/People.csv'

	with open(infoFile) as csv_file:
		people = csv.DictReader(csv_file, delimiter = ',')

		for row in people:
			if row['playerID'] == playerID:
				print(row)

def main():
	#File Location shortcut
	file = "/home/chris/Documents/2019 Lehmans Database/baseballdatabank-master/core/Salaries.csv"

	with open(file) as csv_file:
		salaries = csv.DictReader(csv_file, delimiter = ',')
		#Define list to hold salaries in order of greatest to lowest
		dollars = []

		for row in salaries:
			#for every line with key 'salary' add the value AS AN INTEGER to the previously defined list
			row['salary'] = int(row['salary'])
			dollars.append(row['salary'])
			highestSalary = max(dollars)
		
	#output the maximum (highest) value of the list
	print(f'The highest salary in the MLB is {highestSalary}')

	#run function for determining which player earned the highest salary.
	highestPaidPlayer = playerFinder(highestSalary)
	print(highestPaidPlayer)

	infoFetcher(highestPaidPlayer)

if __name__=="__main__":
	main()
