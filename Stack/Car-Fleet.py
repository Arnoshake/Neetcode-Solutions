from typing import List
#Zachary West 07/18/25
#First Solution Attempt Time: 12 mins -- Used Hints, feel happy about this one!
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = {}
        for index,value in enumerate(position): # connect car  to its speed
            car_speed[value] = speed[index]
        position.sort(reverse=True)
        #7,4,1,0
        #1,2,2,1
        time = {}

        stack = []
        for index,value in enumerate(position):
            time_to_end = (target - value) / car_speed[value]
            if not stack:
                stack.append(time_to_end)
                continue
            if(time_to_end <= stack[-1]): #while cars make it to end faster than the most recent caravan
                continue
            else:
                stack.append(time_to_end)
        return len(stack) 


            

