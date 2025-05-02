/**
 * @param {list_int32} numbers
 * @param {int32} target
 * @return {list_int32}
 */

// two pointers
// if sum less than target increment low pointer
// if sum higher than target decrement high pointer

function pair_sum_sorted_array(numbers, target) {
	let lowIdx = 0
	let highIdx = numbers.length - 1

	while (lowIdx < highIdx) {
		const low = numbers[lowIdx]
		const high = numbers[highIdx]
		const sum = low + high

//		console.log(low, high, sum, numbers, target)
		if (sum > target) {
			highIdx--
		} else if (sum < target) {
			lowIdx++
		} else {
			return [lowIdx, highIdx]
		}
	}

	return [-1, -1]
}

console.log(pair_sum_sorted_array([1, 2, 3, 5, 10], 7))
console.log(pair_sum_sorted_array([1, 2], 10))
console.log(pair_sum_sorted_array([1, 2, 2, 3, 4, 5, 10], 7))
