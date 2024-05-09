import nim_game

def test_user():
    assert nim_game.usuario_escolhe_jogada(5, 3) == 3