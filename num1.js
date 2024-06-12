function hammingWeight(n) {
    var ans = 0;
    while (n !== 0) {
        ans += n % 2;
        n = Math.floor(n / 2);
        console.log(n);
    }
    return ans;
}
;
console.log(hammingWeight(11));
