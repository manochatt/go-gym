package main

import "fmt"

func main() {
	x := 1
	y := 2
	fmt.Println(sub(x, y))
}

func sub(num1, num2 int) int {
	return num1 - num2
}
