# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Tharathorn (Joy) Rimchala

def rotate_char(c,nc):
	return chr(ord(c)+nc)

def rotate_word(s,ns):
	ss = '';
	for js in range (len(s)):
		ss = ss + rotate_char(s[js],ns)
	return ss

# Test 
def printmsg(s,n):
	print 'rotate_char(' + s[0] + ',' + str(n) + ') = ' + rotate_char(s[0],n) 
	print 'rotate_word(' + s + ',' + str(n) + ') = ' + rotate_word(s,n)

printmsg('cheer',7)
printmsg('melon',-10)