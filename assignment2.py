#
#	Students	: Philip Bouman , Alex Khawalid
#	Studentnr	: 10668667		, 10634207
#	Assignment A: step 2 NTMI
#	Date		: 06-02-2015
#
# Command-line:
# (1): python assignment2.py -c austen.txt -n 3
# (2): python assignment2.py -c austen.txt -p test.txt
# (3): python assignment2.py -c austen.txt -n 3 -s test.txt
# (4): python assignment2.py -c austen.txt -n 3 -sp
import re
import itertools
from optparse import OptionParser
from decimal import Decimal

# if n = 1
def getunigrams(f,n):
	ngramtable = {}
	with open(f, 'r') as f:
		for line in f:
			for words in line.split():
				if words in ngramtable:
					ngramtable[words] += 1
				else:
					ngramtable[words] = 1

	return ngramtable

# reads lines from file and splits into words
def getmultigramsgrams(f,n):
	# expression used to split words
	ngramtable = {}
	ngramkey = ""
	i = 0
	linenumber = 1

	# read all lines into words
	with open(f, 'r') as f:
		for line in f:
			j=0
			splitlines = line.split()
			for words in splitlines:
				# Add start if first line
				if j == 0:
					if i == 0:
						ngramkey = "START"
						i += 1
					else:
						ngramkey = ngramkey + " START"
						#print ngramkey
						if ngramkey in ngramtable:
							ngramtable[ngramkey] += 1
						else:
							ngramtable[ngramkey] = 1
						ngramkey = ngramkey.split(' ', 1)[1] 


				# if ngram has less than n words
				if i < n:
					if i == 0:
						ngramkey = words
					else:
						ngramkey = ngramkey + " " + words
					i += 1
					#print "\n ngramkey = %s \n linenumber = %i \n j = %i" % (ngramkey,linenumber,j)
				if i == n:
					# increment occurences of ngram
					if ngramkey in ngramtable:
						ngramtable[ngramkey] += 1
						i = n-1
						ngramkey = ngramkey.split(' ', 1)[1]
					# if new ngram add to table
					else:
						ngramtable[ngramkey] = 1
						i = n-1
						ngramkey = ngramkey.split(' ', 1)[1]
				if j == len(splitlines)-1:
					ngramkey = ngramkey + " " + "END" 
					#print ngramkey
					if ngramkey in ngramtable:
						ngramtable[ngramkey] += 1
					else:
						ngramtable[ngramkey] = 1
					ngramkey = ngramkey.split(' ', 1)[1]
				j += 1
			linenumber += 1
	return ngramtable

# get ngrams
def getngrams(f,n):
	if n > 1:
		ngramtable = getmultigramsgrams(f,n)
	else:
		ngramtable = getunigrams(f,n)
	return ngramtable

# print highest frequency ngrams and their counts
def printhigh(ngramtable,m,n):
	print "\n      Most frequent ngrams with n = %i\n" % (n)
	# sort ngrams
	top =  sorted(ngramtable.iteritems(), key=lambda (k,v):(v,k), reverse=True)
	
	# get the top m results from the sorted ngrams
	i = 0
	ngram = {}
	while i < m:
		print top[i] 
		print "\n"
		i += 1

# calculate probability of ngram
def calcProbability(ngramtable, ngrams,comments):
	nofngrams = sum(ngramtable.values())
	pofngrams = {}
	for line in ngrams:
		if len(line.split()) != orderofn:
			print "The ngram '%s' is not the right length" % (line)
		else:
			if line in ngramtable:
				pofngram = float(ngramtable[line]) / float(nofngrams)
				if comments:
					print "The probability of the ngram '%s' occuring is %.20f" % (line,pofngram)
				pofngrams[line] = pofngram
			else:
				if comments:
					print "The probability of the ngram '%s' occuring is %f" % (line,0.0)
				pofngrams[line] = 0.0
	return pofngrams

# calculate probability of ngrams in a file
def readProbability(ngramtable, pfile):
	ngrams = []

	with open(pfile,'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.replace('\n', '').split(' ')
			line = ' '.join(line)
			ngrams.append(line)
	pofngrams = calcProbability(ngramtable,ngrams,True)
	
	return pofngrams

# calculate probability of sentence
def checksentence(ngramtable, sfile,n):
	ngrams = []
	pofsentence = {}

	with open(sfile,'r') as f:
		lines = f.readlines()
		# for every sentence (line)
		for line in lines:
			i = 0
			probtemp = 1
			ngramkey = ""

			# clean up and split into words
			linesplit = line.replace('\n', '').split(' ')
			for word in linesplit:
				# create all ngrams
				if i == 0:
					ngramkey = word
					i += 1
				elif i < n:
					ngramkey = ngramkey + " " + word
					i += 1
				elif i == n:
					ngrams.append(ngramkey)
					ngramkey = ngramkey + " " + word
					ngramkey = ngramkey.split(' ', 1)[1]

			ngrams.append(ngramkey)

			# calculate probability of ngrams
			temp = calcProbability(ngramtable,ngrams, True)

			# if not empty calculate chance by product of prob
			if temp:
				for item in temp.values():
					probtemp = probtemp * item

				if probtemp == 1:
					probtemp = 0
			else:
				probtemp = 0

			pofsentence[line] = probtemp

	return pofsentence




# create all permutations of a given set
def permutations(set):
	a = ["know", "I", "opinion" "do", "be", "your", "not", "may", "what"]
	b = ["I", "do", "not", "know"]

	set = b 	# set set to b (testing)
	length = len(set)
	perms = []

	while length > 0:

		perm = list(itertools.permutations(set, length))
		perms.append(perm)
		length -= 1

	return perms


##################
#    main code   #
##################

############### parse command line ################

parser = OptionParser()
parser.add_option("-c", "--corpus", dest="file_in")
parser.add_option("-n", dest="nth")
parser.add_option("-p", "--conditionalprobfile", dest="pfilename")
parser.add_option("-s", "--sequenceprobfile" , dest="sfilename")
parser.add_option("-sp", "--scoredpermutations", dest="")
(options,args) = parser.parse_args()

# parameters manual editing
file_name = options.file_in
if options.nth:
	orderofn = int(options.nth)
else:
	orderofn = 2

# the number of results returned for most frequent ngrams
m = 10

###################################################

### 1. 
# parse file and close
ngramtable = getngrams(file_name,orderofn)
#ngramtable2 = getngrams(file_name,orderofn-1)

#printhigh(ngramtable,m,orderofn)
#printhigh(ngramtable2,m,orderofn-1)

### 2.
if options.pfilename:
	# check probability of ngram
	pofn = readProbability(ngramtable,options.pfilename)

### 3.
if options.sfilename:
	pofs = checksentence(ngramtable,options.sfilename,orderofn)
	print pofs

### 4.



# end