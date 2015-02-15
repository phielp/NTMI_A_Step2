#
#	Students	: Philip Bouman , Alex Khawalid
#	Studentnr	: 10668667		, 10634207
#	Assignment A: step 2 NTMI
#	Date		: 06-02-2015
#


import re
from optparse import OptionParser

# reads lines from file and splits into words
def readword(f):
	# expression used to split words
	ngramtable = {}
	ngramkey = ""

	# read all lines into words
	with open(f, 'r') as f:
		i = 0
		'''if line[0] == "\n":
				if paropen:
					ngramkey = word + " " + "-!"
					ngramtable = checkgram(ngramkey,ngramtable)
					paropen = False
				lastn = True
			elif line[0] != "\n":
				if lastn and not paropen:
					ngramkey = "!-"
					i += 1
					paropen = True

				lastn = False'''
		for line in f:
			for words in line.split():
				# if ngramkey smaller than n
				if i < n:
					if i == 0:
						ngramkey = words
					else:
						ngramkey = ngramkey + " " + words
					i += 1
				else:
					# increment occurences of ngram
					if ngramkey in ngramtable:
						ngramtable[ngramkey] += 1
						i = 0
						ngramkey = ""
					# if new ngram add to table
					else:
						ngramtable[ngramkey] = 1
						i = 0
						ngramkey = ""

	return ngramtable

# print highest frequency ngrams and their counts
def printhigh(ngramtable,m):
	# sort ngrams
	top =  sorted(ngramtable.iteritems(), key=lambda (k,v):(v,k), reverse=True)
	
	# get the top m results from the sorted ngrams
	i = 0
	ngram = {}
	while i < m:
		print top[i] 
		print "\n"
		i += 1

# print sum of all frequencies for a number n
def printsum(ngramtable):
	print "The sum of all frequencies is %i times" % (sum(ngramtable.values()))
	return sum(ngramtable.values())


##################
#    main code   #
##################


# read cmdline options
parser = OptionParser()
parser.add_option("-c", "--corpus", dest="file_in")
parser.add_option("-n", dest="nth")
# parser.add_option("-f", dest="nth")

#parser.add_option("-m", dest="mth")

(options,args) = parser.parse_args()

# parameters manual editing
file_name = options.file_in
n = int(options.nth)
m = 10#int(options.mth)

##################################################

# parse file and close
ngramtable = readword(file_name)

# depending on number n, ngrams need to be offset
# should work with n-1 instead conditional offset
# but it did not

if n == 1:
	offset = 0;
elif n == 2:
	offset = 1;
else:
	offset = 2;



# j is used to make ngrams
# i is used to iterate through words
i = 0
# part 1
printhigh(ngramtable,m)
# check probability of ngram
ngram = 'has been'
nofngrams = printsum(ngramtable)
pofngram = float(ngramtable[ngram]) / float(nofngrams)
print pofngram

# end