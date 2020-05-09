# https://leetcode.com/problems/snapshot-array/

###### For binary search solution in discussion - https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search #####

####### My solution ########
class SnapshotArray:

    def __init__(self, length: int):
        self.arr = []
        for i in range(length):
            self.arr.append([0])
        
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        while len(self.arr[index]) < (self.snap_id + 2):
            self.arr[index].append(self.arr[index][-1])
            
        self.arr[index][-1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id > (len(self.arr[index])-1):
            return self.arr[index][-1]
        return self.arr[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)