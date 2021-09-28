import itertools
import pathlib

def kv_pairs(key, vals):
    return [(key, val) for val in vals]

def make_param_dict(keys, vals):
    kvs = [kv_pairs(k,v) for k, v in zip(keys, vals)]
    print(kvs)
    p_list = list(itertools.product(*kvs))
    return [{p[0]:p[1] for p in pp} for pp in p_list]

def is_hidden(path):

    for x in str(path).split("/"):
        if x.startswith(".") and x != "..":
            return True

    return False

def listfiles(folder, include_hidden=False):
    # generator for files in subdirectory

    if include_hidden:
        out = [x for x in pathlib.Path(folder).glob("**/*")]
        return out
    else:
        out = [x for x in pathlib.Path(folder).glob("**/*") if not is_hidden(x)]
        return out