'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
#Solution-->
l1=[]
        if(len(nums1)>len(nums2)):
            for i in range(len(nums1)):
                if(nums1[i] in nums2):
                    l1.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if(nums2[i] in nums1):
                    l1.append(nums2[i])
        return(set(l1))
        
        
 #Solution-->
 # nums1=set(nums1)
 # nums2=set(nums2)
 # a=nums1.intersection(nums2)
 # return(a)
        
