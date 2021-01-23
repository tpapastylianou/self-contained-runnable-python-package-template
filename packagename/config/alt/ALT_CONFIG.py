## This is an example of an alternate configuration file that could be chosen
## at launch time by passing a --config option, e.g,.
##
##     python3 -m packagename --config packagename/config/alt/ALT_CONFIG.py
##
## Compare with the default CONFIG.py file in the parent folder to see the
## configuration differences

import os

VERBOSE  = False   # default was True

class Stan : run = lambda x: { 'stats': "Stats...", 'results': x }
class Emcee: run = lambda x: { 'stats': "Stats...", 'results': x }

MCMC_ENGINE = Emcee   # default was Stan

def get_inputs_path( PkgRoot ):   return os.path.join( PkgRoot, 'inputs' )

def get_outputs_path( PkgRoot ):  return os.path.abspath( '' )   # i.e. dump
                                                                 # output in the
                                                                 # current path
                                                                 # instead.
