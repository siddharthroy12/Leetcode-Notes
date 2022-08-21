# Product of Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]`
is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

**Example 1**:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

**Example 2**:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

**Solution**:

We need to create two arrays with the length of input.

In one array each element is equal the the product of all element in
it's left side of input.

Do one for the right side too.

Now create the `result` array and for each element you just need to multiply
the left side of left array and right side of right array.

```python
class Solution:
    def productExceptSelf(self, nums):
        left_products = [None] * len(nums)
        right_products = [None] * len(nums)
        answer = []

        previous_product = 1

        for i in range(0, len(nums)):
            product = previous_product * nums[i]
            left_products[i] = product
            previous_product = product

        previous_product = 1

        for i in reversed(range(len(nums))):
            product = previous_product * nums[i]
            right_products[i] = product
            previous_product = product

        for i in range(len(nums)):
            current_product = 1

            if i > 0:
                current_product = current_product * left_products[i-1]

            if i < len(nums)- 1:
                current_product = current_product * right_products[i+1]

            answer.append(current_product)

        return answer
```

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> productsFromLeft(nums.size());
        vector<int> productsFromRight(nums.size());
        vector<int> res(nums.size());
        
        // Calculate products from left to right
        int product = 1;
        for (int i = 0; i < nums.size(); i++) {
            product *= nums[i];
            productsFromLeft[i] = product;
        }
        
        // Calculate products from right to left
        product = 1;
        for (int i = nums.size()-1; i > -1; i--) {
            product *= nums[i];
            productsFromRight[i] = product;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            int product = 1;
            
            if (i > 0) {
                product *= productsFromLeft[i-1];
            }
            
            if (i < nums.size()-1) {
                product *= productsFromRight[i+1];
            }
            res[i] = product;
        }
        
        return res;
    }
};
```
