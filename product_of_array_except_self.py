# can i calc the product of the whole array
# skip zeros
# if there's a zero in the array store it in var
# for each value use the product / curr value
# if theres a zero make them a zero
# if the curr value is a zero make it the product of the entire array
# if there are two zeros make the entire array zero

class Solution:
    def productExceptSelf(self, nums):
        product = 1
        zero_count = 0

        for n in nums:
            if n != 0:
                product = product * n

            if n == 0:
                zero_count += 1

        for i in range(len(nums)):
            n = nums[i]

            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1 and n != 0:
                nums[i] = 0
            elif n != 0:
                nums[i] = product // n
            elif n == 0:
                nums[i] = product
            else:
                print(f'We should not get here you forgot a condition nums[i]={n} product={product} i={i}')

        return nums

sol = Solution()

print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
print(sol.productExceptSelf([-1, 0, 0, -3, 3]))
