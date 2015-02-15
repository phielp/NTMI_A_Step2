import itertools

a = ["know", "I", "opinion" "do", "be", "your", "not", "may", "what"]
b = ["I", "do", "not", "know"]

length = len(b)
perms = []

while length > 0:

	perm = list(itertools.permutations(b, length))
	perms.append(perm)
	length -= 1

print perms