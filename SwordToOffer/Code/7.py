# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):

        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number-2)


solution = Solution()
print solution.jumpFloor(4)
