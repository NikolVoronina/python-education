from typing import List

class Solution:
    @staticmethod
    def zeroFilledSubbarray (nums: List[int]) -> int :
        count = 0
        adjacent_zeroes = 0

        for number in nums:
            if number:
                adjacent_zeroes = 0
                continue

            adjacent_zeroes += 1
            count += adjacent_zeroes
            
        return count
    

print(Solution.zeroFilledSubbarray([1,3,0,0,2,0,0,4]))  # Result: 6
print(Solution.zeroFilledSubbarray([0,0,0]))            # Result: 6
print(Solution.zeroFilledSubbarray([2,10,2019, 345]))   # Result: 0