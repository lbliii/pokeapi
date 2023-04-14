import json
import requests
from enum import Enum


class Noun(Enum):
    ABILITY = "ability"
    BERRY = "berry"
    BERRY_FIRMNESS = "berry-firmness"
    BERRY_FLAVOR = "berry-flavor"
    CHARACTERISTIC = "characteristic"
    CONTEST_EFFECT = "contest-effect"
    CONTEST_TYPE = "contest-type"
    EGG_GROUP = "egg-group"
    ENCOUNTER_CONDITION = "encounter-condition"
    ENCOUNTER_CONDITION_VALUE = "encounter-condition-value"
    ENCOUNTER_METHOD = "encounter-method"
    EVOLUTION_CHAIN = "evolution-chain"
    EVOLUTION_TRIGGER = "evolution-trigger"
    GENDER = "gender"
    GENERATION = "generation"
    GROWTH_RATE = "growth-rate"
    ITEM = "item"
    ITEM_ATTRIBUTE = "item-attribute"
    ITEM_CATEGORY = "item-category"
    ITEM_FLING_EFFECT = "item-fling-effect"
    ITEM_POCKET = "item-pocket"
    LANGUAGE = "language"
    LOCATION = "location"
    LOCATION_AREA = "location-area"
    MACHINE = "machine"
    MOVE = "move"
    MOVE_AILMENT = "move-ailment"
    MOVE_BATTLE_STYLE = "move-battle-style"
    MOVE_CATEGORY = "move-category"
    MOVE_DAMAGE_CLASS = "move-damage-class"
    MOVE_LEARN_METHOD = "move-learn-method"
    MOVE_TARGET = "move-target"
    NATURE = "nature"
    PAL_PARK_AREA = "pal-park-area"
    POKEATHLON_STAT = "pokeathlon-stat"
    POKEDEX = "pokedex"
    POKEMON = "pokemon"
    POKEMON_COLOR = "pokemon-color"
    POKEMON_FORM = "pokemon-form"
    POKEMON_HABITAT = "pokemon-habitat"
    POKEMON_SHAPE = "pokemon-shape"
    POKEMON_SPECIES = "pokemon-species"
    REGION = "region"
    STAT = "stat"
    SUPER_CONTEST_EFFECT = "super-contest-effect"
    TYPE = "type"
    VERSION = "version"
    VERSION_GROUP = "version-group"


class PokeAPI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/'

    def get(self, object: Noun, id_or_name=None):
        if id_or_name is None:
            url = self.base_url + f'{object.value}'
        else:
            url = self.base_url + f'{object.value}/{id_or_name}'
        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_sprite(self, pokemon_name: str, gender: str = None, position: str = None, generation: str = None, version: str = None, shiny: bool = False, all: bool = False):
        url = f'{self.base_url}pokemon/{pokemon_name}'
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            sprites = pokemon_data['sprites']

            match all:
                case True:
                    return sprites

            match (shiny, gender, position, generation, version):

                case(None, None, None, None, None):
                    return sprites.get('front_default')

                case(shiny, None, None, None, None):
                    if shiny is True:
                        return sprites.get('front_shiny')
                    else:
                        return sprites.get('front_default')

                case(shiny, gender, None, None, None):
                    if shiny and gender == 'male':
                        return sprites.get('front_shiny')
                    elif shiny and gender == 'female':
                        return sprites.get('front_shiny_female')
                    else:
                        return sprites.get('front_default')

                case(shiny, gender, position, None, None):
                    if shiny and gender == 'female' and position == 'back':
                        return sprites.get('back_shiny_female')
                    elif shiny and gender == 'female' and position == 'front':
                        return sprites.get('front_shiny_female')
                    elif shiny and gender == 'male' and position == 'back':
                        return sprites.get('back_shiny')
                    else:
                        return sprites.get('front_shiny')

                case(shiny, gender, position, generation, None):
                    # For generations after generation-iii, use the original logic
                    keys = sprites['versions'][generation].keys()
                    keyList = list(keys)
                    backupVersion = keyList[0]
                    path = sprites['versions'][generation][backupVersion]

                    if generation == 'generation-i' or 'generation-ii' or 'generation-iii':
                        if shiny and position == 'back':
                            sprite_url = path.get('back_shiny')
                        elif shiny and position == 'front':
                            sprite_url = path.get('front_shiny')
                        else:
                            sprite_url = path.get('front_default')
                    else:

                        if shiny and gender == 'female' and position == 'back':
                            sprite_url = path.get('back_shiny_female')
                        elif shiny and gender == 'female' and position == 'front':
                            sprite_url = path.get('front_shiny_female')
                        elif shiny and gender == 'male' and position == 'back':
                            sprite_url = path.get('back_shiny')
                        else:
                            sprite_url = path.get('front_shiny')

                case(shiny, gender, position, generation, version):
                    path = sprites['versions'][generation][version]

                    if shiny and generation == 'generation-i':
                        if position == 'back':
                            sprite_url = path.get('back_default')
                        elif position == 'front':
                            sprite_url = path.get('front_default')
                    elif not shiny and generation == 'generation-i':
                        if position == 'back':
                            sprite_url = path.get('back_default')
                        else:
                            sprite_url = path.get('front_default')

                    if generation == 'generation-ii' or 'generation-iii':
                        path = sprites['versions'][generation][version]
                        if shiny and position == 'back':
                            sprite_url = path.get('back_shiny')
                        elif shiny and position == 'front':
                            sprite_url = path.get('front_shiny')
                        else:
                            sprite_url = path.get('front_default')
                    else:

                        if shiny and gender == 'female' and position == 'back':
                            sprite_url = path.get('back_shiny_female')
                        if shiny and gender == 'female' and position == 'front':
                            sprite_url = path.get('front_shiny_female')
                        if not shiny and gender == 'female' and position == 'back':
                            sprite_url = path.get('back_female')
                        if not shiny and gender == 'female' and position == 'front':
                            sprite_url = path.get('front_female')
                        if shiny and gender == 'male' and position == 'back':
                            sprite_url = path.get('back_shiny')
                        if shiny and gender == 'male' and position == 'front':
                            sprite_url = path.get('front_shiny')
                        if not shiny and gender == 'male' and position == 'back':
                            sprite_url = path.get('back_default')
                        if not shiny and gender == 'male' and position == 'front':
                            sprite_url = path.get('front_default')
            print("Looking for pokemon...")
            return sprite_url
        else:
            return None


pdx = PokeAPI()


pikachu = pdx.get_sprite('pikachu',
    shiny=True,
    gender="male",
    position="front",
    generation="generation-ii",
    # version="yellow"
    )

print(pikachu)
# save
# with open('pikachu.json', 'w') as f:
#     json.dump(pikachu, f)
