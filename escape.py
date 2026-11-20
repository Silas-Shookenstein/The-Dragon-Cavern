import random

rooms = {
    "Inner Cave": {"pathways": {"s": "The Pit", "w": "Underground Lake"}, "open_with": ""},
    "The Pit": {"pathways": {"w": "Inner Cave", "a": "The Bridge", "s": "Dark Cavern"}, "open_with": "Torch"},
    "Dark Cavern": {"pathways": {"w": "The Pit"}, "open_with": "Torch"},
    "Outter Cave": {"pathways": {"d": "The Pit", "w": "Dragon"}, "open_with": ""},
    "Outside": {"pathways": {"s": "Dragon"}, "open_with": ""},
    "The Bridge": {"pathways": {"a": "Outter Cave", "d": "The Pit"}, "open_with": ""},
    "Underground Lake": {"pathways": {"s": "Inner Cave"}, "open_with": ""},
    "Dragon": {"pathways": {"w": "Outside", "s": "Outter Cave"}, "open_with": "Sword"}
}

pickable_objects = {
    "Torch": {"location": "Underground Lake", "picked": False},
    "Sword": {"location": "Dark Cavern", "picked": False}
}

START_LOCATION = "Inner Cave"

def print_location(location: str) -> None:
    if location in rooms:
        print(f"You are in the {location}.")
    else:
        print("Unknown location.")

def get_directions(location: str) -> dict[str, str]:
    if location in rooms:
        return rooms[location]["pathways"]
    else:
        return {}


def find_room_by_direction(location: str, direction: str) -> str:
    if location not in rooms:
        print("Unknown location.")
        return location
    elif direction in rooms[location]["pathways"]:
        new_loc = rooms[location]["pathways"][direction]
        return new_loc
    else:
        print("Invalid direction. Try again.")
        return location

def has_key_for_room(room_id: str) -> bool:
    if room_id not in rooms:
        return False
    required_key = rooms.get(room_id, {}).get("open_with", "")
    if required_key == "":
        return True
    if required_key in pickable_objects:
        return pickable_objects[required_key]["picked"]
    return False

    
def explore_room(location: str) -> None:
    for key, val in pickable_objects.items():
        if val["location"] == location and val["picked"] == False:
            val["picked"] = True
            print(f"You found {key}.")

def enemy_ai(hp: int, php: int) -> bool:
    while hp > 0:
        print(f"Dragon HP: {hp}")
        print(f"Your HP: {php}")
        atch = random.randint(1, 10)
        if 2 > atch >= 1:
            print("The Dragon slashes with its claws! You take 1 damage!")
            php -= 1
        if 5 > atch >= 2:
            print("The Dragon yawns. It looks cute.")
        if 9 > atch >= 5:
            print("The Dragon blinks. It looks silly.")
        if atch >= 9:
            print("The Dragon spews fire! It deals 2 damage.")
            php -= 2

        plat = str(input("Press f to attack! ").lower())
        match plat:
            case "f":
                hp -= 1
            case "pacify":
                paci = random.randint(1, 10)
                if paci == 3:
                    print("The Dragon was pacified!")
                    return True
            case _:
                print("You stubbed your toe in your confusion and lost a turn!")
        if php == 0:
            print("You fainted and are dragged back to the depths of the mountain.")
            for key, val in pickable_objects.items():
                if val["picked"] == True:
                    val["picked"] = False
                    print(f"{key} has been stolen again!")
            return False
        if hp == 0:
            return True
    return False
        



def game_loop(location: str) -> None:
    while True:    
        print_location(location)
        explore_room(location)
        available_directions = get_directions(location)
        print(f"You can go: {available_directions}")
        chosen_direction = input("Where do you want to go? ('x' to exit) ").lower()
        if chosen_direction  == 'x':
            print("Exited the game.")
            break
        
        next_room = find_room_by_direction(location, chosen_direction)
        if has_key_for_room(next_room):
            location = next_room
        else:
            print("You don't have the correct item to enter this room.")
        if location == "Dragon":
            dragon = enemy_ai(10, 10)
            if dragon == False:
                location = "Inner Cave"
            if dragon == True:
                location = "Outside"
        
        if location == "Outside":
            print("You've defeated the dragon and escaped!")
            break


def start_game() -> None:

    print("The Dragon's Cavern")
    print("You are an adventurer who has been taken by a dragon to its cave. You must find a sword somewhere in the cave... but it's too dark, maybe there's a torch nearby?")

if __name__ == "__main__":
    start_game()
    game_loop(START_LOCATION)