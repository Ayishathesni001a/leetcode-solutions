class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        traingle = []
        for i in range(numRows):
            raw = [1] * (i+1)
            for j in range(1,i):
                raw[j] = traingle[i-1][j-1] + traingle[i-1][j]
            traingle.append(raw)
        return traingle        
