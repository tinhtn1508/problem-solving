def cyclicSort(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

def missNumber(nums):
    cyclicSort(nums)
    miss = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            miss.append(i+1)
    return miss

def missNumberV2(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    miss = []
    for i in range(len(nums)):
        if nums[i] != i:
            miss.append(i)
    return miss

def removeDuplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            correctIndex = nums[i]
            if nums[i] != nums[correctIndex]:
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return 0

def findDuplicate(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i]-1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    dup = []
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            dup.append(nums[i])
    return dup

def missAndDup(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i]-1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    dup = []
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            dup.append(nums[i])
            dup.append(i+1)
        
    return dup

if __name__ == "__main__":
    nums = [2, 3, 1, 7, 2, 3, 5, 1, 9]
    cyclicSort(nums)
    print("cyclic sort: {}".format(nums))
    print("miss numbers: {}".format(missNumber(nums)))
    print("miss numbers v2: {}".format(missNumberV2([1, 1, 4, 1])))
    print("remove duplicate: {}".format(removeDuplicate([1, 4, 4, 3, 2])))
    print("remove duplicates: {}".format(findDuplicate([5, 2, 7, 2, 3, 5, 3])))
    print("miss and dup: {}".format(missAndDup([3, 1, 2, 5, 2])))