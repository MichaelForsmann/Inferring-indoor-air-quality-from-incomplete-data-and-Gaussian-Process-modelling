# Inferring indoor air quality from incomplete data and Gaussian Process modelling
This project/paper was made to correct and simulate indoor air pollution in cohorts.
Some particles and gasses have a strong seasonal component due to temperature and habits of the homes, such as $NO_x$ and Black Carbon. 
When working with data on these components, adjusting for the seasonality is extremely important since different periods can have 2-4 fold difference due to traffic and family habits.
## Data
The data is a synthetic version of the Original COPSAC data. It has the household ID and the measurement of the house where it was taken.
There are multiple indoor and outdoor sources and sinks. The indoor is the number of days the kids are exposed to the source.
The outdoor sources are the total area of the outdoor source as an approximation for the total exposure rate.
The synthetic data was created since it is clinical data, which doesn't allow us to open-source it. 
The data is mostly there to showcase the application and that the code is working.
## Preprocessing 
![plot](https://github.com/MichaelForsmann/Inferring-indoor-air-quality-from-incomplete-data-and-Gaussian-Process-modelling/blob/main/pipeline.png)
![plot](https://github.com/MichaelForsmann/Inferring-indoor-air-quality-from-incomplete-data-and-Gaussian-Process-modelling/blob/main/pm_seasonality.png)
## Plots and performence to estimate general function for seasonality of the gases and particles
![plot](https://github.com/MichaelForsmann/Inferring-indoor-air-quality-from-incomplete-data-and-Gaussian-Process-modelling/blob/main/pm_seasonality.png)
![plot](https://github.com/MichaelForsmann/Inferring-indoor-air-quality-from-incomplete-data-and-Gaussian-Process-modelling/blob/main/no2_seasonality.png)
![plot](https://github.com/MichaelForsmann/Inferring-indoor-air-quality-from-incomplete-data-and-Gaussian-Process-modelling/blob/main/VOCs_seasonality(3).png)
## Models folder 
All the gaussion porcess models used are saved in this folder 

Performance of models
## Arviz stats plots about stability and converge from the models


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
@article{scikit-learn,
  title={Scikit-learn: Machine Learning in {P}ython},
  author={Pedregosa, F. and Varoquaux, G. and Gramfort, A. and Michel, V.
          and Thirion, B. and Grisel, O. and Blondel, M. and Prettenhofer, P.
          and Weiss, R. and Dubourg, V. and Vanderplas, J. and Passos, A. and
          Cournapeau, D. and Brucher, M. and Perrot, M. and Duchesnay, E.},
  journal={Journal of Machine Learning Research},
  volume={12},
  pages={2825--2830},
  year={2011}
}
@ARTICLE{2020SciPy-NMeth,
  author  = {Virtanen, Pauli and Gommers, Ralf and Oliphant, Travis E. and
            Haberland, Matt and Reddy, Tyler and Cournapeau, David and
            Burovski, Evgeni and Peterson, Pearu and Weckesser, Warren and
            Bright, Jonathan and {van der Walt}, St{\'e}fan J. and
            Brett, Matthew and Wilson, Joshua and Millman, K. Jarrod and
            Mayorov, Nikolay and Nelson, Andrew R. J. and Jones, Eric and
            Kern, Robert and Larson, Eric and Carey, C J and
            Polat, {\.I}lhan and Feng, Yu and Moore, Eric W. and
            {VanderPlas}, Jake and Laxalde, Denis and Perktold, Josef and
            Cimrman, Robert and Henriksen, Ian and Quintero, E. A. and
            Harris, Charles R. and Archibald, Anne M. and
            Ribeiro, Ant{\^o}nio H. and Pedregosa, Fabian and
            {van Mulbregt}, Paul and {SciPy 1.0 Contributors}},
  title   = {{{SciPy} 1.0: Fundamental Algorithms for Scientific
            Computing in Python}},
  journal = {Nature Methods},
  year    = {2020},
  volume  = {17},
  pages   = {261--272},
  adsurl  = {https://rdcu.be/b08Wh},
  doi     = {10.1038/s41592-019-0686-2},

@incollection{NEURIPS2019_9015,
title = {PyTorch: An Imperative Style, High-Performance Deep Learning Library},
author = {Paszke, Adam and Gross, Sam and Massa, Francisco and Lerer, Adam and Bradbury, James and Chanan, Gregory and Killeen, Trevor and Lin, Zeming and Gimelshein, Natalia and Antiga, Luca and Desmaison, Alban and Kopf, Andreas and Yang, Edward and DeVito, Zachary and Raison, Martin and Tejani, Alykhan and Chilamkurthy, Sasank and Steiner, Benoit and Fang, Lu and Bai, Junjie and Chintala, Soumith},
booktitle = {Advances in Neural Information Processing Systems 32},
pages = {8024--8035},
year = {2019},
publisher = {Curran Associates, Inc.},
url = {http://papers.neurips.cc/paper/9015-pytorch-an-imperative-style-high-performance-deep-learning-library.pdf}
} 
