import main
from sklearn.model_selection import ParameterGrid

def test_ppo2():
    n_iterations = str(2000) #str(3000)
    experiment_group_name = "TEST_ppo"
    work_dir = experiment_group_name
    plot_dir = experiment_group_name + "_Central"
 
    parmeter_grid1 = {
        "seed": [3],
        "workers": [4],#[8],
        "rollout_length": [10],#[256],
        "eps_clip": [0.2],
        "k_epochs": [2],
        "minibatch_size": [40],
        "entropy_coeff":[0.01],
        "discount":[0.9],
        "lambda_": [1.0],
        "value_coeff": [0.5],
        "policy": ["PPO"],
        "n_agents": [4],
        "recurrent": [True],
        "base_policy_type": ["mlp"],
        "valid_act_heur": [False],
        "block_heur": [True]
    }


    grid1 = ParameterGrid(parmeter_grid1)

    
    
    for param in grid1:
        args = []
        args = ["--working_directory", work_dir, "--alternative_plot_dir", plot_dir]
        #args.extend(["--iterations", n_iterations])
      
        name = "block_" +str(param["block_heur"]) +"valid_act_heur" + str(param["valid_act_heur"]) + "disc" + str(param["discount"]) \
            + "_lambda" + str(param["lambda_"]) \
         + "_workers" + str(param["workers"]) + \
             "_nrollouts" + str(param["rollout_length"]) + \
             "_eps_clip" + str(param["eps_clip"]) + \
            "_val_coeff_" + str(param["value_coeff"]) \
            + "_ent" + str(param["entropy_coeff"]) \
            + "_agnts" + str(param["n_agents"]) + "_" + str(param["policy"])
        #"_ent" + str(param["entropy_coeff"]) \
        
        args.extend(["--env_name", "independent_navigation-v2"])
        args.extend(["--view_d", str(int(4))])
        args.extend(["--obj_density", str(0.25)])
        args.extend(["--map_shape", str(int(6))])
        args.extend(["--n_agents", str(param["n_agents"])])
        args.extend(["--policy", param["policy"]])
        args.extend(["--name", name])
        args.extend(["--seed", str(param["seed"])])
        args.extend(["--render_rate", str(int(10))])
        args.extend(["--benchmark_frequency", str(int(1000))])
        args.extend(["--benchmark_num_episodes", str(int(50))])
        args.extend(["--benchmark_render_length", str(int(25))])

        #           PPO Paramares:
        args.extend(["--ppo_hidden_dim", str(120)])
        args.extend(["--ppo_recurrent"])
        # if param["valid_act_heur"]:
        #   args.extend(["--ppo_heur_valid_act"])
        if param["block_heur"]:
            args.extend(["--ppo_heur_block"])
      #  args.extend(["--ppo_heur_block"])
        #args.extend(["--ppo_heur_no_prev_state"])

        args.extend(["--ppo_lr_a", str(0.001)])
        args.extend(["--ppo_lr_v", str(0.001)])
        args.extend(["--ppo_base_policy_type", "mlp"])
        args.extend(["--ppo_workers", str(param['workers'])])
        args.extend(["--ppo_rollout_length", str(param['rollout_length'])])
        args.extend(["--ppo_share_actor"])
        args.extend(["--ppo_share_value"])
        args.extend(["--ppo_iterations", n_iterations])
        args.extend(["--ppo_k_epochs", str(param['k_epochs'])])
        args.extend(["--ppo_eps_clip", str(param["eps_clip"])])
        args.extend(["--ppo_minibatch_size", str(param['minibatch_size'])])
        args.extend(["--ppo_entropy_coeff", str(param['entropy_coeff'])])
        args.extend(["--ppo_value_coeff", str(param['value_coeff'])])
        args.extend(["--ppo_discount", str(param['discount'])])
        args.extend(["--ppo_gae_lambda", str(param['lambda_'])])
     #   args.extend(["--ppo_use_gpu"])
    
        main.main(args)