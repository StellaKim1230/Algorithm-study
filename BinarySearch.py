def binary_search(arr, search_value):
  if len(arr) == 0:
    return False

  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2

    if arr[mid] == search_value:
      return True

    if arr[mid] > search_value:
      high = mid - 1
    else:
      low = mid + 1

  return False