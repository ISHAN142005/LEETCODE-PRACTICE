class Solution {
    public int commonFactors(int a, int b) {
        int temp=0;
        int count=0;
        if(a>b){
            temp=b;}
        else{
            temp=a;
        }
        for(int i=1;i<=temp;i++){
            if(a%i==0 && b%i==0){
                count+=1;
            }
           
        }
        return count;
        }
    }
