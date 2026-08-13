class TimeMap:

    def __init__(self):
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timeMap:
            self.timeMap[key] = [[timestamp, value]]
        else:
            self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""

        arr = self.timeMap[key]
        low = 0
        high = len(arr) - 1
        ans = ""

        while low <= high:
            mid = low + (high - low)//2

            if arr[mid][0] == timestamp:
                return arr[mid][1]

            elif arr[mid][0] < timestamp:
                ans = arr[mid][1]
                low = mid + 1

            else:
                high = mid - 1

        return ans


        
