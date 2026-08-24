#include<map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        if (size(nums) == 2) return {0,1};
        std::map<int, int> m;
        for (int i = 0; i < size(nums); ++i){
            if (!m.contains(target-nums[i])) {
                m[nums[i]] = i;
            }
            else return {m[target-nums[i]], i};
        }
    }
};
