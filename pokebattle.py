import random

# Expanded Type effectiveness dictionary
TYPE_EFFECTIVENESS = {
    'Fire': {'Grass': 2.0, 'Water': 0.5, 'Fire': 1.0, 'Electric': 1.0, 'Normal': 1.0, 'Steel': 2.0, 'Ground': 1.0, 'Ghost': 1.0},
    'Water': {'Fire': 2.0, 'Grass': 0.5, 'Water': 1.0, 'Electric': 1.0, 'Normal': 1.0, 'Steel': 1.0, 'Ground': 2.0, 'Ghost': 1.0},
    'Grass': {'Water': 2.0, 'Fire': 0.5, 'Grass': 1.0, 'Electric': 1.0, 'Normal': 1.0, 'Steel': 0.5, 'Ground': 2.0, 'Ghost': 1.0},
    'Electric': {'Water': 2.0, 'Grass': 0.5, 'Fire': 1.0, 'Electric': 1.0, 'Normal': 1.0, 'Steel': 1.0, 'Ground': 0.0, 'Ghost': 1.0},
    'Normal': {'Water': 1.0, 'Grass': 1.0, 'Fire': 1.0, 'Electric': 1.0, 'Normal': 1.0, 'Steel': 0.5, 'Ground': 1.0, 'Ghost': 0.0},
    'Steel': {'Water': 0.5, 'Grass': 1.0, 'Fire': 0.5, 'Electric': 0.5, 'Normal': 1.0, 'Steel': 1.0, 'Ground': 1.0, 'Ghost': 1.0},
    'Ground': {'Water': 1.0, 'Grass': 0.5, 'Fire': 2.0, 'Electric': 2.0, 'Normal': 1.0, 'Steel': 2.0, 'Ground': 1.0, 'Ghost': 1.0},
    'Ghost': {'Water': 1.0, 'Grass': 1.0, 'Fire': 1.0, 'Electric': 1.0, 'Normal': 0.0, 'Steel': 1.0, 'Ground': 1.0, 'Ghost': 2.0},
}

class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.type = move_type
        self.power = power

class Pokemon:
    def __init__(self, name, pokemon_type, moves):
        self.name = name
        self.type = pokemon_type
        self.moves = moves
        self.health = 100

    def choose_move(self):
        print(f"\n{self.name}'s moves:")
        for i, move in enumerate(self.moves):
            print(f"{i+1}. {move.name} ({move.type}) - Power: {move.power}")
        while True:
            try:
                choice = int(input("Enter the number of the move: ")) - 1
                if 0 <= choice < len(self.moves):
                    return self.moves[choice]
                else:
                    print("Invalid choice. Please select a valid move number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_random_move(self):
        return random.choice(self.moves)

    def display_health(self):
        health_bar = '+' * (self.health // 10)
        print(f"{self.name} Health: [{health_bar}] {self.health}/100")

class Team:
    def __init__(self):
        self.pokemons = []

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

class Player:
    def __init__(self, name):
        self.name = name
        self.team = Team()

    def choose_pokemon(self):
        print("\nChoose a Pokémon:")
        for i, pokemon in enumerate(self.team.pokemons):
            print(f"{i+1}. {pokemon.name} ({pokemon.type})")
        while True:
            try:
                choice = int(input("Enter the number of the Pokémon: ")) - 1
                if 0 <= choice < len(self.team.pokemons):
                    return self.team.pokemons[choice]
                else:
                    print("Invalid choice. Please select a valid Pokémon number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def choose_random_pokemon(self):
        return random.choice(self.team.pokemons)


class Opponent:
    def __init__(self, name):
        self.name = name
        self.team = Team()

    def choose_pokemon(self):
        # For the opponent, we'll just choose a random Pokémon from their team
        return random.choice(self.team.pokemons)


class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def fight(self, player_pokemon, opponent_pokemon):
        while player_pokemon.health > 0 and opponent_pokemon.health > 0:
            player_pokemon.display_health()
            opponent_pokemon.display_health()
            move1 = player_pokemon.choose_move()
            move2 = opponent_pokemon.choose_random_move()

            self.attack(player_pokemon, opponent_pokemon, move1)
            if opponent_pokemon.health <= 0:
                print(f"{opponent_pokemon.name} fainted!")
                if player_pokemon.health <= 0:
                    print(f"{player_pokemon.name} fainted!")
                    break

            if player_pokemon.health > 0:
                self.attack(opponent_pokemon, player_pokemon, move2)
                if player_pokemon.health <= 0:
                    print(f"{player_pokemon.name} fainted!")
                    if opponent_pokemon.health <= 0:
                        print(f"{opponent_pokemon.name} fainted!")
                        break

        if player_pokemon.health > 0 and opponent_pokemon.health <= 0:
            print(f"{player_pokemon.name} wins!")
            return player_pokemon
        elif opponent_pokemon.health > 0 and player_pokemon.health <= 0:
            print(f"{opponent_pokemon.name} wins!")
            return opponent_pokemon
        else:
            print("It's a tie!")
            return None

    def attack(self, attacker, defender, move):
        effectiveness = TYPE_EFFECTIVENESS[move.type][defender.type]
        damage = int(move.power * effectiveness)
        defender.health = max(defender.health - damage, 0)
        print(f"{attacker.name} used {move.name}! It's {effectiveness}x effective. {defender.name} has {defender.health} health left.")

class Level:
    def __init__(self, level_number):
        self.level_number = level_number

    def play_level(self, player):
        print(f"\nLevel {self.level_number} begins!")
        opponent = Opponent(f"Opponent {self.level_number}")
        opponent.team.add_pokemon(Pokemon("Charmander", "Fire", [Move("Ember", "Fire", 40), Move("Scratch", "Normal", 30)]))
        opponent.team.add_pokemon(Pokemon("Squirtle", "Water", [Move("Water Gun", "Water", 40), Move("Tackle", "Normal", 30)]))
        opponent.team.add_pokemon(Pokemon("Bulbasaur", "Grass", [Move("Vine Whip", "Grass", 45), Move("Tackle", "Normal", 30)]))
        opponent.team.add_pokemon(Pokemon("Geodude", "Ground", [Move("Rock Throw", "Ground", 50), Move("Tackle", "Normal", 30)]))
        opponent.team.add_pokemon(Pokemon("Gastly", "Ghost", [Move("Shadow Ball", "Ghost", 60), Move("Lick", "Ghost", 30)]))

        battle = Battle(player, opponent)
        player_pokemon = player.choose_pokemon()
        opponent_pokemon = opponent.choose_pokemon()
        battle.fight(player_pokemon, opponent_pokemon)


class Game:
    def __init__(self, player):
        self.player = player
        self.levels = [Level(1), Level(2), Level(3)]

    def start(self):
        print("Starting the Pokémon game!")
        for level in self.levels:
            level.play_level(self.player)


# Example usage
player = Player("Ash")
player.team.add_pokemon(Pokemon("Pikachu", "Electric", [Move("Thunder Shock", "Electric", 40), Move("Quick Attack", "Normal", 30)]))
player.team.add_pokemon(Pokemon("Charmander", "Fire", [Move("Ember", "Fire", 40), Move("Scratch", "Normal", 30)]))
player.team.add_pokemon(Pokemon("Squirtle", "Water", [Move("Water Gun", "Water", 40), Move("Tackle", "Normal", 30)]))
player.team.add_pokemon(Pokemon("Snorlax", "Normal", [Move("Body Slam", "Normal", 85), Move("Hyper Beam", "Normal", 150)]))
player.team.add_pokemon(Pokemon("Steelix", "Steel", [Move("Iron Tail", "Steel", 100), Move("Earthquake", "Ground", 100)]))
player.team.add_pokemon(Pokemon("Gengar", "Ghost", [Move("Shadow Ball", "Ghost", 80), Move("Lick", "Ghost", 30)]))

game = Game(player)
game.start()
