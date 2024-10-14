class Battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.turn = "player"  # Tracks whose turn it is

    def player_attack(self, move):
        if self.turn == "player":
            damage = move.calculate_damage(self.player_pokemon)
            self.enemy_pokemon.take_damage(damage)
            print(f"{self.player_pokemon.name} used {move.name}!")
            self.turn = "enemy"

    def enemy_attack(self):
        if self.turn == "enemy":
            damage = 5  # Simplified enemy attack
            self.player_pokemon.take_damage(damage)
            print(f"{self.enemy_pokemon.name} attacked!")
            self.turn = "player"
