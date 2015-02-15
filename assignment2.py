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
	firstword = True
	i = 0

	# read all lines into words
	with open(f, 'r') as f:
		for line in f:
			firstword = True
			j=0
			splitlines = line.split()
			for words in splitlines:
				if firstword:
					if i == 0:
						ngramkey = "START"
					elif i < n:
						ngramkey = ngramkey + " " + "START"
					i += 1
					firstword = False
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
				if j == len(splitlines)-1:
					if i == 0:
						ngramkey = "END"
					elif i < n:
						ngramkey = ngramkey + " " + "END"
					i += 1
				j += 1

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
#def printsum(ngramtable):
#	print "The sum of all frequencies is %i times" % (sum(ngramtable.values()))
#	return sum(ngramtable.values())

def checkProbability(ngram,ngramtable):
	nofngrams = sum(ngramtable.values())
	if ngram in ngramtable:
		pofngram = float(ngramtable[ngram]) / float(nofngrams)
		print "This ngram has a probability of %f" % (pofngram)
		return pofngram
	else:
		print "This ngram has a probability of 0"
		return 0


##################
#    main code   #
##################

############### parse command line ################

parser = OptionParser()
parser.add_option("-c", "--corpus", dest="file_in")
parser.add_option("-n", dest="nth")
parser.add_option("-p", "--conditionalprobfile", dest="pfilename")
parser.add_option("-s", "--sequenceprobfile" , dest="sfilename")
(options,args) = parser.parse_args()

# parameters manual editing
file_name = options.file_in
if options.nth:
	n = int(options.nth)
else:
	n = 2
if options.pfilename:
	pfile = pfilename
if options.sfilename:
	sfile = sfilename

m = 10

###################################################

# parse file and close
ngramtable = readword(file_name,n)
n = n -1

# part 1
printhigh(ngramtable,m)
#####
#print ngramtable
# check probability of ngram
ngram = 'Taylor been'
pofn = checkProbability(ngram,ngramtable)


# end