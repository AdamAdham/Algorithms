# Algorithms
# Leet Code

# Dynamic Programming (DP)

## Easy

## [**Climbing Stairs**](https://github.com/AdamAdham/Algorithms/blob/main/Climb%20Stairs)
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


## [Pascal's Triangle](https://github.com/AdamAdham/Algorithms/blob/main/Pascal's%20Triangle.py)
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:<br>
![image](https://github.com/user-attachments/assets/d6ebb2a9-f321-4920-97a3-575eed5d94cd)



## [119. Pascal's Triangle II](https://github.com/AdamAdham/Algorithms/blob/main/119.%20Pascal's%20Triangle%20II.py)
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: <br>
![image](https://github.com/user-attachments/assets/375e718b-11e0-4382-bfe1-410fe110c81b)



## [338. Counting Bits](https://github.com/AdamAdham/Algorithms/blob/main/338.%20Counting%20Bits.py)
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



## [392. Is Subsequence](https://github.com/AdamAdham/Algorithms/blob/main/392.%20Is%20Subsequence.py)
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



## [509. Fibonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/509.%20Fibonacci%20Number.py)
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.



## [746. Min Cost Climbing Stairs](https://github.com/AdamAdham/Algorithms/blob/main/746.%20Min%20Cost%20Climbing%20Stairs.py)
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



## [1025. Divisor Game](https://github.com/AdamAdham/Algorithms/blob/main/1025.%20Divisor%20Game.py)

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.



## [2900. Longest Unequal Adjacent Groups Subsequence I](https://github.com/AdamAdham/Algorithms/blob/main/2900.%20Longest%20Unequal%20Adjacent%20Groups%20Subsequence.py)
You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.



## [1137. N-th Tribonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/1137.%20N-th%20Tribonacci%20Number.py)
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

### Complexity
**Time Complexity** = O(n)  <br>
**Space Complexity**= O(1)



## Interesting Algorithms

### [Kadan's Algorithm](https://github.com/AdamAdham/Algorithms/blob/main/Kadane's%20Algorithm.py)
Get maximum sum of a subarray

