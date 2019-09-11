from TheWorld import *
from Props import Wizard

the_world = TheWorld()

Carl = Wizard(0, (0, 0))
Bob = Wizard(0, (0, 0))
Jim = Wizard(0, (0, 0))
Jim.movement((1, 1))
the_world.tiles[5][5].props.append(Carl)
the_world.tiles[5][7].props.append(Jim)
the_world.tiles[6][8].props.append(Bob)
Carl.shout('Cold 1 Create Square 3 Point -3 -1 Mana 25')
Carl.shout('Fire 2 Create Rectangle 3 Point -3 -1 Mana 25')
Carl.shout('Lightning 2 Create Square 3 Point -3 -1 Mana 25')
Bob.shout('Earth 2 Create Square 1 Self Mana 25')
Bob.shout('Earth 3 Displace 35 Square 1 Self Mana 25')
the_world.resolve_tiles()
the_world.resolve_tiles()
the_world.print_elements_grid()
the_world.print_props_grid()
print("Jim HP: " + str(Jim.health))
print("Jim Mana: " + str(Jim.mana))
print("Carl HP: " + str(Carl.health))
print("Carl Mana: " + str(Carl.mana))
print("Bob HP: " + str(Bob.health))
print("Bob Mana: " + str(Bob.mana))




