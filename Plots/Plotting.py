import numpy as np
import torch
import pandas as pd
from bokeh.models import Band, ColumnDataSource
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
def gaussian_plot(x,model):
    cosx=np.cos(x/x.max()*np.pi*2)
    sinx=np.sin(x/x.max()*np.pi*2)
    data=pd.DataFrame(np.array([cosx,sinx]).T,columns=["x_cos","x_sin"])
    linmod=torch.from_numpy(data.values.astype("float64")).to(device)
    model_y,model_y_std=model(linmod,full_cov=True)
    model_np,model_std_np=model_y.cpu().detach().numpy().copy(),model_y_std.diag().sqrt().cpu().detach().numpy().copy()
    lower = model_np - model_std_np
    upper = model_np + model_std_np
    data_plot=pd.DataFrame([model_np,lower,upper],index=["y","lower","upper"]).T.set_index(x)
    return ColumnDataSource(data_plot.reset_index()),data_plot
def roll_week(data,resolution,week,particle):
    mean=[]
    std=[]
    particle=particle
    x=np.linspace(0,52.5,resolution,endpoint=True)
    sort=data.sort_values("corrected_week")
    for i in x:
        mean.append(sort.loc[(i-week<sort.corrected_week)&(i+week>sort.corrected_week),particle].mean())
        std.append(sort.loc[(i-week<sort.corrected_week)&(i+week>sort.corrected_week),particle].std())
    mean_1,std_1=pd.DataFrame(mean,index=x),pd.DataFrame(std,index=x)
    lower_std = mean_1 - std_1
    upper_std = mean_1 + std_1
    mean=pd.concat([mean_1,lower_std,upper_std],axis=1)
    mean.columns=["y","lower","upper"]
    mean=mean.set_index(x)
    mean1 = ColumnDataSource(mean)
    return mean1,mean