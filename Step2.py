import re

file_name = "/Users/philipbouman/Documents/AI/NTMI/Assignment01/test.txt"

f = open(file_name, "r")

data = f.read()
paragraphs = []


def addtags(f):

	for paragraph in data:

		v = re.split(r'\n{2,}', data)
		#print paragraph

		paragraphs.extend(v)
		
		# print paragraphs

	paragraphs = filter(None, words)
	#return paragraphs


addtags(f)
print paragraphs



# for paragraph in enumerate(re.split(r'\n{2,}', data)):
