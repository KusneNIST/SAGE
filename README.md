# SAGE
Supporting code for the paper: Kusne, AG, McDannald, A, DeCost, B, "Learning material synthesis–process–structure–property relationship by data fusion: Bayesian co-regionalization N-dimensional piecewise function learning", Digital Discovery, 2024, http://dx.doi.org/10.1039/D4DD00048J.
* If there are any issues, please contact: aaron (dot) kusne (at) nist (dot) gov

## Binder:
You can run the provided notebooks in the Binder environment: https://mybinder.org/v2/gh/KusneNIST/SAGE/HEAD
Notebooks provided:
* Simple function calls using NIST's `Hermes` (or equivalently `Sage`) library.
  * 1D case: (Only Hermes) SAGE_for_SPSPR_Learning_1D_Examples_240821a
  * ND case: (Only Hermes) SAGE_for_SPSPR_Learning_ND_Examples_240821a
* Full code for regenerating all the figures in the paper:
  * 1D case: (Full paper) SAGE for SPSPR Learning 1D Examples 240821a
  * ND case: (Full paper) SAGE for SPSPR Learning ND 240821a
 
Required libraries can be found in requirements.txt. This code uses Python 3.9.

The provided `Hermes` library (folder: hermes, zip: hermes_240821a.zip) is an older version. \
The newest version of `Hermes` can be found here: https://github.com/usnistgov/hermes \
All SAGE functions can also be called through the SAGE library found here (folder: sage, zip:SAGE_240821a.zip). \
To do so, simply change the call hermes.(function) to sage.(function) \
e.g., replace hermes.SAGE_1D with sage.SAGE_1D.

