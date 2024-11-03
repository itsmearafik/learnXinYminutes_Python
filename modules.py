# Python modules are just ordinary python files. The name of the module is the name of the file.
# The local folder(file) has priority over Python's buitl-in libraries 

import math 
print(math.sqrt(16))

# importing specific functions from a module 
from math import ceil, floor 
print(ceil(3.7))
print(floor(3.7))

# importing all functions from a module using the * symbol 

from math import * 

# shortening module names using the keyword `as`
import math as m 
math.sqrt(16) == m.sqrt(16)

import math
print(dir(math))