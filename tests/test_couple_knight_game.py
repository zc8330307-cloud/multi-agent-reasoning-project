from examples.couple_knight_game import CHEN_XIAOFAN, KEY, KNIGHT, TRAP, WALL, move
from examples.couple_knight_game import Position


def test_move_blocked_by_wall():
    grid = [
        [WALL, WALL, WALL],
        [WALL, KNIGHT, WALL],
        [WALL, WALL, WALL],
    ]
    knight = Position(1, 1)

    new_pos, has_key, message, rescued = move(grid, knight, 0, 1, False)

    assert new_pos == knight
    assert has_key is False
    assert rescued is False
    assert "撞墙" in message


def test_cannot_rescue_without_key():
    grid = [
        [WALL, WALL, WALL],
        [WALL, KNIGHT, CHEN_XIAOFAN],
        [WALL, WALL, WALL],
    ]
    knight = Position(1, 1)

    new_pos, has_key, message, rescued = move(grid, knight, 0, 1, False)

    assert new_pos == knight
    assert has_key is False
    assert rescued is False
    assert "先去拿钥匙" in message


def test_can_rescue_with_key():
    grid = [
        [WALL, WALL, WALL],
        [WALL, KNIGHT, CHEN_XIAOFAN],
        [WALL, WALL, WALL],
    ]
    knight = Position(1, 1)

    new_pos, has_key, message, rescued = move(grid, knight, 0, 1, True)

    assert new_pos == Position(1, 2)
    assert has_key is True
    assert rescued is True
    assert "抵达了陈晓凡身边" in message


def test_pick_up_key_updates_state():
    grid = [
        [WALL, WALL, WALL],
        [WALL, KNIGHT, KEY],
        [WALL, WALL, WALL],
    ]
    knight = Position(1, 1)

    new_pos, has_key, message, rescued = move(grid, knight, 0, 1, False)

    assert new_pos == Position(1, 2)
    assert has_key is True
    assert rescued is False
    assert "前进成功" in message


def test_trap_keeps_knight_in_place():
    grid = [
        [WALL, WALL, WALL],
        [WALL, KNIGHT, TRAP],
        [WALL, WALL, WALL],
    ]
    knight = Position(1, 1)

    new_pos, has_key, message, rescued = move(grid, knight, 0, 1, False)

    assert new_pos == knight
    assert has_key is False
    assert rescued is False
    assert "踩到陷阱" in message
