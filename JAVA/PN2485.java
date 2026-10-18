class Solution {
    public int pivotInteger(int n) {
        int total=(n*(n+1)/2);
        int current=0;
        for(int i=0;i<=n;i++){
            current+=i;
            int rest=total-current+i;
            if (current==rest){
                return i;
            }
        }
        return -1;
        
    }
}