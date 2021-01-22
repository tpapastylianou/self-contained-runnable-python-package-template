# Package initialisation file.
#
# This file's role is to grab the relevant configuration preferences from
# /config/CONFIG.py and initialise the package.
#
# Do not add variables here that would be considered configuration parameters;
# only use this file to load the relevant configuration preferences from the
# CONFIG.py file, and to make them available to the other modules.

# To actually add/edit configuration options, edit the /config/CONFIG.py file
# directly (using normal python syntax), and then import / export here as
# needed.



#################################################################
### Initial imports and sanity checks required for initialization
#################################################################

import os

# Detect package directory, and use to create standard paths relative to package
# root.
PKGROOT    = os.path.abspath( os.path.dirname(  __file__ ) )
DOCPATH    = os.path.join( PKGROOT, 'doc' )

# ANSI colour escape codes (for use in logging/debug messages)
ANSI_RED    = '\033[91m';   ANSI_GREEN  = '\033[92m';   ANSI_ORANGE = '\033[93m';
ANSI_BLUE   = '\033[94m';   ANSI_PURPLE = '\033[95m';   ANSI_RESET  = '\033[39m';


# Check that we are running in the context of a python virtual env. This check
# is useful, e.g., when the package represents an experiment, and you want to
# ensure consistency/reproducibility between runs, in terms of what python
# packages/versions are installed and used in the experiment. It can be removed
# if this is not an issue for a particular package, or turned into a
# RuntimeError if you want to be more defensive about its presence.

if not os.getenv( 'VIRTUAL_ENV' ): print(
f"""{ANSI_PURPLE}

Warning: No suitable VIRTUAL_ENV environmental variable detected.

In order to ensure consistency / reproducibility between runs, you might want to
consider always running this package from within a suitable python virtual
environment, containing the python package versions specified in the package's
requirements.txt file.

{ANSI_RESET}""" )



############################
### Parse configuration file
############################

from . config import CONFIG

# Import all configuration constants
VERBOSE     = CONFIG.VERBOSE
MCMC_ENGINE = CONFIG.MCMC_ENGINE

# Some variables may need to be generated dynamically from the config:
INPUTS_PATH  = CONFIG.get_inputs_path ( PKGROOT )
OUTPUTS_PATH = CONFIG.get_outputs_path( PKGROOT )



######################
### Initialize package
######################

def printconfig( Varname, Var ):
    print(  f"{ANSI_BLUE}__init__: Setting {Varname} " +
            f"to {ANSI_ORANGE}{Var}{ANSI_RESET}"           )

if VERBOSE not in [ True, False ]:
    raise ValueError( 'Bad value given for VERBOSE environmental variable. Needs to be True or False.' )

if VERBOSE:
    printconfig( 'PKGROOT'     , PKGROOT      )
    printconfig( 'INPUTS_PATH' , INPUTS_PATH  )
    printconfig( 'OUTPUTS_PATH', OUTPUTS_PATH )
    printconfig( 'MCMC_ENGINE' , MCMC_ENGINE  )


__all__ = [
    'PKGROOT',
    'DOCPATH',
    'VERBOSE',

    'INPUTS_PATH',
    'OUTPUTS_PATH',
    'MCMC_ENGINE'
]

# Import package documentation (to avoid having to dump it all on the top of
# this file instead). You could follow a similar strategy in other modules if
# they are to contain significant documentation that would clutter the sources.
PkgDoc = os.path.join( DOCPATH, 'packagename.__doc__' )
with open( PkgDoc, 'r' ) as f:   __doc__ = f.read()
