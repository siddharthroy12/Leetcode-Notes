# Best Time to Buy and Sell Stock (Blind)

You are given an array `prices` where `prices[i]` is the price of a given stock on 
the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and 
choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return `0`.

**Example 1**:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2**:

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Solution**:

Have two pointers one is the for buying and another for selling.
Initially buying pointer will point at the first and selling pointer will point at
second.

Calculate the profit and store the max profit in a variable if the proft is negative then
move the buying pointer to the selling pointer and move the selling pointer to next.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                
                max_profit = max(max_profit, profit)
                right += 1
        
        return max_profit
```
