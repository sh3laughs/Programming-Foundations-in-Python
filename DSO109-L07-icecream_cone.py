"""Practices code DSO109 from lesson 7."""
# DSO109 - Programming Foundations - Python
    # Lesson 7 - Standard Library

# Page 4 - Modules
pip install icecream
import icecream
# couldn't get import to work by itself, but managed to import the
    # module by installing it first.. not totally convinced this
    # was the right solution, though

icecream.scoop_icecream('small', 'sprinkles', 'chocolate', 'cherries')
icecream.scoop_icecream('large', 'peanuts')
# these won't work yet, keep getting this error and can't figure out
        # why yet:
    # AttributeError: module 'icecream.__version__' has no attribute
        # 'scoop_icecream'


    # alternate option to import function only
from icecream import scoop_icecream
# ImportError: cannot import name 'scoop_icecream' from
    # 'icecream.__version__' (/Applications/anaconda3/lib/python3.9/
    # site-packages/icecream/__version__.py)


    # next step from lesson, though I can't actually test since the
        # imports aren't working
scoop_icecream('small', 'sprinkles', 'chocolate', 'cherries')
# NameError: name 'scoop_icecream' is not defined
    # this error makes sense, given the import failed


    # assign an alias when importing afunction
from icecream import scoop_icecream as scoop
# ImportError: cannot import name 'scoop_icecream' from
    # 'icecream.__version__' (/Applications/anaconda3/lib/python3.9/
    # site-packages/icecream/__version__.py)


    # assign an alias when importing a module
import icecream as i
# imported (supposedly...)

    # alternate option to import all functions from a module
from icecream import *
# imported (supposedly...)

    # call imported function
scoop_icecream('small', 'sprinkles', 'chocolate', 'cherries')
# NameError: name 'scoop_icecream' is not defined
