#
#	Students	: Philip Bouman , Alex Khawalid
#	Studentnr	: 10668667		, 10634207
#	Assignment A: step 2 NTMI
#	Date		: 06-02-2015
#
# Command-line:
# (1): python assignment2.py -c austen.txt -n 3
# (2): python assignment2.py -c austen.txt -p test2.txt
# (3): python assignment2.py -c austen.txt -n 3 -s test.txt
# (4): python assignment2.py -c austen.txt -n 3 -fo
import itertools
from optparse import OptionParser

# if n = 1
def getunigrams(f,n):
	ngramtable = {}
	with open(f, 'r') as f:
		for line in f:
			if line:
				if ngramtable["START"]:
					ngramtable["START"] += 1;
				else:
					ngramtable["START"] = 1;
				if ngramtable["END"]:
					ngramtable["END"] += 1;
				else:
					ngramtable["END"] = 1;
			for words in line.split():
				if words in ngramtable:
					ngramtable[words] += 1
				else:
					ngramtable[words] = 1

	return ngramtable

# reads lines from file and splits into words
def getmultigrams(f,n):
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
		ngramtable = getmultigrams(f,n)
	else:
		ngramtable = getunigrams(f,n)
	return ngramtable


def getR(ngramtable,ngram):
	nr = ngramtable[ngram]
	nr1 = ngramtable[ngram]+1
	if nr in numberofrs:
		counternr = numberofrs[ngramtable[ngram]]
	else:
		counternr = listofocc.count(nr)
	if nr1 in numberofrs:
		counternr1 = numberofrs[ngramtable[ngram]]
	else:
		counternr1 = listofocc.count(nr1)
	return [counternr,counternr1]

# print highest frequency ngrams and their counts
def printhigh(ngramtable):
	# sort ngrams
	top =  sorted(ngramtable.iteritems(), key=lambda (k,v):(v,k), reverse=True)

	# get the bot m results from the sorted ngrams
	return top

# good turing
def calcProbabilityGT(ngramtable,pofn):
	k = 5
	nofngrams = sum(ngramtable.values())
	counter = -1
	sortngrams = printhigh(ngramtable)
	while sortngrams[counter][1] < k + 1:
		temp = getR(ngramtable,sortngrams[0][0])
		pofn[sortngrams[0][0]] *= float(temp[1])/float(temp[0])
		counter -= 1
		print "%i,%i" % (counter,nofngrams)
	
	return pofn



	
# add 1 smoothing
def calcProbabilityAdd1(ngramtable,comments,n):
	nofngrams = sum(ngramtable.values())
	pofngrams = {}
	for ngram in ngramtable:
		if ngram in ngramtable:
			pofngram = (float(ngramtable[ngram])+1) / float(nofngrams)
			if comments:
				print "The probability of the ngram '%s' occuring is %.20f" % (ngram,pofngram)
			pofngrams[ngram] = pofngram
		else:
			if comments:
				print "The probability of the ngram '%s' occuring is %f" % (ngram,0.0)
			pofngrams[ngram] = 0.0
	return pofngrams


# no smoothing
def calcProbability(ngramtable,comments,n):
	nofngrams = sum(ngramtable.values())
	pofngrams = {}
	for ngram in ngramtable:
		if ngram in ngramtable:
			pofngram = (float(ngramtable[ngram]) / float(nofngrams))
			if comments:
				print "The probability of the ngram '%s' occuring is %.20f" % (ngram,pofngram)
			pofngrams[ngram] = pofngram
		else:
			if comments:
				print "The probability of the ngram '%s' occuring is %f" % (ngram,0.0)
			pofngrams[ngram] = 0.0
	return pofngrams



# calculate probability of ngrams in a file
def readProbability(ngramtable, pfile,orderofn,smoothmethod):
	ngrams = []

	with open(pfile,'r') as f:
		lines = f.readlines()
		for line in lines:
			line = line.replace('\n', '').split(' ')
			line = ' '.join(line)
			ngrams.append(line)
	pofngrams = calcProbability(ngramtable,ngrams,True,orderofn)


	'''if smoothmethod == "no":
		pofngrams = calcProbability(ngramtable,ngrams,True,orderofn)
	elif smoothmethod == "add1":
		pofngrams = calcProbabilityAdd1(ngramtable,ngrams,True,orderofn)
	else:
		pofngrams = calcProbabilityGT(ngramtable,ngrams,True,orderofn)
		'''
	return pofngrams


# create all permutations of a given set
def permutations(set):
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
parser.add_option("-t", "--testcorpus", dest="test_corp")
parser.add_option("-s", "--smoothing" , dest="smoothmethod")

(options,args) = parser.parse_args()

# parameters manual editing
file_name = options.file_in
testcorpus = options.test_corp
if options.nth:
	orderofn = int(options.nth)
else:
	orderofn = 2

###################################################

### 1. 
ngramtable = getngrams(file_name,orderofn)
#ngramtable2 = getngrams(file_name,orderofn-1)
numberofrs = {}
listofocc = ngramtable.values()

### 2.
if options.smoothmethod == "no":
	# check probability of ngram
	#pofn = readProbability(ngramtable,file_name,orderofn,options.smoothmethod)
	pofn = calcProbability(ngramtable,True, 2)
if options.smoothmethod == "add1":
	pofn = calcProbabilityAdd1(ngramtable,True,2)
if options.smoothmethod == "gt":
	pofn = calcProbabilityAdd1(ngramtable,False,2)
	pofn = calcProbabilityGT(ngramtable,pofn)
	print pofn
	#print pofn










# end