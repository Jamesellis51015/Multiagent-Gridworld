# Multiagent-Gridworld

## Work In Progress!

A basic gridworld implementation where agents can collide with each other as well as obstacles. Agents have to navigate to their goal locations. Majority of the code for the environment can be found in Env/grid_env.py and Env/env.py

![Alt text](gridworld_example.png?raw=true "")

Requirements:
- Many requirements. Best would be to make a conda environment from environment.yml

For an example run manual_test.py and type commands according to instructions. (Sometimes fails first time, if its a problem with command inputs, try again.)

To make own gridworld, make new class in env.py which inherits Grid_Env class from grid_env.py and implement reset() and get_rewards() accoring to new environment dynamics. Custom environments instead of randomly generated ones can also be specified by a csv file (see Env/custom folder for examples). 


## Code Credits:

Credits for rendering goes to:

```
@misc{gym_minigrid,
  author = {Chevalier-Boisvert, Maxime and Willems, Lucas and Pal, Suman},
  title = {Minimalistic Gridworld Environment for OpenAI Gym},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/maximecb/gym-minigrid}},
}
```

### Code in Agents/MAAC.py and Agents/maac_utils/ modified from: https://github.com/shariqiqbal2810/MAAC
 
```
@InProceedings{pmlr-v97-iqbal19a,
  title =    {Actor-Attention-Critic for Multi-Agent Reinforcement Learning},
  author =   {Iqbal, Shariq and Sha, Fei},
  booktitle =    {Proceedings of the 36th International Conference on Machine Learning},
  pages =    {2961--2970},
  year =     {2019},
  editor =   {Chaudhuri, Kamalika and Salakhutdinov, Ruslan},
  volume =   {97},
  series =   {Proceedings of Machine Learning Research},
  address =      {Long Beach, California, USA},
  month =    {09--15 Jun},
  publisher =    {PMLR},
  pdf =      {http://proceedings.mlr.press/v97/iqbal19a/iqbal19a.pdf},
  url =      {http://proceedings.mlr.press/v97/iqbal19a.html},
}

```

### Code in Agents/ic3Net.py modified from: https://github.com/IC3Net/IC3Net
```
@article{singh2018learning,
  title={Learning when to Communicate at Scale in Multiagent Cooperative and Competitive Tasks},
  author={Singh, Amanpreet and Jain, Tushar and Sukhbaatar, Sainbayar},
  journal={arXiv preprint arXiv:1812.09755},
  year={2018}
}
```
