# Algorithms

# Leet Code

# Dynamic Programming (DP)

## Intuition Behind Solving

1. Get base case (edge cases like current=0, current=1, current=n etc)
2. Assume that f[current-1] is solved (sometimes all of f[0:current] current exclusive (like longest increasing subsequence))
3. Then what to do with f[current-1] to formulate the f[current]

Same intuition of prove by induction

## Easy

### [**Climbing Stairs**](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/Climb%20Stairs.py)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### [Pascal's Triangle](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/Pascal's%20Triangle.py)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:<br>
![image](https://github.com/user-attachments/assets/d6ebb2a9-f321-4920-97a3-575eed5d94cd)

### [119. Pascal's Triangle II](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/119.%20Pascal's%20Triangle%20II.py)

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: <br>
![image](https://github.com/user-attachments/assets/375e718b-11e0-4382-bfe1-410fe110c81b)

### [338. Counting Bits](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/338.%20Counting%20Bits.py)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

### [392. Is Subsequence](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/392.%20Is%20Subsequence.py)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

### [509. Fibonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/509.%20Fibonacci%20Number.py)

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

### [746. Min Cost Climbing Stairs](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/746.%20Min%20Cost%20Climbing%20Stairs.py)

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

### [1025. Divisor Game](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1025.%20Divisor%20Game.py)

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

### [2900. Longest Unequal Adjacent Groups Subsequence I](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/2900.%20Longest%20Unequal%20Adjacent%20Groups%20Subsequence.py)

You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

### [1137. N-th Tribonacci Number](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1137.%20N-th%20Tribonacci%20Number.py)

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

**Time Complexity** = O(n) <br>
**Space Complexity**= O(1)

### [1668. Maximum Repeating Substring](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Easy/1668.%20Maximum%20Repeating%20Substring.py)

Revise this
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

**Time Complexity** = $O(nm) \quad n:len(sequence) \quad m: len(word)$ <br>
**Space Complexity**= O(n)

## Medium

### [2383. Minimum Hours of Training to Win a Competition](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Medium/53.%20Maximum%20Subarray.py)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [1143. Longest Common Subsequence](https://github.com/AdamAdham/Algorithms/blob/main/Dynamic%20Programming/Medium/1143.%20Longest%20Common%20Subsequence.py)

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

**Time Complexity** = $O(n^2)$<br>
**Space Complexity**= $O(n^2)$

# Greedy

## Easy

### [1974. Minimum Time to Type Word Using Special Typewriter](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/1974.%20Minimum%20Time%20to%20Type%20Word%20Using%20Special%20Typewriter.py)

There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

<br>

![image](https://github.com/user-attachments/assets/aec2fcf5-9954-4f4a-9e4a-e12a0b9f574b)
<br>

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

**Time Complexity** = O(n) <br>
**Space Complexity**= O(1)

#### Adjustments / Optimizations

Do not calculate the counter clockwise way just do 26-clockwise

### [2037. Minimum Number of Moves to Seat Everyone](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2037.%20Minimum%20Number%20of%20Moves%20to%20Seat%20Everyone.py)

There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.

**Time Complexity** = O(nlog(n)) (Sort time)<br>
**Space Complexity**= O(1)

### [2259. Remove Digit From Number to Maximize Result](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2259.%20Remove%20Digit%20From%20Number%20to%20Maximize%20Result.py)

You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

**Time Complexity** = O(n^2) (Outer loop=O(n), array slicing=O(n))<br>
**Space Complexity**= O(1)

### [2591. Distribute Money to Maximum Children](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2591.%20Distribute%20Money%20to%20Maximum%20Children.py)

You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

**Time Complexity** = O(1)<br>
**Space Complexity**= O(1)

## [2591. Distribute Money to Maximum Children](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/605.%20Can%20Place%20Flowers.py)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [2383. Minimum Hours of Training to Win a Competition](https://github.com/AdamAdham/Algorithms/blob/main/Greedy/Easy/2383.%20Minimum%20Hours%20of%20Training%20to%20Win%20a%20Competition.py)

You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.

You are also given two 0-indexed integer arrays energy and experience, both of length n.

You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.

Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].

Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.

Return the minimum number of training hours required to defeat all n opponents.

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

# Top Interview Questions

## Easy

### [27. Remove Element](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Easy/27.%20Remove%20Element.py)

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

```python
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [169. Majority Element](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/169.%20Majority%20Element.py)

### [26. Remove Duplicates from Sorted Array](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Easy/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

```python
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
```

#### Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores). <br>

#### Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [169. Majority Element](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/169.%20Majority%20Element.py)

#### Could not solve alone

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

## Medium

### [80. Remove Duplicates from Sorted Array II](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II.py)

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [88. Merge Sorted Array](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/88.%20Merge%20Sorted%20Array.java)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

**Time Complexity** = O(n+m)<br>
**Space Complexity**= O(n+m)

### [122. Best Time to Buy and Sell Stock II](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.py)

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [189. Rotate Array](https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/189.%20Rotate%20Array.py)

#### Could not solve alone

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

#### Intuition

This post assumes you have already explored the reversing based solution which pretty much says:
For k=2
12345 -> 54321
54321->45321
45321->45123

So why does this work?

Let us understand the significance of k. k is nothing but a pivot point.
What this means is, in case of 12345 with k = 2, your pivot point lies at 123|45.

We want to rotate the entity along the pivot point. For simplicity let us denote either sides of pivot point as single entities as X|Y where X = 123 and Y = 45.

When we are done rotating the aggregate entity it looks something like Y|X.
Let us now understand why this tranlates to reversing the entire array. The crucial thing we will try to understand here is why irrespective of where the pivot point lies, we alwasys have to reverse the array.

The answer for this is irrespective of where you keep the pivot point the reverse always fetches the same result. Let us try to understand this. When we say reverse by default we mean mirror from the mid point.

12|34 -> 43|21

But what else is possible? Does it still fetch the same result when mirror point is changed? Let's observe

1|234 -> 432|1

Wow, why did this happen? We can understand this by adding additional padding on the lighter side and always positioning the mirror at the center. The same string can be returned as:

001|234 -> 432|100

You can alwasys balance the sides with padding resulting in the same result. So complete reverse across any pivot points fetches the same result. That is all character end up changing sides. Think about it.

Now that we have converted X|Y to Y'|X', we know in the process we ended of mirroring contents of X and Y as well.
Where Y' means Y reverse
and X' means X reverse
So in the next step we mirror them back to get the same configuration like below.

In reverse 1, X transformed this way 123 -> 321, we do not desire this transformation.
So to fix it we use:
Mirror(reverse)+Mirror(reverse) -> Original

So we reverse X and Y individually again.
So X again transforms 321 -> 123

And we get our answer 123|45 -> 45|123

Hope this was helpful. Happy learning :)
Thanks to [kooskoos](https://leetcode.com/u/kooskoos/)

**Time Complexity** = O(n)<br>
**Space Complexity**= O(1)

### [380. Insert Delete GetRandom O(1)](<https://github.com/AdamAdham/Algorithms/blob/main/Top%20Interview%20Questions/Medium/380.%20Insert%20Delete%20GetRandom%20O(1).py>)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:

-231 <= val <= 231 - 1
At most 2 \* 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

**Time Complexity** = O(1)<br>
**Space Complexity**= O(n)

# Interesting Algorithms

## [Kadan's Algorithm](https://github.com/AdamAdham/Algorithms/blob/main/Kadane's%20Algorithm.py)

Get maximum sum of a subarray
