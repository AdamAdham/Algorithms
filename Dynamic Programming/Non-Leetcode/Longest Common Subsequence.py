class Solution:
	def findLCSLength(self, X: str, Y: str) -> int:
		dp = [[0] * (len(Y)+1) for _ in range(len(X)+1)]
		
		for i in range(1,len(X)+1):
			for j in range(1,len(Y)+1):
				if(X[i-1]==Y[j-1]):
					dp[i][j] = 1 + dp[i-1][j-1]
				else:
					dp[i][j] = max(dp[i][j-1],dp[i-1][j])
		return dp[len(X)][len(Y)]
