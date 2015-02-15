#
#	Students	: Philip Bouman , Alex Khawalid
#	Studentnr	: 10668667		, 10634207
#	Assignment A: step 2 NTMI
#	Date		: 06-02-2015
#
import re
from optparse import OptionParser


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

# print sum of all frequencies for a number n
#def printsum(ngramtable):
#	print "The sum of all frequencies is %i times" % (sum(ngramtable.values()))
#	return sum(ngramtable.values())

def checkProbability(ngram,ngramtable):
	nofngrams = sum(ngramtable.values())
	if ngram in ngramtable:
		pofngram = float(ngramtable[ngram]) / float(nofngrams)
		print "The probability of the ngram '%s' occuring is %f" % (ngram,pofngram)
		return pofngram
	else:
		print "The probability of the ngram '%s' occuring is %f" % (ngram,0.0)
		return 0.0


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
	orderofn = int(options.nth)
else:
	orderofn = 2
if options.pfilename:
	pfile = pfilename
if options.sfilename:
	sfile = sfilename

# the number of results returned for most frequent ngrams
m = 10

###################################################

# parse file and close
ngramtable = getngrams(file_name,orderofn)
ngramtable2 = getngrams(file_name,orderofn-1)

printhigh(ngramtable,m,orderofn)
printhigh(ngramtable2,m,orderofn-1)

# check probability of ngram
ngram = 'Taylor been'
pofn = checkProbability(ngram,ngramtable)


# end