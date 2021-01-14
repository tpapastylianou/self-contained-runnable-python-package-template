# This is the project's main configuration file.
#
# Add any variables you want to later import to your project, using normal
# python syntax.
#
# Any configuration variable you add here will later need to be imported and
# dealt with appropriately by the project's __init__ file.

import os

# Choose verbosity of output
VERBOSE  = True

# As an example, suppose our package is effectively an experiment, and we can
# choose here between two appropriate "MCMC Engines", e.g. let's say "stan" or
# "emcee".
#
# Obviously, in practice, the most useful thing to do from a configuration-file
# point of view at this stage would be to simply choose between assigning the
# string "stan" or "emcee" to this variable, and letting your __init__ file
# perform the appropriate initialisations accordingly.
#
# However, for the purposes of keeping the __init__.py as generic as possible
# for the sake of this template, for this example we will create an actual
# object (of trivial functionality) that can be imported and used later in our
# template without generating errors.
#
# This also shows how flexible this configuration file is; after all, all
# definitions created in this file are simply intended to be imported by
# __init__.py and made available to the rest of the package, as if this
# configuration file were a normal python module!

class Stan : run = lambda x: { 'stats': "Stats...", 'results': x }
class Emcee: run = lambda x: { 'stats': "Stats...", 'results': x }

MCMC_ENGINE = Stan


# Here, instead of defining an INPUTS_PATH variable that would be imported
# directly, we instead provide a function that is to be called by the
# __init__.py file, because we want to initialise these relative to the package
# root, which is not known until initialization time.
def get_inputs_path( PkgRoot ):   return os.path.join( PkgRoot, 'inputs' )

# Here we provide a function that __init__.py will use to generate an
# OUTPUTS_PATH variable, in the same way as with INPUTS_PATH above.
def get_outputs_path( PkgRoot ):   return os.path.join( PkgRoot, 'outputs' )
