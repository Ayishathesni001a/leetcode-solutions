class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mnm_price = prices[0]
        mxm_profit = 0
        for price in prices:
            if price < mnm_price:
                mnm_price = price
            profit = price - mnm_price
            if profit > mxm_profit:
                mxm_profit = profit
        return mxm_profit         