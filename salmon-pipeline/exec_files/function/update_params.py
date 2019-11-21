def update_params(params_dict, params_list):
    params_key = [params_list[i] for i in range(len(params_list)) if i%2==0]
    params_value = [params_list[i] for i in range(len(params_list)) if i%2 == 1]
    
    intermidiate_dict = dict(zip(params_key, params_value))

    for k, v in intermidiate_dict.items():
        params_dict[k] = v 

    return params_dict 
