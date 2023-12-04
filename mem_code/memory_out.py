import shutil
import sys
import os
import pickle
import json
import copy
from mem_code import *

# take in filename
dir = 'misc' # sys.argv[1] #
input_name = 'predict_4_num' # sys.argv[2] #
filename = dir + '_' + input_name

# # Load in tree from pickle file
with open('mem_code/mem_tree.pickle', 'rb') as f:
    tree = pickle.load(f)
# print(data.get_acc_marks())
# data.set_acc_marks([1])
# print(data)
# print(data.get_acc_marks())
# tree = copy.deepcopy(data)
# # print(json.dumps(tree, indent = 4))
# print(tree.extension)



# Read in sensory sequence input from input file
with open(f'memory/{dir}_{input_name}_template_out.txt', 'r') as f:
    template = f.readlines()
    # letter.set_ess_marks([template])

with open(f'memory/{dir}_{input_name}_interpret_mem.lp', 'r') as f:
    interpretation = f.readlines()
    # letter.set_ess_marks(letter.get_ess_marks() + [interpretation])

temp_dict = template_to_dict(template)
# print(temp_dict)
# print(tree.get_extension_names())
update_tree_template(tree, temp_dict)
update_tree_interpret(tree, interpretation)
# tree.get_node_by_name('t_sensor').set_objects([Object('obj_sensor')])
# print(tree.get_extension_names())
# tree.set_acc_marks([1,2,3])
print(tree)
# print(json.dumps(tree.to_dict(), indent = 4))
print(tree.get_pretty_structure())
with open('mem_extra/mem_tree_display.txt', 'w') as file:
    file.write(str(tree))
# print(json.dumps(tree, indent = 4))
# print('-----------------------------------------------------------')
# print(tree.get_n_n_dict().keys())

# print(template)
# print(interpretation)

with open('mem_code/mem_tree.pickle', 'wb') as pickle_file:
    pickle.dump(tree, pickle_file)

# with open('mem_code/mem_tree.json', 'w') as json_file:
#     json.dump(tree, json_file)

# with open('memory/misc_predict_4_num_template_out.txt', 'r') as f:
#     template = f.read()
#     number.set_ess_marks([template])

# with open('memory/misc_predict_4_num_interpret_mem.lp', 'r') as f:
#     interpretation = f.read()
#     number.set_ess_marks(number.get_ess_marks() + [interpretation]
