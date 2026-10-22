class Solution {
    public int arrangeCoins(int n) {
        int rows=0;
        int i=1;
        while((n/i)>0){
            if(n/i>0){
                rows++;
                n-=i;
            }
            i++;
        }
        return rows;
    }
}