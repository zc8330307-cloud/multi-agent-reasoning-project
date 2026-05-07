import examples.couple_knight_game as game


def test_parse_level_raises_without_knight():
    level = [
        "###",
        "#P#",
        "###",
    ]

    try:
        game.parse_level(level)
    except ValueError as exc:
        assert "缺少骑士起点" in str(exc)
    else:
        raise AssertionError("Expected ValueError when level has no knight start.")


def test_play_level_returns_false_when_user_quits(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _prompt: "q")

    result = game.play_level(game.LEVELS[0], 0)

    assert result is False


def test_main_prints_success_when_all_levels_pass(monkeypatch, capsys):
    monkeypatch.setattr(game, "LEVELS", [["dummy-1"], ["dummy-2"]])
    monkeypatch.setattr(game, "play_level", lambda _raw_level, _idx: True)

    game.main()

    output = capsys.readouterr().out
    assert "恭喜通关" in output


def test_play_level_handles_invalid_command_then_continue(monkeypatch, capsys):
    commands = iter(["x", "q"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    result = game.play_level(game.LEVELS[0], 0)

    output = capsys.readouterr().out
    assert result is False
    assert "无效操作" in output
