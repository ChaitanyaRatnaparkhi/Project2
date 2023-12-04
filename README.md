# Project2

Chaitanya Ratnaparkhi cratnapa@stevens.edu

# GitHub repo 

URL : https://github.com/ChaitanyaRatnaparkhi/Project2.git

# Time

I Spent around 15 hours to complete this project.

# Bugs or issues

There was a bug while implementing code for ambigious inputs.

# resolved issues

I used filters to resolve it.

# 3 Extensions

3.1 A help verb which tells the players what the valid verbs are and we write ___ which indicates some target after the verb.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? help
You can run the following commands:
  go ...
  get ...
  look 
  inventory 
  quit 
  help 
What would you like to do? 

3.2 A drop verb Extension which is opposite of the verb get which will drop item in the room from inventory and we write ___ which indicates some target after the verb.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
What would you like to do? look
> A red room

This room is fancy. It's red!

Exits: north west

What would you like to do? go north
You go north.

> A green room

You are in a simple room, with bright green walls.

Exits: west south

What would you like to do? drop rose
You drop the rose.
What would you like to do? look
> A green room

You are in a simple room, with bright green walls.

Items: rose

Exits: west south

What would you like to do? 

3.3 Direction as verb

Even if we put 'East' instead of 'Go East' it will go east.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? e
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? s
There's no way to go south.
What would you like to do? go west
You go west.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? 