class Solution {
    public int countTriples(int n) {
        int count=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                int left=(i*i)+(j*j);
                for(int k=1;k<=n;k++){
                    int right=(k*k);
                    if(right==left){count+=1;}
                    else if(right>left){break;}
                }
            }
        }
        return count;
    }
}