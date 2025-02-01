class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = -1
        startNet = -1
        # -2,-2,-2,3,2,-3,4
        for i in range(len(gas)):
            if(gas[i]-cost[i]>=0 and startNet<0):
                 # If routetill now is currently negative -> then we cannot get use that route so we reset
                start = i
                startNet = 0
            startNet += gas[i]-cost[i] 

        # If best route from 1 pass of the array is <0 then cannot be done (the path to return to start of array is impossiblr)
        # start==-1 means there does not exists gas-cost > 0
        if startNet<0 or start==-1: return -1

        for i in range(len(gas)):
            if(startNet<0): return -1
            if(i==start): return start
            startNet += gas[i]-cost[i] 