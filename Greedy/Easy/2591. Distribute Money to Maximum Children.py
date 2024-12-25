class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if(money<children):
            return -1
        
        remMoney = money-children # Remaining money after each child has been given 1 dollar (so 2nd constraint is guaranteed)
        
        sevens = remMoney//7 # the remaining money to reach 8 is 7 so we check how many whole 7s is remaining
        rem = remMoney%7 # the remainder when we took the 7s
        if(sevens==children-1 and rem==3):
            # The only way i can think of that a child HAS to get a 4 (extra 3) is when it is the only child left and the remaining money is 3 (because already given the 1 initially)
            # So it just decreases the number of sevens we can use so that the remaining money is distributed to 2 children
            # And returns -1 when there is only 1 child and the money is 4
            sevens-=1
        if(sevens>children or (sevens==children and rem>0)):
            # More 8s than the children so we have to just sacrifice 1 child (lol) to take all the remaining money
            # Or 8s are equal to the children but there is remaining money that is less than 7
            sevens = children-1
        return sevens    
        