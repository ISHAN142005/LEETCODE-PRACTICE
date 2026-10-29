class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for char in letters:
            if ord(char)>ord(target):
                return char
        return letters[0]

       