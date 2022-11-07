# Binary Search by Adi

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def binarySearch(anArray, item):
  lowIndex = 0
  highIndex = len(anArray) - 1

  while lowIndex <= highIndex:
    middleIndex = (lowIndex + highIndex) // 2

    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      highIndex = middleIndex - 1
    else:
      lowIndex = middleIndex + 1

  return -1


print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))