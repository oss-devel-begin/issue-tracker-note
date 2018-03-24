# Two Sum
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int save1, save2;
        for(int i = 0; i < sizeof(nums); i++)
        {
            for(int j = i+1; j < sizeof(nums); j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    save1 = i;
                    save2 = j;
                    break;
                }
            }
        }
        return {save1, save2};
    }
};
```
