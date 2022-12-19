package main

import (
    "fmt"
    "log"
    "github.com/ahumph/aoc"
)

func main() {
    lines, err := aoc.parseInput("../../code/python/aoc-2022/2022/12/input.txt")
    if err != nil {
        log.Fatalf("parseInput: %s", err)
    }
    for i, line := range lines {
        fmt.Printf("%2d %s\n", i, line)
    }
}
