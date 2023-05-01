import os
import requests
import random
from colorama import init, Fore, Back

init()

class PokemonGame:
    def __init__(self):
        self.pokemon = self.get_random_pokemon()
        self.max_attempts = 5
        self.attempts = 0

    def get_random_pokemon(self):
        pokemon_id = random.randint(1, 898)
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
        response = requests.get(url)

        if response.ok:
            pokemon_data = response.json()
            return pokemon_data['name']
        else:
            return None

    def ask_pokemon(self):
        while self.attempts < self.max_attempts:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
            print(f'Guess the Pokemon Im thinking of! It must have {len(self.pokemon)} letters.')
            pokemon_guess = input(f'Attempt {self.attempts + 1}/{self.max_attempts}. Enter a Pokemon: ')
            if len(pokemon_guess) != len(self.pokemon):
                print(f'Sorry, the Pokemon must have {len(self.pokemon)} letters.')
                input('Press enter to continue...')
            elif pokemon_guess.lower() == self.pokemon.lower():
                print('Correct! Thats the Pokemon I was thinking of!')
                break
            else:
                self.attempts += 1
                print(f'Sorry, thats not the Pokemon I was thinking of. Try again! You have {self.max_attempts - self.attempts} attempts left.')
                print(Fore.YELLOW + self.get_hint(pokemon_guess) + Fore.RESET)
                input('Press enter to continue...')

        if self.attempts == self.max_attempts:
            print(f'No more attempts left. The Pokemon I was thinking of was {self.pokemon}.')
            input('Press enter to continue...')

    def get_hint(self, pokemon_guess):
        hint = ''
        for i in range(len(self.pokemon)):
            if self.pokemon[i] == pokemon_guess[i]:
                hint += Back.GREEN + ' ' + pokemon_guess[i] + ' ' + Back.RESET + ' '
            elif pokemon_guess[i] in self.pokemon:
                hint += Back.YELLOW + ' ' + pokemon_guess[i] + ' ' + Back.RESET + ' '
            else:
                hint += Back.RED + ' ' + pokemon_guess[i] + ' ' + Back.RESET + ' '
        return hint

if __name__ == '__main__':
    game = PokemonGame()
    game.ask_pokemon()