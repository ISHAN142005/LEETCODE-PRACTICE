class Solution {
    public int numberOfChild(int n, int k) {
        int pass=k/(n-1);
        int left=k%(n-1);
        if(pass%2==0){return left;}
        else{return (n-1-left);}
    }
}