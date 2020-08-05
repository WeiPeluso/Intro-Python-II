from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("wei peluso", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# Declare current room
print(player1.room.name)
curr_room = player1.room

while True:
    print(player1)
    command = input(
        "please enter the command, n for north, s for south, e for east, w for west , q for quit:  ")
    if (command == 'q'):
        break
    elif (command == 'n'):
        try:
            curr_room = player1.room.n_to
            player1.room = curr_room
            print(f"You are in room : {curr_room}")
        except AttributeError:
            print(f'\n{player1.name} turned north and ran into a dead end!')
    elif (command == 'w'):
        try:
            curr_room = player1.room.w_to
            player1.room = curr_room
            print(f"You are in room : {curr_room}")
        except AttributeError:
            print(f'\n{player1.name} turned west and ran into a dead end!')
    elif (command == 'e'):
        try:
            curr_room = player1.room.e_to
            player1.room = curr_room
            print(f"You are in room : {curr_room}")
        except AttributeError:
            print(f'\n{player1.name} turned east and ran into a dead end!')
    elif (command == 's'):
        try:
            curr_room = player1.room.s_to
            player1.room = curr_room
            print(f"You are in room : {curr_room}")
        except AttributeError:
            print(f'\n{player1.name} turned south and ran into a dead end!')
