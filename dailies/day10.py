#!/usr/bin/env python3
""" Functions to solve the Day Ten challenges. """

TITLE = "Pipe Maze"

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

# Functions used by both the Tracker and PipeMaze classes
def get_west(maze: list[str], current_pos: tuple[int, int]) -> (str, tuple[int, int]):
    """Return the symbol and coordinates to the left/west of current_pos."""
    x = current_pos[0] - 1
    y = current_pos[1]
    if x < 0:
        raise ValueError(f"Out of bounds to the left/west: ({x},{y})")
    return (maze[x][y], (x, y))

def get_east(maze: list[str], current_pos: tuple[int, int]) -> (str, tuple[int, int]):
    """Return the symbol and coordinates to the right/east of current_pos."""
    x = current_pos[0] + 1
    y = current_pos[1]
    if x > len(maze[0]) - 1:
        raise ValueError(f"Out of bounds to the right/east: ({x}, {y})")
    return (maze[x][y], (x, y))

def get_north(maze: list[str], current_pos: tuple[int, int]) -> (str, tuple[int, int]):
    """Return the symbol and coordinates up from/north of current_pos."""
    x = current_pos[0]
    y = current_pos[1] - 1
    if y < 0:
        raise ValueError(f"Out of bounds to the north/up: ({x}, {y})")
    return (maze[x][y], (x, y))

def get_south(maze: list[str], current_pos: tuple[int, int]) -> (str, tuple[int, int]):
    """Return the symbol and coordinates down from/south of current_pos."""
    x = current_pos[0]
    y = current_pos[1] + 1
    if y >= len(maze):
        raise ValueError(f"Out of bounds to the south/down: ({x}, {y})")
    return (maze[x][y], (x, y))

class Tracker:
    """Follows pipe in a single direction."""

    def __init__(
        self,
        name: str,
        current_pos: tuple[int, int],
        prev_pos: tuple[int, int],
        maze: list[str],
    ):
        # self.current_pipe = current_pipe  # No, can infer from maze and current_pos
        self.name = name  # To distinguish trackers during debugging
        self.current_pos = current_pos
        self.prev_pos = current_pos
        self.steps = 1  # Adjacent to START at creation
        self.maze = maze
        # debug only message:
        print(f"Tracker {self.name} created at {self.current_pos}")

    def __str__(self):
        return (
            f"Tracker {self.name}: step={self.steps}, "
            f"({self.current_pos[0]}, {self.current_pos[1]}), "
            f"pipe={self.maze[self.current_pos[0]][self.current_pos[1]]}"
        )

    def take_step(self):
        """Take one step and update prev_pos, current_pos, and steps."""

        # Unlike Start symbol, bounds checking unnecessary because we can assume the pipe
        #  forms a loop without running off the map.


class PipeMaze:
    """Map of a pipe maze with support methods."""

    def __init__(self):
        self.maze = []  # List of strings
        self.start = (-1, -1)  # x,y coordinates
        self.rows = 0
        self.cols = 0
        self.farthest = -1  # Unknown until calculated

    def __str__(self):
        return f"PipeMaze: rows={self.rows}, cols={self.cols}, start=({self.start})"

    def add_row(self, line: str):
        """Add horizontal row of map data"""

        new_line = line.strip()  # sanitize input
        for col, char in enumerate(new_line):
            if char == "S":
                self.start = (col, self.rows)
        if self.cols < 1:
            self.cols = len(new_line)
        self.maze.append(new_line)
        self.rows += 1

    def follow_pipe(self):
        """Send two trackers to follow loop until they meet in the middle."""

        trackers = []
        tracker_count = 0
        # TODO: refactor Look Left and Look Right since I added support functions
        # Find both adjacent points on map and send a Tracker down each path
        ## Look Left, if Start not on left edge
        if self.start[0] > 0:
            match self.maze[self.start[0] - 1][self.start[1]]:
                case "-" | "L" | "F":
                    trackers.append(
                        Tracker(
                            str(tracker_count + 1),
                            (self.start[0] - 1, self.start[1]),
                            self.start,
                            self.maze,
                        )
                    )
                    tracker_count += 1
                case _:
                    pass
        ## Look Right, if Start not on right edge
        if self.start[0] < self.cols - 2:
            #print("looked right")
            pipe, (x, y) = get_east(self.maze, self.start)
            print(f"{pipe=}")
            match pipe:
                case "-" | "7" | "J":
                    trackers.append(
                        Tracker(
                            str(tracker_count + 1),
                            (self.start[0] - 1, self.start[1]),
                            self.start,
                            self.maze,
                        )
                    )
                    tracker_count += 1
                case _:
                    pass

        ## Look Up, if Start not on top edge
        if self.start[1] > 0:
            pipe, (x, y) = get_north(self.maze, self.start)
            match pipe:
                case "|" | "7" | "F":
                    trackers.append(
                        Tracker(str(tracker_count + 1),
                                (x, y),
                                self.start,
                                self.maze
                        )
                    )
                    tracker_count += 1
                case _:
                    pass

        ## Look Down, if Start not on bottom edge
        if self.start[1] < self.rows - 2:
            pipe, (x, y) = get_south(self.maze, self.start)
            match pipe:
                case "|" | "L" | "J":
                    trackers.append(
                        Tracker(str(tracker_count + 1),
                                (x, y),
                                self.start,
                                self.maze
                        )
                    )
                    tracker_count += 1                   
                case _:
                    pass

        # Once both Trackers are sent out, we can infer the shape of S pipe
        #   ...if needed

        # debug: how many trackers created?
        print(f"{tracker_count=} {len(trackers)=}")

        while trackers[0].current_pos != trackers[1].current_pos:
            trackers[0].take_step()
            trackers[1].take_step()

        self.farthest = trackers[0].steps


def part_one(data: list[str]) -> int:
    """Calculate the results for Part One."""

    # total = 0
    maze = PipeMaze()

    for line in data:
        maze.add_row(line)

    print(maze)
    maze.follow_pipe()  # Calculate result

    return maze.farthest


def part_two(data: list[str]) -> int:
    """Calculate the results for Part Two."""

    total = 0

    # TBD ...

    return total
