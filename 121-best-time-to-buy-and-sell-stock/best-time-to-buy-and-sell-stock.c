int maxProfit(int* prices, int pricesSize) {
    int max_prof = 0;
    int min_price = prices[0];

    for(int i = 0 ; i < pricesSize;i++){
        int profit =  prices[i] - min_price;
        if(profit>max_prof){
            max_prof = profit;
        }
        if(prices[i]<min_price){
            min_price = prices[i];
        }
    }
    return max_prof;
}