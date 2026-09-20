// Split Array Largest Sum
// Problem: https://leetcode.com/problems/split-array-largest-sum/
// Difficulty: Medium
// Language: cpp

class Solution {
public:
    bool isValid(int mid,int n , int k , vector<int>& nums) { 
        int students =1 , pages=0;
        for(int i =0;i<n;i++){
            if(nums[i]>mid){
                return false;
            }
            if (pages+nums[i]<=mid){
                pages+=nums[i];
            }
            else{
                students++;
                pages=nums[i];
            }
        }
        return students <= k;
    
    
    }
    int splitArray(vector<int>& nums, int k) {
        int sum = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }
        int ans = -1;
        int mid;
        int start = 0, end = sum;

        while (start <= end) {
            mid = start + (end - start) / 2;
            if (isValid(mid,n,k,nums)) {
                ans = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return ans;
    }
};