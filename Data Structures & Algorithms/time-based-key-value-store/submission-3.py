class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        min_num = ""
        if key not in self.table:
            return ""

        for t, v in self.table[key]:
            if t == timestamp:
                return v
            if t <= timestamp:
                min_num = v
        
        return min_num
        
        
