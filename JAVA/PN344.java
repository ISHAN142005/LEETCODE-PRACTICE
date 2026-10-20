class Solution {
    public void reverseString(char[] s) {
        int startPosition = 0;
        int endPosition = s.length - 1;
        
        while (startPosition < endPosition) {
            char temporaryLetter = s[startPosition];
            s[startPosition] = s[endPosition];
            s[endPosition] = temporaryLetter;
            
            startPosition = startPosition + 1;
            endPosition = endPosition - 1;
        }
    }
}