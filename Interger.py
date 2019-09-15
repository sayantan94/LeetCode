class Integer(object):
	def Process(self, val):
		rev = 0
		fact = True if val < 0 else False
		#print (fact)
		val = abs(val)
		while  ( int(val) > 0):
			lastDigit = val % 10
			if rev>0 or lastDigit !=0:
				rev = rev*10 + lastDigit
#
			print (val)
			print (lastDigit)
			print (rev)
			val = int(val/10)
			print ('8888888888888888888888')
		if fact:
			rev = rev * (-1)
		print (int(rev))

if __name__ == '__main__':
	obj = Integer()
	obj.Process(-901000)