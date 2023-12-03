import json
import sys

class adv():
    def __init__(self, mapPath):
        self.load_map(mapPath)
        self.current_room_id = 0
        self.inventory = []
        self.verb_list = ['go', 'look', 'get', 'drop', 'inventory', 'quit', 'help']
    def load_map(self, mapPath):
        with open(mapPath) as file:
            self.rooms = json.load(file)

    def display_room(self):
        room = self.rooms[self.current_room_id]
        print(f"> {room['name']}\n\n{room['desc']}")
        if 'items' in room and len(room['items']) > 0:
            print(f"\nItems: {', '.join(room['items'])}")
        print(f"\nExits: {' '.join(room['exits'])}\n")

    def go(self, direction):
        '''
        Use this keyword to go to any other room. Usage: go ___
        '''
        direction = direction.lower()
        room = self.rooms[self.current_room_id]
        possible_matches = [d for d in room['exits'] if d.startswith(direction)]

        if direction in room['exits']:
            self.current_room_id = room['exits'][direction]
            print("You go "+direction+".\n")
            self.display_room()
        elif len(possible_matches) == 1:
            self.current_room_id = room['exits'][possible_matches[0]]
            print("You go "+direction+".\n")
            self.display_room()
        elif len(possible_matches) > 1:
            last_word = possible_matches[-1]
            words_till_last = possible_matches[0:-1]

            print(f"Did you want to go {', '.join(words_till_last)} or {last_word}?")
        else:
            print(f"There's no way to go {direction}.")

    def look(self):
        '''
        Use this keyword to look in which room you are. Usage: look ___
        '''
        self.display_room()

    def get(self, item):
        room = self.rooms[self.current_room_id]
        possible_matches = [i for i in room.get('items', []) if i.startswith(item)]
        if item == None:
            print("Sorry, you need to 'get' something.")
            return
        if len(possible_matches) == 1:
            item = possible_matches[0]
            self.inventory.insert(0,item)
            room['items'].remove(item)
            print(f"You pick up the {item}.")
        elif len(possible_matches) > 1:
            last_word = possible_matches[-1]
            words_till_last = possible_matches[0:-1]
            print(f"Did you want to get the {', '.join(words_till_last)} or the {last_word}?")
        else:
            print(f"There's no {item} anywhere.")

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
            print("You're not carrying anything.")

    def help(self):
        print("You can run the following commands:")

        for verb in self.verb_list:
            func = getattr(adv,verb,None)
            if func:

                print(f"  {verb:10} {func.__doc__.strip()}")
                
    def handle_direction(self,input_verb):
        room = self.rooms[self.current_room_id]
        possible_directions = list(filter(lambda x: input_verb in x,room['exits'] ))
        # print(possible_directions)
        if len(possible_directions) > 0:
            self.go(input_verb)
            
        else:
            print("Invalid command. Type 'help' for available commands.\n")

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
            if target == None:
                print("Sorry, you need to 'go' somewhere.")
                continue
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
            adventure.handle_direction(verb)
            
if __name__ == "__main__":
    main()
