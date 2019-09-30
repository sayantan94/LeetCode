class Solution:
	def maxArea(self, height):
		l = 0
		maxArea = 0
		r = len(height) - 1
		while (r > l):
			maxArea = max(maxArea, (r-l)*min(height[l], height[r]))
			if height[l] > height[r]:
				r = r-1
			else:
				l = l + 1
		return maxArea

if __name__ == '__main__':
	print (Solution().maxArea([1,2,3,4,5,6,4]))