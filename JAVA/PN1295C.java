class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for(int i=0;i<nums.length;i++){
            int n=nums[i];

            if((n>=10 && n<=99) || n>=1000 && n<=9999){
                count+=1;
            }
    }
    return count;
}
}