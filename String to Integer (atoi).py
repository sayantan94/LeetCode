# Need to convert string to atoi
# use the python isinstance value and check if the value is possible or not
class Solution:
			
		def myAtoi(self, str: str) -> int:
			str = str.strip()
			if not str:
				return 0
			start = 0
			result = 0
			sign = 1
			#print (str)
			# First Character could either be -/+/integer else return zero
			print (str)
			if (str[start] in ['-','+'] and len(str) > 1):
				if not str[start+1].isdigit():
					return 0
				else:
					sign = -1 if str[start]=='-' else 1
					start = start + 1

           
			while (start < len(str) and str[start].isdigit()):
				result = result*10 + int(str[start])
				start = start + 1

			
			result =  result*sign
			#print (result)

			if sign < 0 and result < -2**31:
				result = -2**31
			if sign > 0 and result > 2**31 - 1:
				print (33)
				result = 2**31 -1
			print (2**31)
			return result
# Keep checking the loop until white space is achives --> trim
# Check if the first character is either -/+/ interger -- isinstance(integer) : True
# If we receive any non integer character then we need to stop the value
# Check if the store values is between 2**31 and -2**31, if more then return the values accordinly
#pass


if __name__ == '__main__':
	obj = Solution()
	print (obj.myAtoi("2147483648"))
