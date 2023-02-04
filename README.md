# Model-Evaluation
TPAMI'23: Evaluating Classification Model Against Bayes Error Rate

## Introduction:

This is the code repository to reproduce the experiments in the paper **[Evaluating Classification Model Against Bayes Error Rate]
(https://ieeexplore.ieee.org/document/10027467)**. This repository is based on numpy, scipy and [Sklearn](https://scikit-learn.org/stable/).

## Prerequisite

We implement our methods by Python 3.8. The environment is as bellow:

- Anaconda 3  
- Linux operating system or Windows operating system  
- Sklearn, numpy, matplotlib  


## Run demo

### Synthetic Data Set 
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian.png" width='30%' height='30%'/>
</p>

### Homogeneous clusters  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian_hc.png" width='30%' height='30%'/>
</p>

### Reduced Data Set  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian_reduced.png" width='30%' height='30%'/>
</p>

## Technical Details and Citations:  
You can find more details in the paper:  
[Evaluating Classification Model Against Bayes Error Rate](https://ieeexplore.ieee.org/document/10027467)

If you're using this repo in your research or applications, please cite this BibTeX:

@ARTICLE{10027467,
  author={Chen, Qingqiang and Cao, Fuyuan and Xing, Ying and Liang, Jiye},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title={Evaluating Classification Model Against Bayes Error Rate}, 
  year={2023},
  volume={},
  number={},
  pages={1-16},
  doi={10.1109/TPAMI.2023.3240194}}
