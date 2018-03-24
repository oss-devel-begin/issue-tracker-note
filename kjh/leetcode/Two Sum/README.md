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

```cpp
vector<int> twoSum(vector<int> &numbers, int target)
{
    //Key is the number and value is its index in the vector.
	unordered_map<int, int> hash;
	vector<int> result;
	for (int i = 0; i < numbers.size(); i++) {
		int numberToFind = target - numbers[i];

            //if numberToFind is found in map, return them
		if (hash.find(numberToFind) != hash.end()) {
                    //+1 because indices are NOT zero based
			result.push_back(hash[numberToFind] + 1);
			result.push_back(i + 1);			
			return result;
		}

            //number was not found. Put it in the map.
		hash[numbers[i]] = i;
	}
	return result;
}
```
