class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
            
        return False
        
#         count = 0
#         for i in range(len(arr)):
#             if i/2!=0:
#                 count+=1
#                 if count ==3:
#                     return True
#             else:
#                 count = 0
#                 return False
        
