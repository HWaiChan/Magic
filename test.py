from TheWorld import *
from Props import Wizard

the_world = TheWorld()

Carl = Wizard('N', 0)
Bob = Wizard('N', 0)
Jim = Wizard('N', 0)
the_world.tiles[5][5].props.append(Carl)
the_world.tiles[4][7].props.append(Jim)
the_world.tiles[5][7].props.append(Bob)
Carl.shout('Cold 1 Create Square 3 Self')
Carl.shout('Fire 2 Create Rectangle 3 Self')
Carl.shout('Lightning 2 Create Square 3 Self')
Bob.shout('Earth 2 Create Square 1 Self')
Bob.shout('Earth 2 Displace Square 1 Point')
the_world.resolve_tiles()
the_world.print_elements_grid()
the_world.print_props_grid()
print("Jim HP: " + str(Jim.health))
print("Carl HP: " + str(Carl.health))
print("Bob HP: " + str(Bob.health))




