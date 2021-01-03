# Package initialisation file.
#
# This file's role is to grab the relevant configuration preferences from the
# CONFIG.ME file and initialise the package.
#
# Do not add variables here that would be considered configuration parameters;
# only use this file to load the relevant configuration preferences from the
# CONFIG.ME file, and to make them available to the other modules.

# To actually add/edit configuration options, edit the CONFIG.ME file directly
# (using normal python syntax), and then import / export here as needed.


import os

PKGROOT = os.path.abspath( os.path.dirname(  __file__ ) )
DOCPATH = os.path.join( PKGROOT, 'doc' )

ANSICOLOR_LIGHTBLUE   = "\033[94m"
ANSICOLOR_LIGHTORANGE = "\033[93m"
ANSICOLOR_RESET       = "\033[39m"


############################
### Parse configuration file
############################

# In order to load this configuration file as a python module, we need to create
# a symbolic link with a .py extension instead. We will unlink this after we
# have imported everything we wanted from this configuration file.

os.symlink( os.path.join( PKGROOT, 'CONFIG.ME' ),
            os.path.join( PKGROOT, 'CONFIG.py' )  )

# Import all configuration constants
from . CONFIG import INPUTS_PATH
from . CONFIG import OUTPUTS_PATH
from . CONFIG import VERBOSE
from . CONFIG import MCMC_ENGINE

# Remove the temporary symlink we created to the CONFIG.ME file
os.unlink( os.path.join( PKGROOT, 'CONFIG.py' ) )



######################
### Initialize package
######################

if VERBOSE not in [ True, False ]:
    raise ValueError( 'Bad value given for VERBOSE environmental variable. Needs to be True or False.' )

if VERBOSE:
    print( f"{ANSICOLOR_LIGHTBLUE}__init__: Setting PKGROOT to {ANSICOLOR_LIGHTORANGE}{PKGROOT}{ANSICOLOR_RESET}"           )
    print( f"{ANSICOLOR_LIGHTBLUE}__init__: Setting INPUTS_PATH to {ANSICOLOR_LIGHTORANGE}{INPUTS_PATH}{ANSICOLOR_RESET}"   )
    print( f"{ANSICOLOR_LIGHTBLUE}__init__: Setting OUTPUTS_PATH to {ANSICOLOR_LIGHTORANGE}{OUTPUTS_PATH}{ANSICOLOR_RESET}" )
    print( f"{ANSICOLOR_LIGHTBLUE}__init__: Setting MCMC_ENGINE to {ANSICOLOR_LIGHTORANGE}{MCMC_ENGINE}{ANSICOLOR_RESET}"   )


__all__ = [
    'PKGROOT',
    'DOCPATH',
    'INPUTS_PATH',
    'OUTPUTS_PATH',
    'MCMC_ENGINE',
    'VERBOSE'
]

# Import package documentation (to avoid having to dump it all on the top of
# this file instead). You could follow a similar strategy in other modules if
# they are to contain significant documentation that would clutter the sources.
PkgDoc = os.path.join( DOCPATH, 'packagename.txt' )
with open( PkgDoc, 'r' ) as f:   __doc__ = f.read()
