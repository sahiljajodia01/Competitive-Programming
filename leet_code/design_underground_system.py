# https://leetcode.com/problems/design-underground-system/


######### Got this solution by myself. Process the average time value when the customer is checking out of the station
from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.customer_in = {}
        self.stations = defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_in[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:            
        initial_value = self.stations[self.customer_in[id][0] + "-" + stationName][0]
        initial_count = self.stations[self.customer_in[id][0] + "-" + stationName][1]
            
        self.stations[self.customer_in[id][0] + "-" + stationName][0] = (initial_value * initial_count + (t - self.customer_in[id][1]))/(initial_count+1)
        self.stations[self.customer_in[id][0] + "-" + stationName][1] = initial_count + 1
        
        del self.customer_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans = 0
        for key, value in self.stations.items():
            start, end = key.split('-')
            
            if start == startStation and end == endStation:
                ans = value[0]
                break
                
        return ans
