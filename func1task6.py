def reversik(s):  
	s1 = s.split(' ') 
	revs =' '.join(reversed(s1)) 
	return revs

s=input()
print(reversik(s)) 
