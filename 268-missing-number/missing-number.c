int missingNumber(int* nums, int numsSize)
{
    int n = numsSize;

    int ans = n;

    for (int i = 0; i < n; i++)
    {
        ans = ans ^ i ^ nums[i];
    }

    return ans;
}