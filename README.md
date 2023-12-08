# 🎄 Advent-of-Code-2023 🎄

![2023_Trebuchet](https://github.com/Milnor/Advent-of-Code-2023/assets/7789866/e22b85cb-0403-4c56-98bf-ac6a42c0f5c4)


My favorite annual coding competition. Will this be the year I finally complete it?  

## Usage
* As of day 7, there are still no dependencies outside of the Python standard library.
* Supply your own puzzle input in `data/dayXX.txt` and `data/sampleXX.txt` where XX is the number of the day (with a leading zero if less than 10).
    - I saw on reddit that sharing your own input data is against the rules, so I removed it from this repo.
* Default usage will use actual challenge data and display all days completed so far.
```
./solver.py
```
* Alternatively, you can specify the smaller sample data sets with `--samples` and/or limit which day's puzzles are displayed with `--days X Y Z`
```
./solver.py --days 5 2 --samples
```

## Misc
* I'm developing on an Ubuntu 22.04 machine running Python 3.10
* While I doubt anyone cares to copy my solutions, in the interest of avoiding spoilers, I'm not pushing code for day *n* until day *n+1*

## TODO
* [ ] Day 5 Part 2 is a disaster. Fix it.
