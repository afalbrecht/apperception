import json
import pickle
from mem_code import *


if __name__ == '__main__':

    tree = TreeNode('Root')

    # take in filename
    dir = 'misc' #sys.argv[1]
    input_name = 'predict_2' #sys.argv[2]
    filename = dir + '_' + input_name

    # Read in sensory sequence input from input file
    with open(f'memory/{dir}_{input_name}_template_out.txt', 'r') as f:
        template = f.readlines()

    with open(f'memory/{dir}_{input_name}_interpret_mem.lp', 'r') as f:
        interpretation = f.readlines()

    with open('mem_code/mem_tree.pickle', 'wb') as pickle_file:
        pickle.dump(tree, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

    with open('mem_code/mem_tree.pickle', 'rb') as f:
        data = pickle.load(f)

    print(json.dumps(data.to_dict(), indent = 2))
