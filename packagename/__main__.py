"""
This is the package's main module.
It should define a main function to be executed, representing execution of the
whole package.
"""


# ----------------
# external imports
# ----------------

import os
import csv
import numpy
import Stan_MCMC_engine   # imaginary module


# ----------------
# internal imports
# ----------------

# Import project variables (provided via __init__)
from . import INPUTS_PATH
from . import OUTPUTS_PATH

# Import project-specific modules
from . private import dataGetter
from . private import dataAnalyser
from . private import dataPresenter




def main():

    # -------------------------------------------------------------------------
    # This main function should only contain high-level code, executing the the
    # steps required for the package's logic, and delegating implementation
    # details to the package's specialised modules in a top-down manner.
    #
    # A good main function in this context should almost read like a table of
    # contents, redirecting to the specialised functions invoked.
    # -------------------------------------------------------------------------

  # Get data
    Data = dataGetter.run( INPUTS_PATH )

  # Analyse data (initialise with an appropriate MCMC Engine!)
    dataAnalyser.MCMCEngine = Stan_MCMC_engine
    Results = dataAnalyser.run( Data        )

  # Create report  from results
    reportCreator.run( Results, OUTPUTS_PATH )




if __name__ == '__main__':   main()
