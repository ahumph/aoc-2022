package aoc

import (
    "bufio"
    "os"
)

func parseInput(day string, example bool) ([]string, error) {
    var path string
    if example {
        path = day + "/example_input.txt"
    } else {
        path = day + "/input.txt"
    }
    file, err := os.Open("../../code/python/aoc-2022/2022/" + path + "/input.txt")
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}
