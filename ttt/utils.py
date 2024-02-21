import itertools
import pathlib
from itertools import repeat
from os import scandir


def kv_pairs(key, vals):
    return [(key, val) for val in vals]


def make_param_dict(keys, vals):
    kvs = [kv_pairs(k, v) for k, v in zip(keys, vals)]
    print(kvs)
    p_list = list(itertools.product(*kvs))
    return [{p[0]: p[1] for p in pp} for pp in p_list]


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


def listfolders(folder):
    folders = [pathlib.Path(x) for x in scandir(folder) if pathlib.Path(x).is_dir()]
    return folders


def walk_keys(dictionary, layer=0):
    layer += 1
    try:
        keys = dictionary.keys()
        for key in keys:
            printStr = "--" * layer
            printStr += key
            print(printStr)
            walk_keys(dictionary[key], layer)
    except AttributeError:
        return
