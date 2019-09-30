class Solution:
    def threeSum(self, nums, target):
        # Sort the array
        result = list()
        nums.sort()
        #print (nums)
        target = target
        params = dict()
        closest = target
        params = dict()

        size = len(nums)
        #print (size)
        if (size==3):
            sum =  (nums[0] + nums[1] + nums[2])
            return sum
            params[abs(target - sum)] = sum
        
        for i in range(size - 2):
            l = i+1
            r = size-1
            while ( l < r):
                sum = nums[i] + nums[l] + nums[r]
                #print (i,l,r)
                #print (sum)
                #val = [nums[i], nums[l], nums[r]]
                params[abs(target - sum)] = sum
                #if sum < closest:
                #    closest = abs(target - sum)
                #params[abs(target - sum)] = sum
                    
                    #result.append([nums[i], nums[l], nums[r]])
                    #print (nums[i], nums[l], nums[r])
                
                #l+=1
                #r-=1

                if sum < target:
                    l = l + 1
                if sum > target:
                    r = r - 1
                if sum == target:
                    break
                

        return (params)
        #return params

                
if __name__ == '__main__':
    # Need to return the template
    val = [0,2,1,-3]
    aa = Solution().threeSum(val,1)


    print (aa)
    

#    print (aa)
    #print (len(aa))