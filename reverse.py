import os, sys

class Reverse(object):
	def reverse(self, text):
		print(text[::-1])


if __name__ == '__main__':
	print("Running as a script...")
	givenString = input("Enter the string you wish to reverse:\n")
	#time.sleep(0.5)
	rv = Reverse()
	rv.reverse(givenString)