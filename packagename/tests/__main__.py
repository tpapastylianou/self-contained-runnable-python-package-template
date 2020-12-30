"""
This is the __main__ module for the package.tests module / subpackage.

In the same way that the core package itself is executable, the package.tests
package is executable too in the same manner, simply by providing its own
__main__ module.

It can be run independently of the core package, e.g. as

    python3 -m packagename.tests

This file's role is to simply discover all tests in this folder and run them.

Alternatively, you could do this yourself from the linux terminal by
issuing the following command:

    python3 -m unittest discover -s packagename.tests -v
"""

import unittest
import os

from .. import PKGROOT

PkgName = os.path.basename( PKGROOT )
TestDir = PkgName + '.tests'




def main():

    Tests  = unittest.defaultTestLoader.discover( start_dir = TestDir )
    Runner = unittest.TextTestRunner( descriptions = True ,
                                      verbosity    = 2    ,
                                      failfast     = False   )
    Runner.run( Tests )



if __name__ == '__main__': main()
