"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #0 - Hello World! (helloworld.py)


Author: Chris Lai

Difficulty Level: 0/10

Use this file to practice the submission format for the rest of the Code Clashes.
Return a string to the function that prints out "Hello World!".

Test Cases:
Input: ""   Output: "Hello World!"
"""

class Solution:
    def helloworld(self):
        # return type: String

        # TODO: Write code below to return a string with the solution to the prompt
        return "Hello World!"

def main():
    tc1 = Solution()
    ans = tc1.helloworld()
    print(ans)

if __name__ == "__main__":
    main()