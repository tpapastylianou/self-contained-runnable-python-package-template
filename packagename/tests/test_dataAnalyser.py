import unittest, unittest.mock
import numpy

# Module under test
from .. src import dataAnalyser


# --------------------------------------------------------
# Print a nice header identifying the module under testing
# --------------------------------------------------------

class Test_( unittest.TestCase ):   # Note: the name 'Test_' guarantees
                                    # (alphabetically) this TestCase is run
                                    # before other TestCases in this module

    def setUpClass():
        print(                                                          )
        print( "******************************************************" )
        print( "*** Unit tests for packagename.src.dataAnalyser module" )
        print( "******************************************************" )
        print(                                                          )
    def tearDownClass ():   print( )


  # add dummy test so that the testcase is picked up during discovery
    def test_( self ): pass



##############
### Unit Tests
##############

# -------------------
# 'run_mcmc' function
# -------------------

class Test_run_mcmc( unittest.TestCase ):

    def setUpClass    ():   print( "### 'run_mcmc' tests:" )
    def tearDownClass ():   print( )


    def test_01( self ):
        # -----------------------------------------------------------------------------------------------------------
        "Check that an exception is raised correctly if the returned dict does not contain 'stats' or 'results' keys"
        # -----------------------------------------------------------------------------------------------------------

        Mock_MCMC_Engine1     = unittest.mock.Mock()
        Mock_MCMC_Engine1.run = lambda x: { 'stats' : "Stats", 'notresults' : "Results" }

        Mock_MCMC_Engine2     = unittest.mock.Mock()
        Mock_MCMC_Engine2.run = lambda x: { 'notstats' : "Stats", 'results' : "Results" }

        with self.assertRaises( AssertionError ):
            dataAnalyser.MCMCEngine = Mock_MCMC_Engine1;   dataAnalyser.run_mcmc( [1,2,3,4] )
            dataAnalyser.MCMCEngine = Mock_MCMC_Engine2;   dataAnalyser.run_mcmc( [1,2,3,4] )



# --------------
# 'run' function
# --------------

class Test_run( unittest.TestCase ):

    def setUpClass    ():   print( "### 'run' tests:" )
    def tearDownClass ():   print( )


    def test_01( self ):
        # ---------------------------------------------------------------------------------
        "Check that an exception is raised correctly if the MCMC Engine is not initialised"
        # ---------------------------------------------------------------------------------

        Data = numpy.array( [1,2,3,4,5] )
        dataAnalyser.MCMCEngine = None
        with self.assertRaises( AssertionError ): dataAnalyser.run( Data )




# ... etc
