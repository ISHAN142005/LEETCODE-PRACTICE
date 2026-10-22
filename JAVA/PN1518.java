class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drink=numBottles;
        while(numBottles>=numExchange){
            int empty=numBottles%numExchange;
            int temp=numBottles/numExchange;
            drink+=temp;
            numBottles=temp+empty;
            
        }
        return drink;
    }
}