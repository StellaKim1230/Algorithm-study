const binarySearch = (array, search_value) => {
  if (array.length === 0) return

  var low = 0
  var high = array.length - 1
  var middle

  while (low <= high) {
    middle = Math.floor((low + high) / 2)

    if (array[middle] === search_value) return middle

    if (array[middle] > search_value) {
      high = middle - 1
    } else {
      low = middle + 1
    }
  }
}

console.log(binarySearch([21, 45, 48, 90, 101, 102, 105, 110], 105))
