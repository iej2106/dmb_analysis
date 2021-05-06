masses = [1e-5, 1e-3, 1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 100]
#should be looping m over masses

from classy import Class

cosmo = Class()

cosmo0 = Class()

par0 = {}

par = {}

par['output'] = 'tCl pCl lCl'

par0['output'] = 'tCl pCl lCl'
par['lensing']='yes'
par0['lensing']='yes'

par['omega_cdm'] = 0.

par0['omega_cdm'] = 0.12

par['omega_dmb'] = 0.12

par['m_dmb'] = m

par['sigma_dmb'] = 1.7e-25

cosmo.set(par)
cosmo0.set(par0)

cosmo.compute()
cosmo0.compute()

data0 = cosmo0.lensed_cl()
data = cosmo.lensed_cl()


#for a relative to itself test:
plt.semilogx(data['ell'],((data0[mode]-data[mode])/data0[mode])*100.)

#for a test against the old code, should compare the above lines with equivalent from dmeff 
