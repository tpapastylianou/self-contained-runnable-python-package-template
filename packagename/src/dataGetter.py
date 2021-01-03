"""
- This is a 'functional' module, meaning it has a single 'run' function, acting
  as the module's main point of call, and carrying out the module's core
  responsibility.

- Functional modules may require 'initialization' by the caller before use.
  Typically this involves assigning to variables at module-global scope before
  running it. If such initialization is required, all functions
  relying on it should conduct appropriate checks to ensure this
  has been performed correctly.

This is an example functional module responsible for collecting and
preparing data. This particular module does not require initialization.
"""

# ----------------
# external imports
# ----------------

import os
import csv
import numpy


# ----------------
# internal imports
# ----------------

from .. import INPUTS_PATH


# -------------------------------------------------------
# module variables requiring initialisation by the caller
# -------------------------------------------------------

None



####################
### Primary function
####################

def run( InputsPath : str = None):
    """
    Get the data and preprocess it appropriately
    """

    if InputsPath is None:   InputsPath = INPUTS_PATH

    Headers, RawData = get_raw_data( InputsPath )
    PreprocessedData = preprocess_data( RawData )

    return PreprocessedData



####################
### Helper functions
####################

def get_raw_data( InputsPath : str ):
    """
    Get the data from the data.csv file inside the folder
    """

    Inputfile = os.path.abspath( os.path.join( InputsPath, 'data.csv' ) )
    CsvFile   = open( Inputfile, 'r' )
    CsvReader = csv.reader( CsvFile )
    CsvData   = list( CsvReader )
    Headers   = CsvData[0]
    RawData   = CsvData[1:]

    CsvFile.close()

    return Headers, RawData




def preprocess_data( RawData ):
    """
    Preprocess data using method X by Y et al.
    """

  # Preprocess the data
    PreprocessedData = []
    for Row in RawData:
        PreprocessedData.append( [numpy.float( i ) for i in Row] )   # convert csv string to numpy float
    PreprocessedData = numpy.array( PreprocessedData )

    return PreprocessedData
