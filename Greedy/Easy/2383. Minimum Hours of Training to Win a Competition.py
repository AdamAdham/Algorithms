class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        extraEnergy = max(0, sum(energy) - initialEnergy + 1)  # +1 because at least 1 energy is left
        
        currentXp = initialExperience
        extraXp = 0
        for xp in experience:
            if(currentXp<=xp):
                extraXp += xp - currentXp + 1 # Because have to be strictly greater
                currentXp = xp+1
            currentXp += xp

        return extraEnergy + extraXp