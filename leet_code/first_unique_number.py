class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = {}
        self.q = []
        self.recent = 0
        for i in range(len(nums)):
            # print(self.d, nums[i])
            if nums[i] in self.d.keys():
                if self.d[nums[i]] != -1:
                    index = self.d[nums[i]]
                    self.q[index] = -1
                    self.d[nums[i]] = -1
            else:
                self.d[nums[i]] = len(self.q)
                self.q.append(nums[i])
        
                
                

    def showFirstUnique(self) -> int:
        for i in range(self.recent, len(self.q)):
            if self.q[i] != -1:
                self.recent = i
                return self.q[i]
        
        self.recent = len(self.q)
        return -1

    def add(self, value: int) -> None:
        if value in self.d.keys():
            if self.d[value] != -1:
                index = self.d[value]
                self.q[index] = -1
                self.d[value] = -1
        else:
            self.d[value] = len(self.q)
            self.q.append(value)
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)