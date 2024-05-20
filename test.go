package main

import "math"

func largestLocal(grid [][]int) [][]int {
	n := len(grid)
	var res [][]int
	for i := 1; i < n-1; i++ {
		var cur_row []int
		for j := 1; j < n-1; j++ {
			var tmp int

			for p := 1; p < i+2; p++ {
				for k := 1; k < j+2; k++ {
					tmp = math.Max(tmp, int(grid[p][k]))
				}
			}
			cur_row = append(cur_row, tmp)
		}
		res = append(res, cur_row)
	}
	return res
}
