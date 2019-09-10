from TheWorld import *
from Props import Wizard

the_world = TheWorld()

Carl = Wizard(0, (0, 0))
Bob = Wizard(0, (0, 0))
Jim = Wizard(0, (0, 0))
the_world.tiles[5][5].props.append(Carl)
the_world.tiles[5][7].props.append(Jim)
the_world.tiles[6][8].props.append(Bob)
Carl.shout('Cold 1 Create Square 3 Point -3 -1')
Carl.shout('Fire 2 Create Rectangle 3 Point -3 -1')
Carl.shout('Lightning 2 Create Square 3 Point -3 -1')
Bob.shout('Earth 2 Create Square 1 Self')
Bob.shout('Earth 3 Displace 35 Square 1 Self')
the_world.resolve_tiles()
the_world.print_elements_grid()
the_world.print_props_grid()
print("Jim HP: " + str(Jim.health))
print("Carl HP: " + str(Carl.health))
print("Bob HP: " + str(Bob.health))




