# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/


######## This is also a design question. Again there can be multiple correct answers for these questions ##########
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min = float('inf')
        

    def push(self, x: int) -> None:
        if x < self.min:
            self.min = x
        self.nums.append(x)

    def pop(self) -> None:
        if len(self.nums) > 0:
            num = self.nums.pop()
            if num == self.min:
                if len(self.nums) > 0:
                    self.min = min(self.nums)
                else:
                    self.min = float('inf')

    def top(self) -> int:
        if len(self.nums) > 0:
            return self.nums[-1]

    def getMin(self) -> int:
        return self.min

######### O(1) time complexity solution using a seperate stack for storing min values
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')
        self.min_stack = []
        

    def push(self, x: int) -> None:
        if x <= self.min:
            self.min_stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()