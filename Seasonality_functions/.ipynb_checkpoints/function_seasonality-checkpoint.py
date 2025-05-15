import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from pyro import clear_param_store
import pyro.contrib.gp as gp
from pyro.nn import PyroSample
import pyro.distributions as dist
from pyro.infer import MCMC, NUTS, Predictive,HMC
import torch
import arviz as az
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
def make_periodic(data):
    data=data.loc[(data.corrected_week>0)&(data.corrected_week<53),:].copy()
    data.loc[:,"theta"]=data.corrected_week/53*2*np.pi
    data.loc[:,"cos_theta"]=np.cos(data.corrected_week/data.corrected_week.max()*2*np.pi)
    data.loc[:,"sin_theta"]=np.sin(data.corrected_week/data.corrected_week.max()*2*np.pi)
    return data 
def make_Xy(data,X,y):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data=data.dropna(subset=y)
    X_tensor = torch.from_numpy(data.loc[:,X].dropna().values.astype("float64")).to(device)
    y_tensor=torch.tensor(data.loc[:,y].values).float().to(device)
    return X_tensor,y_tensor
def model(X,y):
    clear_param_store()
    rbf = gp.kernels.RBF(input_dim=X.shape[1])
    rbf.variance = PyroSample(dist.HalfNormal(y.mean()))
    rbf.lengthscale = PyroSample(dist.HalfNormal(torch.tensor(5.)))
    gpr = gp.models.GPRegression(X,y, rbf).to(device)
    gpr.noise = PyroSample(dist.HalfNormal(torch.tensor(20.)))
    nuts_kernel = NUTS(gpr.model)
    return nuts_kernel,gpr
def train_model(X,nuts_kernel,gpr):
    mcmc = MCMC(nuts_kernel,warmup_steps=12000, num_samples=3000,num_chains=1)
    mcmc.run()
    posterior_samples = mcmc.get_samples(500)
    posterior_predictive= Predictive(gpr, posterior_samples)(X)
    prior = Predictive(gpr, num_samples=500)(X)
    pyro_data = az.from_pyro(mcmc,
    prior=prior,
    posterior_predictive=posterior_predictive)
    return pyro_data,gpr,mcmc