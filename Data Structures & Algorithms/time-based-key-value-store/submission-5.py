class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap.setdefault(key, []).append([timestamp, value])

        
    def get(self, key: str, timestamp: int) -> str:

        # edge case
        if key not in self.TimeMap:
            return ""

        result = ""

        N = len(self.TimeMap[key])
        k = self.TimeMap[key]

        low = 0
        high = N - 1

        while low <= high:
            mid = low + (high-low)//2

            if k[mid][0] <= timestamp:
                result = k[mid][1]
                low = mid + 1
            else:
                high = mid - 1


        return result
            
            
        # for time, value in self.TimeMap[key]:
        #     if time <= timestamp:
        #         result = value
        #     else:
        #         break
        
        # return result
        
