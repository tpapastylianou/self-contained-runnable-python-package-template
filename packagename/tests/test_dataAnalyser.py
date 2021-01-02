import unittest
import numpy

from .. src . dataAnalyser import run
from .. src . dataAnalyser import run_mcmc

##############
### Unit Tests
##############

# -------------------
# 'run_mcmc' function
# -------------------

class Test_run_mcmc( unittest.TestCase ):

    def setUpClass    ():   print( "### Unit Tests for run_mcmc()" )
    def tearDownClass ():   print( )

    def test_01( self ):
        # -------------------------------------------------------------------
        "Check that the resulting dict contains 'stats' and a 'results' keys"
        # -------------------------------------------------------------------

        dataAnalyser.MCMCEngine = Mock_MCMC_Engine

        MCMCDict = dataAnalyser.run_mcmc( [1,2,3,4] )

        self.assertIn( 'stats'  , MCMCDict.keys() )
        self.assertIn( 'results', MCMCDict.keys() )



# --------------
# 'run' function
# --------------

# ... etc
