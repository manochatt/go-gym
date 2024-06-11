let array1: number[] = [1,2,3]
let array2: number[] = [5,6]

function plus(array1: number[], array2: number[]){
    if(array1.length-array2.length>0){
        array2 = new Array(array1.length-array2.length).fill(0).concat(array2)
    } else {
        array1 = new Array(array2.length-array1.length).fill(0).concat(array1)
    }

    let ans: number[] = []
    let carry = 0
    
    for (let i = array1.length-1; i>=0; i--) {
        let subAns = array1[i]+array2[i] + carry
        ans.push(subAns%10)
        carry = Math.floor(subAns/10)
    }

    if(carry!=0){
        ans.push(carry)
    }

    return ans.reverse()
}

console.log(plus(array1, array2))

function multiply(array1: number[], array2: number[]){
    let ans = []

    for (let i = array1.length)
}