class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length<=1) return nums;

        int mid=nums.length/2;

        int[] first=new int[mid];
        int[] second=new int[nums.length-mid];

        for(int i=0;i<mid;i++) {
            first[i]=nums[i];
        }

        for(int i=mid;i<nums.length;i++) {
            second[i-mid]=nums[i];
        }

        sortArray(first);
        sortArray(second);

        merge(nums,first,second);

        return nums;
    }

    public void merge(int[] nums,int[] first,int[] second) {
        int i=0,j=0,k=0;

        while(i<first.length && j<second.length) {
            if(first[i]<=second[j]) {
                nums[k]=first[i];
                i++;
            }
            else {
                nums[k]=second[j];
                j++;
            }
            k++;
        }

        while(i<first.length) {
            nums[k]=first[i];
            i++;
            k++;
        }

        while(j<second.length) {
            nums[k]=second[j];
            j++;
            k++;
        }
    }
}