/**
 * @param {list_char} balls
 * @return {list_char}
 */
// RBG
function dutch_flag_sort(balls) {
	let lowIdx = 0
	let midIdx = 0 // i don't understand this part
	let highIdx = balls.length - 1

	while (midIdx <= highIdx) {
		let low = balls[lowIdx]
		let mid = balls[midIdx]
		let high = balls[highIdx]

		if (mid === "R") {
			balls[lowIdx] = mid
			balls[midIdx] = low

			lowIdx++
			midIdx++

		} else if (mid === "G") {
			midIdx++
		} else {
			// if mid is "B"
			balls[highIdx] = mid
			balls[midIdx] = high

			highIdx--
		}
	}

    return balls;
}

console.log(dutch_flag_sort(["R", "R", "G", "B", "B", "B", "B", "R", "G", "G", "G", "G"]))
