class Solution(object):
    def mostWordsFound(self, sentences):
        maximum=0
        for words in sentences:
            current_max=len(words.split(" "))
            if current_max>maximum:
                maximum=current_max
        return maximum
        