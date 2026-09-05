#include <stdlib.h>


int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* answer = (int*)malloc(numsSize * sizeof(int));
    int* leftProduct = (int*)malloc(numsSize * sizeof(int));
    int* rightProduct = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
  
    leftProduct[0] = 1;  
    for (int i = 1; i < numsSize; i++) {
        leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
    }
    
    
    rightProduct[numsSize - 1] = 1;  
    for (int i = numsSize - 2; i >= 0; i--) {
        rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
    }
    
    for (int i = 0; i < numsSize; i++) {
        answer[i] = leftProduct[i] * rightProduct[i];
    }
    
   
    free(leftProduct);
    free(rightProduct);
    
    return answer;
}