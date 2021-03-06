
# About

This repository contains a PyTorch implementation of [*No Fuss Distance Metric Learning using Proxies*](https://arxiv.org/pdf/1703.07464.pdf) as introduced by Google Research.

The adjustment of most training settings (learning rate, optimizer, criterion, dataset, ...) in the config file. 

Since the training has been done on Google Colab, Spec: Nvidia K80 / T4, GPU memory : 12GB, Performance : 4.1 TFLOPS / 8.1 TFLOPS.


## [Cars_196 , CUB 200-2011 , SOP]
```
You can head to the Proxy-nca ( https://github.com/dichotomies/proxy-nca ) to follow train instractions
```
## Dataset

UPMC-G20 is a dataset based on the UPMC Food-101 with gaze annotation.<br/>
We selected 20 food categories and 100 images per category from the UPMC Food-101.<br/>
For each image, we collected about 15 fixations across 3 subjects with a total duration of 2.5 seconds.<br/> 
The categories selected are Apple-pie, Bread-pudding, Beef-carpaccio, Beet-salad, Chocolate-cake, 
Chocolate-mousse, Donuts, Beignets, Eggs-benedict, Croque-madame, Gnocchi, Shrimp-and-grits, Grilled-salmon,
Pork-chop, Lasagna, Ravioli, Pancakes, French-toast, Spaghetti-bolognese, Pad-thai.

Link : http://visiir.lip6.fr/

### [UPMC-G20](http://visiir.lip6.fr/)

```
git clone 'https://github.com/Papirapi/proxy-nca.git'
cd proxy-nca
mkdir foods
cd foods
wget 'http://visiir.lip6.fr/data/public/Gaze_UPMC_Food20.zip'
!unzip Gaze_UPMC_Food20.zip
cd ..
python3 foods_dataset.py


PS:This repo has been edited from orignal proxy-nca (dichotomies) and training has been done on Google Colab:
Paths has been edited for colab use, if you want to replicated the training on another environment please 
consider chanigng the paths.

```
[Google Colab implementation](https://colab.research.google.com/drive/1orzykB4Gf8ly1pYdzSgGEV9h7h_McnCl?usp=sharing)



## Commands

```
DATA=foods; SCALING_X=3.0; SCALING_P=3.0; LR=0.01; python3 train.py --data $DATA \
--log-filename $DATA-scaling_x_$SCALING_X-scaling_p_$SCALING_P-lr_$LR \
--config config.json --epochs=20 --gpu-id 0 --lr-proxynca=$LR \
--scaling-x=$SCALING_X --scaling-p=$SCALING_P --with-nmi
```
## Training

Since the UPMC-G20 dataset contains only 20 classes, and since in the ‘No Fuss Distance Metric Learning Using Proxies’ 
used half of the classes for train and the otherhalf for the evaluation.<br/>
In our case, 10 classes were used for training (50%) and 10 classes for evaluation (50%).<br/>
Such low number of classes impact the value of NMI that can be found in the Results section.<br/>
(Explanation: The number of classes is small for working with Distance Metric Learning like has been done with Cars_196, CUB 200-2011, SOP.
Also, the inner-class variation is quite large when compared with the intra-class variation.)<br/>
Most of the training parameters can be adjusted in the config file. <br/>
(config.json file contains the best selected parameters after many tries).<br/>
The training duration was about 12~13min.

## Results

The results were obtained mostly with one Colab GPU with the following specs:
Nvidia K80 / T4, GPU memory : 12GB, Performance : 4.1 TFLOPS / 8.1 TFLOPS.

Reading: This Implementation [Link](https://arxiv.org/pdf/1703.07464.pdf)].

|          | UPMC-G20          |
| -------- | ----------------- |
| Duration | 12:00 min         |
| Epoch    | 20                |
| Log      | [Link](https://github.com/Papirapi/proxy-nca/blob/master/log/foods-scaling_x_3.0-scaling_p_3.0-lr_0.01.log)| 
| R@1      | **38.100**        |
| R@2      | **55.900**        |
| R@4      | **70.900**        |
| R@8      | **82.300**        |
| NMI      | **24.365**        |


# Referencing this Implementation:
I did not contribute to this work, I just run training on a different dataset from previous used one.<br/>
If you'd like to reference this ProxyNCA implementation, you can use this bibtex:
 
```
@misc{Tschernezki2020,
  author = {Tschernezki, Vadim and Sanakoyeu, Artsiom and Ommer, Bj{\"o}rn,},
  title = {PyTorch Implementation of ProxyNCA},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/dichotomies/proxy-nca}},
}
```


# How unlabelled data can be incorporated into proxy learning as was pioneered by Ren et al. for episodic meta learning?
(https://arxiv.org/abs/1803.00676) 

First consider a simple way of leveraging ***unlabeled examples*** for refining prototypes.<br/>
Viewing each prototype as a cluster center, the refinement process could attempt to adjust the cluster locations to better fit the examples in both the support S and ***unlabeled set***.<br/>
Cluster assignments of the labeled examples in the support set S are considered known and fixed to each example’s label.<br/>
The refinement process must instead estimate the cluster assignments of the ***unlabeled examples*** and adjust the cluster locations (prototypes) accordingly.<br/>


# MORE : 
A new CVPR paper 'Proxy Anchor Loss for Deep Metric Learning' by Sungyeon. et Al ( https://arxiv.org/pdf/2003.13911.pdf )<br/>
Github repo : https://github.com/tjddus9597/Proxy-Anchor-CVPR2020 <br/>
This paper presents a new proxy-based loss that takes advantages of both pair- and proxy-based methods and overcomes their limitations.<br/>
Adv: + reducing training complexity & + Rich and fine-grained <br/>
Overcoming limitations: - impoverished information & Demanding high training complexity
