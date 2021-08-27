import itertools

def kv_pairs(key, vals):
    return [(key, val) for val in vals]

def make_param_dict(keys, vals):
    kvs = [kv_pairs(k,v) for k, v in zip(keys, vals)]
    print(kvs)
    p_list = list(itertools.product(*kvs))
    return [{p[0]:p[1] for p in pp} for pp in p_list]