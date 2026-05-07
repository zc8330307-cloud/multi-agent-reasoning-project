from dataclasses import dataclass


WALL = "#"
EMPTY = "."
TRAP = "^"
KEY = "K"
CHEN_XIAOFAN = "P"
KNIGHT = "@"


@dataclass
class Position:
    row: int
    col: int


LEVELS = [
    [
        "###########",
        "#@..#....P#",
        "#.#.#.###.#",
        "#.#...#...#",
        "#.#####.#.#",
        "#.....#...#",
        "###########",
    ],
    [
        "###########",
        "#@..#..^..#",
        "#.#.#.###.#",
        "#.#...#...#",
        "#.###.#.#P#",
        "#...#.....#",
        "###########",
    ],
    [
        "###########",
        "#@..#..^..#",
        "#.#.#.###.#",
        "#.#.K.#...#",
        "#.###.#.#P#",
        "#...#.....#",
        "###########",
    ],
]


def parse_level(raw_level: list[str]) -> tuple[list[list[str]], Position]:
    grid = [list(row) for row in raw_level]
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == KNIGHT:
                return grid, Position(r, c)
    raise ValueError("关卡中缺少骑士起点。")


def draw(grid: list[list[str]], level_index: int, has_key: bool) -> None:
    print(f"\n=== 第 {level_index + 1} 关 ===")
    print("你是程子阳，目标是闯关救出陈晓凡！")
    print("操作：W/A/S/D 移动，Q 退出")
    print(f"当前状态：{'已拿到钥匙' if has_key else '未拿到钥匙'}")
    for row in grid:
        print("".join(row))


def move(
    grid: list[list[str]],
    knight: Position,
    dr: int,
    dc: int,
    has_key: bool,
) -> tuple[Position, bool, str, bool]:
    nr, nc = knight.row + dr, knight.col + dc
    target = grid[nr][nc]
    if target == WALL:
        return knight, has_key, "撞墙了，换个方向！", False

    if target == TRAP:
        return knight, has_key, "踩到陷阱，原地停住！", False

    if target == KEY:
        has_key = True

    if target == CHEN_XIAOFAN and not has_key:
        return knight, has_key, "陈晓凡前有魔法封印，先去拿钥匙！", False

    if target == CHEN_XIAOFAN and has_key:
        grid[knight.row][knight.col] = EMPTY
        return Position(nr, nc), has_key, "你抵达了陈晓凡身边！", True

    grid[knight.row][knight.col] = EMPTY
    grid[nr][nc] = KNIGHT
    return Position(nr, nc), has_key, "前进成功！", False


def play_level(raw_level: list[str], level_index: int) -> bool:
    grid, knight = parse_level(raw_level)
    has_key = False

    while True:
        draw(grid, level_index, has_key)
        command = input("你的操作: ").strip().lower()
        if command == "q":
            print("你暂时撤退了，下次继续救援！")
            return False
        direction = {
            "w": (-1, 0),
            "a": (0, -1),
            "s": (1, 0),
            "d": (0, 1),
        }.get(command)
        if direction is None:
            print("无效操作，请输入 W/A/S/D/Q。")
            continue

        knight, has_key, message, rescued = move(
            grid, knight, direction[0], direction[1], has_key
        )
        print(message)

        if rescued:
            print(f"第 {level_index + 1} 关完成，你成功救到陈晓凡！")
            return True


def main() -> None:
    print("欢迎来到《骑士救援：程子阳 x 陈晓凡》")
    for index, level in enumerate(LEVELS):
        success = play_level(level, index)
        if not success:
            return
    print("恭喜通关！程子阳成功穿越所有关卡，救出了陈晓凡！")


if __name__ == "__main__":
    main()
