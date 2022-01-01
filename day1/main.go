package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readInput(filename string) []int {
	filePath := "./" + filename
	data, err := os.ReadFile(filePath)
	check(err)

	raw_lines := strings.Split(string(data), "\n")

	// Convert each string to an int
	var lines []int
	for _, c := range raw_lines {
		value, err := strconv.Atoi(c)
		if err == nil {
			lines = append(lines, value)
		}
	}
	return lines
}

func partA() {
	input := readInput("input.txt")

	// starting with 2nd number, add to count if number is greater than the previous
	count := 0
	for i := 0; i < len(input); i++ {
		// fmt.Print(input[i])
		if i == 0 {
			continue
		}
		if input[i] > input[i-1] {
			count++
			// fmt.Println(" increased - " + strconv.Itoa(count))
		} else {
			// fmt.Println(" decreased - " + strconv.Itoa(count))
		}
	}

	fmt.Println(count)
}

func main() {
	partA()
}
