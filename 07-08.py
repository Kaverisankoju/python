import random

# Snake positions: key = head, value = tail
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

# Ladder positions: key = bottom, value = top
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# Initial positions
player1 = 0
player2 = 0

def roll_dice():
    return random.randint(1, 6)

def move(player, player_name):
    input(f"{player_name}'s turn. Press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{player_name} rolled a {dice}")
    player += dice

    if player > 100:
        print(f"{player_name} needs exact number to reach 100. Staying at {player - dice}")
        return player - dice

    if player in snakes:
        print(f"Oh no! {player_name} got bitten by a snake! Going from {player} to {snakes[player]}")
        player = snakes[player]
    elif player in ladders:
        print(f"Yay! {player_name} climbed a ladder! Going from {player} to {ladders[player]}")
        player = ladders[player]
    else:
        print(f"{player_name} moved to {player}")

    return player

# Game loop
while True:
    player1 = move(player1, "Player 1")
    if player1 == 100:
        print("🎉 Player 1 wins the game! 🎉")
        break

    player2 = move(player2, "Player 2")
    if player2 == 100:
        print("🎉 Player 2 wins the game! 🎉")
        break
