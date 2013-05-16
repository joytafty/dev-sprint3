# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Tharathorn (Joy) Rimchala

# Exercise 9.1
def printlong(word):
	plen = 20
	if (len(word) > plen):
		print word

# Exercise 9.1 calls
print "# Exercise 9.1 #"
print "================"
f1 = open('words.txt')
for line in f1:
	word = line.strip()
	printlong(word)

# Exercise 9.2
def has_no_e(word):
	if ("e" not in word):
		print word
		return 1
	else: 
		return 0

# Exercise 9.2 calls
print "# Exercise 9.2 #"
print "================"
f2 = open('words.txt')
n_noe = 0
nw = 0
for line in f2:
	nw = nw+1
	word = line.strip()
	temp = has_no_e(word)
	n_noe = n_noe + temp
f_noe = float(n_noe)/float(nw)
print "Percentage of words with no 'e' :" + str(f_noe)
	
# Exercise 9.3
def avoids(word, c):
	return ("c" not in word)

def avoids2(fin, c):
	for line in fin:
		word = line.strip()		
		if not(set(c).issubset(set(word))):
			print word
# Exercise 9.3 calls
print "# Exercise 9.3.1 #"
print "=================="
p1 = "Please provide a word input to test : "
c1 = raw_input(p1)
p2 = "Please provide a character or string to avoid: "
c2 = raw_input(p2)
b = avoids(c1,c2)
print str(b)

print "# Exercise 9.3.2 #"
print "=================="
f3 = open('words.txt')
p = "Please provide word or string of forbidden letters :"
c = raw_input(p)
avoids2(f3,c)

# Exercise 9.4
def uses_only(word,c):
	return (set(word).issubset(set(c)))

# Exercise 9.4 calls
print "# Exercise 9.4 #"
print "=================="
p4 = "Please provide word to test :"
c4 = raw_input(p4)
p5 = "Please provide word or string of allowed letters :"
c5 = raw_input(p5)
b5 = uses_only(c4,c5)
print str(b5)


