import json
import sys

class adv():
    def __init__(self, mapPath):
        self.load_map(mapPath)
        self.current_room_id = 0
        self.inventory = []

    def load_map(self, mapPath):
        with open(mapPath) as file:
            self.rooms = json.load(file)

    def display_room(self):
        room = self.rooms[self.current_room_id]
        print(f"> {room['name']}\n\n{room['desc']}")
        if 'items' in room and len(room['items']) > 0:
            print(f"Items: {', '.join(room['items'])}")
        print(f"\nExits: {', '.join(room['exits'])}\n")

    def go(self, direction):
        room = self.rooms[self.current_room_id]
        possible_matches = [d for d in room['exits'] if d.startswith(direction)]

        if direction in room['exits']:
            self.current_room_id = room['exits'][direction]
            self.display_room()
        elif len(possible_matches) == 1:
            self.current_room_id = room['exits'][possible_matches[0]]
            self.display_room()
        elif len(possible_matches) > 1:
            print(f"Did you want to go {', '.join(possible_matches)}?")
        else:
            print(f"There's no way to go {direction}.\n")

    def look(self):
        self.display_room()

    def get(self, item):
        room = self.rooms[self.current_room_id]
        possible_matches = [i for i in room.get('items', []) if i.startswith(item)]

        if len(possible_matches) == 1:
            item = possible_matches[0]
            self.inventory.append(item)
            room['items'].remove(item)
            print(f"You pick up the {item}.\n")
        elif len(possible_matches) > 1:
            print(f"Did you want to get {', '.join(possible_matches)}?")
        else:
            print(f"There's no {item} anywhere.\n")

    def drop(self, item):
        room = self.rooms[self.current_room_id]
        if item in self.inventory:
            if 'items' in room:
                room['items'].append(item)
            else:
                room['items'] = [item]
            print("Successfully dropped " + item)
        else:
            print("No item " + item + " in inventory to drop.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(f"  {item}")
        else:
            print("You're not carrying anything.\n")

    def help(self):
        print("You can run the following commands:")
        for verb in ['go', 'look', 'get', 'drop', 'inventory', 'quit', 'help']:
            print(f"  {verb} ...")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)
    
    adventure = adv(sys.argv[1])
    adventure.display_room()

    verb_abbreviations = {'go': ['g'], 'look': ['l'], 'get': ['g'], 'drop': ['d'], 'inventory': ['i'], 'help': ['h']}

    while True:
        user_input = input("What would you like to do? ").strip().split()
        if not user_input:
            continue
        
        verb = user_input[0].lower()
        target = user_input[1] if len(user_input) > 1 else None

        for full_verb, abbreviations in verb_abbreviations.items():
            if verb in abbreviations or verb == full_verb:
                verb = full_verb
                break

        if verb == 'go':
            adventure.go(target)
        elif verb == 'look':
            adventure.look()
        elif verb == 'get':
            adventure.get(target)
        elif verb == 'drop':
            adventure.drop(target)    
        elif verb == 'inventory':
            adventure.show_inventory()
        elif verb == 'help':
            adventure.help()
        elif verb == 'quit':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid command. Type 'help' for available commands.\n")

if __name__ == "__main__":
    main()
