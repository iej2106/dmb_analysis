# Fisher analysis for constraining dark matter+baryon interaction in early universe. 

The purpose for this repo is to constrain cosmolocial parameters the CMB simulated in the Boltzman code CLASS. In particular I have been constraining the 6 LCDM parameters in addition the the early-universe dark matter-baryon scattering cross section using a modified version of CLASS. With the intention to forcast sensitivities of future CMB experiment by plotting upper limits for cross sections in mass ranging between 10keV - 1TeV. See: upperlimit_crossection.ipynb

<b>compute_fisher_dmb</b> computes the fisher matrix for a given experiment with required input of dark matter (DM) mass, velocity dependence, and relagtive bulk velocity which uses simulated cosmological observables from CLASS.

Each of these notebooks (for given experiment) contains details on the equations used and their references. Each one has input paramters that are easily modified for velocity dependance (n_power/n_dmb), relative bulk velocity (relative_bulk_velocity/Vrel_dmb), dark matter mass (dm_mass/m_dmb), sky coverage (f_sky) etc.

The fiducal values for the LCDM paramters are also easily changed, as well as which one to include/not include.

Each setting above requres adjustment of the step size used in numerically differenting the C_ls in the fisher matrix (see details in notebooks).

To numerically differentiation the Cl's with respect to the parameters you want to contrain its important to choose the right stepsize. One that is small enough to converge but also large enough not to hit numerical noise. See 'convergence_check.ipynb'
## Requirements:
Boltzman code: I used modified version of CLASS with DM baryon interaction: https://github.com/veragluscevic/class_public/tree/dmb

Python 3 (numpy, scipy, matplotlib).


## Formalism
 

[Wu et al. 2014](https://arxiv.org/abs/1402.4108)


## Experimental noise
Each experiment has their own sets of noise curves:
##Sources: 

<b>Simons observatory</b>
Lensing noise: https://github.com/simonsobs/so_noise_models/tree/master/LAT_comp_sep_noise/v3.1.0
Temperature and Polarization: https://github.com/simonsobs/so_noise_models

<b>CMB STAGE-4</b>
https://github.com/xzackli/fishchips-public

<b>Cosmic variance limited</b>

<b>Planck</b>
https://github.com/xzackli/fishchips-public

## References

[Boddy & Gluscevic 2018](https://arxiv.org/abs/1801.08609.pdf) First Cosmological Constraint on the Effective Theory of Dark Matter-Proton Interactions

[Boddy & Gluscevic 2018](https://arxiv.org/pdf/1808.00001.pdf) A Critical Assessment of CMB Limits on Dark Matter–Baryon Scattering:
New Treatment of the Relative Bulk Velocity

[CMB-S4 Collaboration(2016)](https://arxiv.org/pdf/1610.02743.pdf) CMB-S4 Science Book, First Edition

[Coe 2009](https://arxiv.org/pdf/0906.4123.pdf) Fisher Matrices and Confidence Ellipses: A Quick-Start Guide and Software

[Gluscevic & Boddy 2017](https://arxiv.org/pdf/1712.07133.pdf) Constraints on Scattering of keV–TeV Dark Matter with Protons in the Early
Universe

[Lewis & Challinor 2006](https://arxiv.org/pdf/astro-ph/0601594.pdf) Weak Gravitational Lensing of the CMB

[Planck Collaboration et al.(2016)](https://arxiv.org/pdf/1502.01589.pdf) Planck 2015 results. XIII. Cosmological parameters

[Simons Observatory(2018)(https://simonsobservatory.org/)

[Wu et al. 2014](https://arxiv.org/pdf/1402.4108.pdf) A Guide to Designing Future Ground-based CMB Experiments

[Z. Li et al. 2018](https://arxiv.org/pdf/1806.10165.pdf) DISENTANGLING DARK PHYSICS WITH COSMIC MICROWAVE BACKGROUND EXPERIMENTS


## Upper limit on cross section for velocity independent & dependent cases
<img src="fisher_plots/upperlimit_crosssection_all.png " width="600" height="900">

