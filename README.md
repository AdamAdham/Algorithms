# Algorithms

# Leet Code

# Dynamic Programming (DP)

## Easy

## [**Climbing Stairs**](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/Climb%20Stairs)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## [Pascal's Triangle](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/Pascal's%20Triangle.py)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:<br>
![image](https://github.com/user-attachments/assets/d6ebb2a9-f321-4920-97a3-575eed5d94cd)

## [119. Pascal's Triangle II](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/119.%20Pascal's%20Triangle%20II.py)

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: <br>
![image](https://github.com/user-attachments/assets/375e718b-11e0-4382-bfe1-410fe110c81b)

## [338. Counting Bits](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/338.%20Counting%20Bits.py)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## [392. Is Subsequence](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/392.%20Is%20Subsequence.py)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## [509. Fibonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/509.%20Fibonacci%20Number.py)

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

## [746. Min Cost Climbing Stairs](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/746.%20Min%20Cost%20Climbing%20Stairs.py)

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

## [1025. Divisor Game](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1025.%20Divisor%20Game.py)

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

## [2900. Longest Unequal Adjacent Groups Subsequence I](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/2900.%20Longest%20Unequal%20Adjacent%20Groups%20Subsequence.py)

You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

## [1137. N-th Tribonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1137.%20N-th%20Tribonacci%20Number.py)

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

### Complexity

**Time Complexity** = O(n) <br>
**Space Complexity**= O(1)

## [1668. Maximum Repeating Substring](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1668.%20Maximum%20Repeating%20Substring.py)

Revise this
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

### Complexity

**Time Complexity** = O(nm) n:len(sequence), m: len(word) <br>
**Space Complexity**= O(n)

## Medium

## [2383. Minimum Hours of Training to Win a Competition](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Medium/53.%20Maximum%20Subarray.py)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

### Complexity

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

# Greedy

## Easy

## [1974. Minimum Time to Type Word Using Special Typewriter](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/1974.%20Minimum%20Time%20to%20Type%20Word%20Using%20Special%20Typewriter.py)

There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

<br>

![image](https://github.com/user-attachments/assets/aec2fcf5-9954-4f4a-9e4a-e12a0b9f574b)
<br>

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

### Complexity

**Time Complexity** = O(n) <br>
**Space Complexity**= O(1)

### Adjustments / Optimizations

Do not calculate the counter clockwise way just do 26-clockwise

## [2037. Minimum Number of Moves to Seat Everyone](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2037.%20Minimum%20Number%20of%20Moves%20to%20Seat%20Everyone.py)

There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

### Complexity

**Time Complexity** = O(nlog(n)) (Sort time)<br>
**Space Complexity**= O(1)

## [2259. Remove Digit From Number to Maximize Result](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2259.%20Remove%20Digit%20From%20Number%20to%20Maximize%20Result.py)

You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

### Complexity

**Time Complexity** = O(n^2) (Outer loop=O(n), array slicing=O(n))<br>
**Space Complexity**= O(1)

## [2591. Distribute Money to Maximum Children](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2591.%20Distribute%20Money%20to%20Maximum%20Children.py)

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

### Complexity

**Time Complexity** = O(1)<br>
**Space Complexity**= O(1)

## [2591. Distribute Money to Maximum Children](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/605.%20Can%20Place%20Flowers.py)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

### Complexity

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

## [2383. Minimum Hours of Training to Win a Competition](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2383.%20Minimum%20Hours%20of%20Training%20to%20Win%20a%20Competition.py)

You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.

You are also given two 0-indexed integer arrays energy and experience, both of length n.

You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.

Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].

Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.

Return the minimum number of training hours required to defeat all n opponents.

### Complexity

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

# Non-Leetcode

# Dynamic Programming

## [Longest Common Subsequence](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Non-Leetcode/Longest%20Common%20Subsequence.py)

Given two sequences, find the length of the longest common subsequence (LCS) present in it. The LCS is the longest sequence which can be obtained from the first sequence by deleting some items and from the second sequence by deleting other items.

Input: X = 'ABCBDAB', Y = 'BDCABA'
Output: 4
Explanation: The LCS are 'BDAB', 'BCAB', and 'BCBA', having length 4.

### Complexity

**Time Complexity** = O(n^2)<br>
**Space Complexity**= O(n^2)

# Interesting Algorithms

## [Kadan's Algorithm](https://github.com/AdamAdham/Algorithms/blob/main/Kadane's%20Algorithm.py)

Get maximum sum of a subarray
