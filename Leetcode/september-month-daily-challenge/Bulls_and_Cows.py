# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455/

"""
Problem Statement: 
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates how many digits in 
said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). 
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows. 
Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""
# # Solution: 2 solution with different approaches

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         dict = {}
#         l, bulls, crows  = len(secret), 0, 0
        
#         for keys in secret: 
#             dict[keys] = dict.get(keys, 0) + 1
        
#         for i in range(l):
#             is_eq = int(secret[i] == guess[i])
#             bulls += is_eq
#             if is_eq: dict[guess[i]] -= is_eq
        
#         for i in range(l):
#             if secret[i] != guess[i] and dict.get(guess[i], 0) > 0:
#                 dict[guess[i]] -= 1
#                 crows += 1
                
#         return f"{bulls}A{crows}B"

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b,c  = 0, 0
        
        for i in range(len(secret)):
            b += int( secret[i] == guess[i])
        
        for ch in set(secret):
            c += min(secret.count(ch), guess.count(ch))
                
        return f"{b}A{c - b}B"

def main():
    sol = Solution()
    secret = "1123"
    guess = "0111"
    print(sol.getHint(secret, guess))
    secret = "1807"
    guess = "7810"
    print(sol.getHint(secret, guess))


if __name__ == "__main__":
    main()