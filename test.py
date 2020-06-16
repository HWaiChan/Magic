from TheWorld import *
from Props import Wizard

the_world = TheWorld()
# Spawn weird Wizards

#Carl = Wizard(0, (0, 0))  # Lightning Steam boy
#Bob = Wizard(0, (0, 0))  # Magicka pro
#Jim = Wizard(0, (0, 0))  # Don't talk to him, he will murder you
#Fred = Wizard(0, (0, 0))  # he do a thing
Jeb = Wizard(0, (0, 0))
#the_world.add_prop(Carl, (6, 8))
#the_world.add_prop(Jim, (6, 6))
#the_world.add_prop(Bob, (6, 8))
#the_world.add_prop(Fred, (1, 2))
the_world.add_prop(Jeb, (4, 4))

# Thundercloud
#Carl.shout('Cold 1 Create Square 3 Point -3 -1 Mana 25 And'
           #' Fire 1 Create Square 3 Self Mana 25 And'
           #' Lightning 2 Create Square 3 Self Mana 25')

# Rock Throwing
#Bob.shout('Earth 2 Create Square 1 Self Mana 25 And Earth 3 Displace 35 Square 1 Self Mana 25')

# Gravity Slingshot
#Jim.shout('Force 2 Create 0 Square 1 Point 1 1 Mana 25')

# KNOCKBACK FIREBALL
#Fred.shout('Fire 3 Create Square 1 Self Mana 25 Concentrate And '
           #'Fire 4 Displace 55 Square 1 Self Mana 25 '
           #'Then Fire 3 Create Square 3 Self Mana 25 Then Force 1 Create Square 3 Self Mana 25')

the_world.tiles[4][4].state["Rate_of_Time"] = 4
Jeb.mana = 1000
Jeb.shout('Fire 3 Create Square 1 Point -1 -1 Mana 25')
the_world.resolve_tiles()
Jeb.shout('Fire 3 Create Square 1 Point 1 1 Mana 25')
the_world.print_props_grid()
Jeb.shout('Fire 3 Create Square 1 Point -1 1 Mana 25')
the_world.resolve_tiles()
the_world.print_props_grid()
Jeb.shout('Fire 3 Create Square 1 Point 1 -1 Mana 25')
the_world.resolve_tiles()
the_world.print_props_grid()
the_world.resolve_tiles()
the_world.print_props_grid()
the_world.resolve_tiles()
the_world.print_props_grid()

#print("Jim HP: " + str(Jim.health))
#print("Jim Mana: " + str(Jim.mana))
#print("Is Jim walking: " + str(Jim.velocity))
#print("Is Carl getting yeeted: " + str(Carl.velocity))
#print("Carl HP: " + str(Carl.health))
#print("Carl Mana: " + str(Carl.mana))
#print("Bob HP: " + str(Bob.health))
#print("Bob Mana: " + str(Bob.mana))
