"""

test_mpm_w_mgb.py

Author: Jordan Mirocha
Affiliation: University of Colorado at Boulder
Created on: Mon Mar 23 09:35:41 MDT 2015

Description: Test the evolution of a MultiPhaseMedium using ionization and
heating rates induced by a MetaGalacticBackground (hence, mpm_w_mgb). 

"""

import ares
import numpy as np
import matplotlib.pyplot as pl

pars = \
{
 'source_type': 'bh',
 'spectrum_type': 'pl',
 'spectrum_alpha': -1.5,
 'spectrum_Emin': 2e2,
 'spectrum_Emax': 3e4,
 'spectrum_EminNorm': 2e2,
 'spectrum_EmaxNorm': 5e4,
 'approx_xrb': False,
 'redshifts_xrb': 400,
 'initial_redshift': 40.,
 'final_redshift': 10.,
 'is_ion_src_cgm': False,
 'include_He': True,
}

sim = ares.simulations.MultiPhaseMedium(**pars)
sim.run()

anl = ares.analysis.MultiPhaseMedium(sim)
ax1 = anl.TemperatureHistory()

ax2 = anl.IonizationHistory(element='h', color='k', fig=2)
ax2 = anl.IonizationHistory(element='he', color='b', ax=ax2)



