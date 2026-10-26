class TimeMap:

    def __init__(self):
        self.dictionary = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = [(value,timestamp)]
        else:
            self.dictionary[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        value = self.dictionary[key]
        if value[0][1] > timestamp:
            return ""
        left = 0 
        right = len(value) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if value[mid][1] <=timestamp:
                left = mid 
            else:
                right = mid - 1
        return value[left][0]

