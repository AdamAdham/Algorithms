class Solution:
    def minTimeToType(self, word: str) -> int:
        alphabet = {chr(97 + i): i for i in range(26)}
        index = 0
        count = 0
        for i in word:
            nextIndex = alphabet[i]
            route1 = (25-max(nextIndex,index)) + min(nextIndex,index) + 1 # Going counter clockwise
            # So if going from 20 to 3 we go 20->21->22->23->24->25->0->1->2->3 which is 9
            # == (25-20) + 3 + 1 
            # Why plus 1? because of the zero index
            
            route2 = abs(nextIndex-index) # Normal clockwise route
            # 3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18->19->20 which is 17
            # == |3-20| or |20-3|
            index = nextIndex
            
            count += min(route1,route2) + 1 # +1 due to typing the character the pointer is currently on
        
        return count 
            
