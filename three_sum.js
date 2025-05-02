// we want this array to be sorted so we can take advantage of the multiple pointer approach
// target -> a + b + c = 0
// a = arr[i]
// b = arr[i + 1]
// c = arr[arr.length - 1]
// loop through each value of a
// if the prev value of a is === current value of a then we skip this calc (this will prevent dupes of a)
// now, for b + c
// if a + b + c < 0 we need to increment b to find a "lager number" but keep c the same
// if a + b + c > 0 we need to decrement c to find a "smaller number" but keep b the same
// if a + b + c are equal then we can append "a,b,c" to result --> need to check for dupes
// if arr[b + 1] is equal to current b this is a dupe and we don't push the value into the result
// otherwise said if they are NOT equal then push into the result
// either way, we have found a sum of zero so we need to increment and decrement j and k

function find_zero_sum(array) {
    const arr = array.sort((a, b) => a - b)
    const result = []

    for (let i = 0; i < arr.length; i++) {
        if (i > 0 && arr[i] === arr[i - 1]) continue

        let j = i + 1
        let k = arr.length - 1

        while (j < k) {
            const [a, b, c] = [arr[i], arr[j], arr[k]]
            const sum = a + b + c

            if (sum < 0) {
                j++
            } else if (sum > 0) {
                k--
            } else {
                const prevB = arr[j - 1]
                const prevC = arr[k + 1]
                if (b !== prevB || c !==  prevC) {
                    result.push(`${a},${b},${c}`)
                }

                j++
                k--
            }
        }
    }

    return result
}


console.log(find_zero_sum([1, -1, 0, 2, -2, 0]))
console.log(find_zero_sum([0, 0, 0, 0, 0, 0]))
console.log(find_zero_sum([-1, 0, 1, -1, 0, 1]))
// [-1, -1, 0, 0, 1, 1]
