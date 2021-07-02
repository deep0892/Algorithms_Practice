def findPlatform(arr, dep, n):
  plat_needed = 1
  result = 1
  i, j = 0, 0

  for i in range(n):
    plat_needed = 1

    for j in range(i + 1, n):
      if ((arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i])):
          plat_needed += 1
      result = max(result, plat_needed);

  return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print(findPlatform(arr, dep, n))