# co2syspy

[![Travis-CI Build Status](https://travis-ci.org/brews/co2syspy.svg?branch=master)](https://travis-ci.org/brews/co2syspy)
[![Coverage Status](https://coveralls.io/repos/github/brews/co2syspy/badge.svg?branch=master)](https://coveralls.io/github/brews/co2syspy?branch=coverage_fix)

A Python interpretation of CO2SYS (http://cdiac.ess-dive.lbl.gov/ftp/co2sys/).

This package is not stable, nor fully tested. It is also not very pythonic.

## Example

First, import the package:

    import co2sys
    
Use the old-school interface with `co2sys.CO2SYS()`. First, lets setup some variables to input:

    par1type =    1  # The first parameter supplied is of type "1", which is "alkalinity"
    par2type =    2  # The first parameter supplied is of type "2", which is "DIC"
    par3type =    3  # The first parameter supplied is of type "3", which is "pH"
    presin   =    4.036785269144779e3  # Pressure at input conditions
    tempout  =    0  # Temperature at output conditions.
    presout  =    0  # Pressure    at output conditions.
    pHscale  =    1  # pH scale at which the input pH is reported ("1" means "Total Scale")
    k1k2c    =    4  # Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
    kso4c    =    1  # Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")
    alk_s = 2.337701660156250e3
    dic_s = 2.186364257812500e3
    sal_s = 34.875812530517578
    temp_s = 2.197510004043579
    si_s = 49.758834838867188
    p_s = 1.458118438720703

Now, take all of this and run with it:

    out, niceheaders = co2sys.CO2SYS(alk_s, dic_s, par1type, par2type, sal_s, 
                                     temp_s, tempout, presin, presout, si_s, 
                                     p_s, pHscale, k1k2c, kso4c)

Our output system variables are now held in `out` and the traditional CO2SYS "nice headers" are in `niceheaders`.

## Installation

Install `co2syspy` from `conda` with:

    $ conda install co2syspy -c sbmalev

Install with `pip`, directly from the master branch using:

    $ pip install git+git://github.com/brews/co2syspy.git@master
    
## Support and development

* Please feel free to report bugs and issues, or view the source code on GitHub (https://github.com/brews/co2syspy).

## License

`co2syspy` is available under the Open Source GPLv3 (https://www.gnu.org/licenses).