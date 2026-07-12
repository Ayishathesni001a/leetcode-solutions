class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(1,rowIndex+1):
            new_raw = [1] *(i+1)
            for j in range(1,i):
                new_raw[j] = row[j-1]+row[j]
            row = new_raw
        return row        

