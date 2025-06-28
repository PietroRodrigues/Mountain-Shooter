from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d, K_SPACE, K_RETURN, USEREVENT

# W
WIN_WIDTH = 546
WIN_HEIGHT = 324

# C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# M
MENU_OPTION = ("NEW GAME 1P",
                "NEW GAME 2P - COOPERATIVE",
                "NEW GAME 2P - COMPETITIVE",
                "SCORE",
                "EXIT")


ENTITY_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 6,
    "Player1": 5,
    "Player1Shot": 10,
    "Player2": 5,
    "Player2Shot": 10,
    "Enemy1": 1,
    "Enemy1Shot": 8,
    "Enemy2": 2,
    "Enemy2Shot": 4,
}
ENTITY_HEALTH = {
    "Player1": 300,
    "Player2": 300,
    "Enemy1": 50,
    "Enemy2": 60
}

EVENT_ENEMY = USEREVENT + 1
ENEMY_SPAWN_RATE = 4000  # milliseconds

PLAYER_KEY_UP = {
    "Player1": K_w,
    "Player2": K_UP
}
PLAYER_KEY_DOWN = {
    "Player1": K_s,
    "Player2": K_DOWN
}
PLAYER_KEY_LEFT = {
    "Player1": K_a,
    "Player2": K_LEFT
}
PLAYER_KEY_RIGHT = {
    "Player1": K_d,
    "Player2": K_RIGHT
}
PLAYER_KEY_SHOOT = {
    "Player1": K_SPACE,
    "Player2": K_RETURN
}

ENTITY_SHOOT_DELAY = {
    "Player1": 20,
    "Player2": 20,
    "Enemy1": 100,
    "Enemy2": 50,
}

ENTITY_SHOOT_DAMAGE = {
    "Player1Shot": 10,
    "Player2Shot": 10,
    "Enemy1Shot": 10,
    "Enemy2Shot": 10
}

ENTITY_SCORE = {
    "Enemy1": 10,
    "Enemy2": 20
}

VOLUME = {
    "music": 0.07,
    "sound": 0.1
}