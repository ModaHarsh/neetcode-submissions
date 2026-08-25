class TimeMap:
    
    def __init__(self):
        self.myDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict.setdefault(key,[(value, timestamp)])
        else:
            self.myDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ## perform binary search on the timestamp
        ## bounds from 1 to len(self.myDict[key])
        ## the timestamps are always sorted because so binary search
        if key not in self.myDict:
            return ""
        else:
            l = 0
            r = len(self.myDict[key]) - 1
            valid = len(self.myDict[key])
            while(l <= r):
                mid = (l + r) // 2
                if self.myDict[key][mid][1] > timestamp :       # timestamp is smaller
                    r = mid - 1
                elif self.myDict[key][mid][1] < timestamp :
                    valid = mid
                    l = mid + 1
                else:
                    return self.myDict[key][mid][0]
            if (valid != len(self.myDict[key])):
                return self.myDict[key][valid][0]
            else:
                return ""

            





    ## will try this problem using python dictionaires
    ## saving keys as keys and values as tuples ig


