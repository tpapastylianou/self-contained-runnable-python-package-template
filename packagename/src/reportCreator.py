"""
- This is a 'functional' module, meaning it has a single 'run' function, acting
  as the module's main point of call, and carrying out the module's core
  responsibility.

- Functional modules may require 'initialization' by the caller before use.
  Typically this involves assigning to variables at module-global scope before
  running it. If such initialization is required, all functions
  relying on it should conduct appropriate checks to ensure this
  has been performed correctly.

This is an example functional module responsible for creating reports from
results. This particular module does not require initialization before use.
"""

# ----------------
# external imports
# ----------------

import os
import nbformat   # for programmatic creation of jupyter notebooks
                  # e.g. see: https://stackoverflow.com/a/62105736/4183191


# ----------------
# internal imports
# ----------------

None


# -------------------------------------------------------
# module variables requiring initialisation by the caller
# -------------------------------------------------------

None



####################
### Primary function
####################

def run( Data, OutputsPath ):
    """
    Create a report (e.g. jupyter notebook format)
    """

  # ... report code goes here. e.g.:
    nb = nbformat.v4.new_notebook()
    nb['cells'] = [
                    nbformat.v4.new_markdown_cell( "The Result was:" ),
                    nbformat.v4.new_code_cell( repr( Data.tolist() ) )
                  ]
    OutputFile = os.path.join( OutputsPath, 'output.ipynb' )
    with open( OutputFile, 'w') as f:   nbformat.write(nb, f)
