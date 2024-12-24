class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)  # Length of the sequence
        m = len(word)      # Length of the word we are checking for repeats
        dp = [0] * (n + 1)  # Array to store the maximum number of repeats up to each index
        maxRepeat = 0  # Variable to store the maximum number of consecutive repeats found

        # Loop over the sequence from index 'm' to 'n'
        for i in range(m, n + 1):
            # Check if the substring of length 'm' ending at index 'i' equals the word
            if sequence[i - m:i] == word:
                # If it matches, update dp[i] to reflect the consecutive repeat count
                dp[i] = dp[i - m] + 1
                # Update maxRepeat if this count is larger than the previous max
                maxRepeat = max(maxRepeat, dp[i])

        return maxRepeat  # Return the maximum number of consecutive repeats found

