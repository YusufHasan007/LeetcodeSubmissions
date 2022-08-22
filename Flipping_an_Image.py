class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        for i in range(len(image)):
             image[i].reverse()
    
    
             for j in range(len(image[i])):
                        if int(image[i][j]) == int(1):
                             image[i][j] = int(0)
                        elif int(image[i][j]) == int(0):
                             image[i][j] = int(1)
        
        return image  
