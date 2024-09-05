class SteamUser:
    def __init__(self, username: str, games: list):
        """Initialize the Steam user with a username, a list of games, and zero played hours."""
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game: str, hours: int) -> str:
        """Play a game. Increase played hours if the game is in the library."""
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game: str) -> str:
        """Buy a game. Add it to the library if it's not already present."""
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self) -> str:
        """Return the status of the user with the number of games and total play time."""
        games_count = len(self.games)
        return f"{self.username} has {games_count} games. Total play time: {self.played_hours}"

#Example Usage
steam_user = SteamUser("JohnDoe", ["Half-Life", "Portal"])
print(steam_user.play("Half-Life", 5))   # Output: JohnDoe is playing Half-Life
print(steam_user.play("Left 4 Dead", 3)) # Output: Left 4 Dead is not in library
print(steam_user.buy_game("Left 4 Dead"))# Output: JohnDoe bought Left 4 Dead
print(steam_user.status())              # Output: JohnDoe has 3 games. Total play time: 5

