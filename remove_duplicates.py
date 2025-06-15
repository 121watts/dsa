# if n1 and n2 are the same

class Solution:
    def removeDuplicates(sef, nums) -> int:
        p1 = 0
        p2 = 1
        end = len(nums) - 1
        k = 0
        dupe_counter = 0

        while p2 < end:
            n1 = nums[p1]
            n2 = nums[p2]
            print(f'dupe_counter {dupe_counter}, p1 {p1}, p2 {p2}')

            if n1 == n2:
                dupe_counter += 1
                if dupe_counter > 1:
                    nums[p2] = '_'
                p2 += 1
            else:
                dupe_counter = 0
                p2 += 1
                p1 = p2 - 1


        return nums


sol = Solution()

s1 = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
print(s1)


# s2 = sol.removeDuplicates([1,1,1,2,2,3])
# print(s2)
