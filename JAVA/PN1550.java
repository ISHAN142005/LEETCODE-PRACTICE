class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int check=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]%2!=0){
                check+=1;
            }
            else{
                check=0;
                }
    if(check==3){
        return true;
    }
        }       
    return false;
    }
}