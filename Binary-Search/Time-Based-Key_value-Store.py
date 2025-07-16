# Zachary West 07/15/2025
# First Solution Attempt Time: 33 mins

# The main concept here is the return exists outside of the search in order to find the most relevant result instead of an exact
    # basically math.floor() the search param
class TimeMap:

    def __init__(self):
        self.my_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = []
        self.my_dict[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict: return ""
        val = self.my_dict[key]
        l = 0,
        r = len(val) - 1
        solution = ""
        while (l <= r):
            m = l + (r-l)//2
            if val[m][1] <= timestamp:
                solution = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return solution

        
