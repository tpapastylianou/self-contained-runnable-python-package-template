"""
- This is a 'functional' module, meaning it has a single 'run' function, acting
  as the module's main point of call, and carrying out the module's core
  responsibility.

- Functional modules may require 'initialization' by the caller before use.
  Typically this involves assigning to variables at module-global scope before
  running it. If such initialization is required, all functions
  relying on it should conduct appropriate checks to ensure this
  has been performed correctly.

This is an example functional module responsible for analysing data.
This particular module requires initialization before use.
"""

# ----------------
# external imports
# ----------------

import os
import numpy


# ----------------
# internal imports
# ----------------

from .. import INPUTS_PATH


# -------------------------------------------------------
# module variables requiring initialisation by the caller
# -------------------------------------------------------

MCMCEngine = None   # This variable would need to be assigned a value
                    # by the caller, before running any function in this file.
                    #
                    # Obviously this could have been provided as an input to the
                    # run function directly instead. Or it could be left as a
                    # module-global function here, but left up to the 'run'
                    # function to initialise internally.
                    #
                    # However, there are advantages to having such an
                    # initialization requirement. E.g. one could call helper
                    # functions without requiring the 'run' function to be
                    # called first.
                    #
                    # This is particularly useful for unit tests, since it
                    # allows for dependence on other functions to be cut.


# -----------------------------
# other module-global variables
# -----------------------------

MCMCStats = None   # Contrary to the MCMCEngine variable above, which should be
                   # initialised by the caller, and is expected to be read-only,
                   # this variable is for internal use, and can be writeable.
                   #
                   # Any function that needs to write to this
                   # module-global variable should therefore explicitly state it
                   # as a 'global' variable, otherwise python will complain
                   # about trying to "reference a variable before assignment".
                   #
                   # Apart from the fact that they provide a common interface
                   # for all helper functions, such module-global variables may
                   # also be useful for making things available back to the
                   # caller.



####################
### Primary function
####################

def run( Data ):
    """
    Analyse the data
    """

    assert MCMCEngine, "'MCMCEngine' module variable needs to be explicitly set by the caller before running this function."
    global MCMCStats

    MCMCDict  = run_mcmc( Data )
    MCMCStats = MCMCDict[ 'stats' ]

    return MCMCDict[ 'results' ]




def run_mcmc( Data ):

    assert MCMCEngine, "'MCMCEngine' module variable needs to be explicitly set by the caller before running this function."

    MCMCDict = MCMCEngine.run( Data )

    return MCMCDict
