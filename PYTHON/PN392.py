class Solution(object):
    def isSubsequence(self, s, t):
        s_track=0
        t_track=0
        while s_track<len(s) and t_track<len(t):
            if s[s_track]==t[t_track]:
                s_track+=1
            t_track+=1
        return s_track==len(s)