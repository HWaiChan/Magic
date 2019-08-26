from TheWorld import *
from Props import Wizard

the_world = TheWorld()

Carl = Wizard('N', 0)
Bob = Wizard('N', 0)
the_world.tiles[5][5].props.append(Carl)
the_world.tiles[5][7].props.append(Bob)
Carl.shout('Cold 1 Create Square 3 Self 1')
Carl.shout('Earth 2 Create Rectangle 3 Self 1')
Carl.shout('Lightning 2 Create Square 3 Self 1')
Bob.shout('Earth 2 Create Rectangle 1 Point 5')
the_world.resolve_tiles()
the_world.print_elements_grid()
the_world.print_props_grid()
print(the_world.get_total_elements())



