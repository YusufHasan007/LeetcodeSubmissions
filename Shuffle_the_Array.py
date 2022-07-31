class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        mid = n

        out =[]
        for i in range(n):
                out.append(nums[i])
                out.append(nums[mid])
    
                mid += 1
    
        return(out)   
