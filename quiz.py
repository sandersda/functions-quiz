	
# TODO - write has_teen
def has_teen(a,b,c):
	if 13 <= a and a <= 19 or 13 <= b and b <= 19 or 13 <= c and c <= 19:
		return True
	else:
		return False

print "Has Teen\n"
print has_teen(1,14,6) # Expect true
print has_teen(17,9,4) # Expect true
print has_teen(7,9,14) # Expect true
print has_teen(7,9,1) # Expect false
# TODO - write not_string
def not_string(str):
	if str.startswith("not"):
		return str + " not"
	else:
		return "not " + str

print "\nNot String\n"
print not_string("not David") 
print not_string("John")
print not_string("not a game")
print not_string("not")
# TODO - write icy_hot
def icy_hot(temp1,temp2):
	if temp1 < 0 and temp2 > 100 or temp2 < 0 and temp1 > 100:
		return True
	else:
		return False

print '\n Icy Hot \n'
print icy_hot(0,100) #expects False 
print icy_hot(-1,101) #expects True 
print icy_hot(1100,1000) #expects False 
print icy_hot(101,-2) #expects True
print icy_hot(-101,-2) #expects False
# TODO - write closer_to
def closer_to(int,n1,n2):
	g1 = abs(int - n1)
	g2 = abs(int - n2)
	if g1 > g2:
		return n2
	elif g2 > g1:
		return n1
	else:
		return 0
print "\n Closer To\n"
print closer_to(10,4,6) # Expects 6
print closer_to(60,57,64) # Expects 57
print closer_to(25,19,18) # Expects 19
print closer_to(10,6,6) # Expects 0
# TODO - write two_as_one
def two_as_one(a,b,c):
	ab = a + b
	ac = a + c
	bc = b + c
	if ac == b or ab == c or bc == a:
		return True
	else: 
		return False

print "\nTwo As One\n"
print two_as_one(7,7,14) # Expects True
print two_as_one(13,7,6) # Expects True
print two_as_one(36,60,24) # Expects True
print two_as_one(7,7,13) # Expects False
print two_as_one(13,7,7) # Expects False
print two_as_one(7,13,7) # Expects False
# TODO - write pig_latinify
def pig_latinify(str):
	str1 = str.lstrip()
	str2 = str1.rstrip()
	str3 = str2.lower()

	if str3.startswith("a" or "o" or "i" or "e" or "u"):
		return str3 + "way"
	else:
		return str3 + "ay"

print "\nPig Latinify\n"
print pig_latinify("                         appLe    ")
print pig_latinify("peter")
