# We're doing shit step by step
# Two methods of doing imports 1. -- from <module> import <method> 2. import module first the call then call function
# import <module>
# <module>.function()

from pathtrial import Path
from converter_module import user_input
from find_max import max_number
import maths.finding_max
from maths import finding_max
from maths.finding_max import max_number

path = Path("maths")
print(path.exists())
finding_max.max_number()
maths.finding_max.max_number()



max_number()

user_input()
