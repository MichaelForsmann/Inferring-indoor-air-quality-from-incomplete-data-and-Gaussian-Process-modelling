# Inferring indoor air quality from incomplete data and Gaussian Process modelling
This project/paper was made to correct and simulate indoor air pollution in cohorts.
Some particles and gasses have a strong seasonal component due to temperature and habits of the homes, such as $NO_x$ and Black Carbon. 
When working with data on these components, adjusting for the seasonality is extremely important since different periods can have 2-4 fold difference due to traffic and family habits.
## Data
The data is a synthetic version of the Original data from COPSAC. It has the household ID and the measurement of the house where it was taken.
There are multiple indoor and outdoor sources and sinks. The indoor is the number of days the kids are exposed to the source.
The outdoor sources are the total area of the outdoor source as an approximation for the total exposure rate.
The synthetic data was created since it is clinical data, which doesn't allow us to open-source it. 
The data is mostly there to showcase the application and that the code is working.
## Preprocessing 
First 
## Arviz stats 
## Seasonality functions
## Plots
![alt text](http://url/to/img.png)
## models 
## Performance of models




### References
@article{bingham2019pyro,
  author    = {Eli Bingham and
               Jonathan P. Chen and
               Martin Jankowiak and
               Fritz Obermeyer and
               Neeraj Pradhan and
               Theofanis Karaletsos and
               Rohit Singh and
               Paul A. Szerlip and
               Paul Horsfall and
               Noah D. Goodman},
  title     = {Pyro: Deep Universal Probabilistic Programming},
  journal   = {J. Mach. Learn. Res.},
  volume    = {20},
  pages     = {28:1--28:6},
  year      = {2019},
  url       = {http://jmlr.org/papers/v20/18-403.html}
}
