
/**
 * @param {list_int32} numbers
 * @return {list_int32}
 */
// we want even on the left and odd on the right
// we want even before the odd
// two pointers l & r
// if left is even and right is odd increment both
// if left is odd and right is even swap
// if left is even and right is even left++
// if left is odd and right is odd right--
function segregate_evens_and_odds(numbers) {
	let leftIdx = 0
	let rightIdx = numbers.length -1

	while (leftIdx < rightIdx) {
		const left = numbers[leftIdx]
		const right = numbers[rightIdx]

		if (isEven(left) && isOdd(right)) {
			leftIdx++
			rightIdx--
		} else if (isEven(left) && isEven(right)) {
			leftIdx++
		} else if (isOdd(left) && isOdd(right)) {
			rightIdx--
		} else {
			numbers[leftIdx] = right
			numbers[rightIdx] = left
		}
	}

    return numbers;
}

function isEven(n) {
	return n % 2 === 0
}

function isOdd(n) {
	return !isEven(n)
}

console.log(segregate_evens_and_odds([1, 2, 3, 4]))
