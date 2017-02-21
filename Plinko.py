import sys
import random

disks = random.randint(1, 5)

print("Congratulations you have", disks, "disks to play with.")

totalPrice = 0

for disk in range(1, disks + 1):
	sys.stdout.write("Dropping disk ")
	sys.stdout.write(str(disk))
	sys.stdout.write("...\n")

	initialPosition =  random.randint(-5, 5)

	movingDisk = initialPosition


	for x in range(5):
		outcome = random.randint(1,100)
		if outcome < 50:
			if movingDisk != -5:
				movingDisk -= 1
			print("-tick-", movingDisk)

		else:
			if movingDisk != 5:
				movingDisk += 1
			print("-tock-", movingDisk)
			pass

	finalOutcome = movingDisk

	if finalOutcome == -5:
		price = "$0"
		totalPrice += 0
		print("The disk landed in", price, "aww, too bad!")
	elif finalOutcome == -4:
		price = "$100"
		totalPrice += 100
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == -3:
		price = "$500"
		totalPrice += 500
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == -2:
		price = "$1000"
		totalPrice += 1000
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == -1:
		price = "$0"
		totalPrice += 0
		print("The disk landed in", price, "aww, too bad!")
	elif finalOutcome == 0:
		price = "$10000"
		totalPrice += 10000
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == 1:
		price = "$0"
		totalPrice += 0
		print("The disk landed in", price, "aww, too bad!")
	elif finalOutcome == 2:
		price = "$1000"
		totalPrice += 1000
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == 3:
		price = "$500"
		totalPrice += 500
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == 4:
		totalPrice += 100
		price = "$100"
		totalPrice += 0
		print("The disk landed in", price, "congratulations!")
	elif finalOutcome == 5:
		price = "$0"
		print("The disk landed in", price, "aww, too bad!")

totalPrice = "$" + str(totalPrice) + "!";
print("\nYour total price winning today is", totalPrice);