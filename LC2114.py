class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        out = 0
        for i in range(len(sentences)):
               if len(sentences[i].split()) > out:
                      out = len(sentences[i].split())
        
        return(out) 
        
