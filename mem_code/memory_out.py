import shutil
import sys
import os
import pickle
import json
import copy
from mem_code import *

# take in filename
dir = sys.argv[1] # 'misc' # 
input_name = sys.argv[2] # 'predict_4_num' # 
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
with open(f'memory/{dir}_{input_name}/{dir}_{input_name}_template_out.txt', 'r') as f:
    template = f.readlines()
    # letter.set_ess_marks([template])

with open(f'memory/{dir}_{input_name}/{dir}_{input_name}_interpret_mem.lp', 'r') as f:
    interpretation = f.readlines()
    # letter.set_ess_marks(letter.get_ess_marks() + [interpretation])

temp_dict = template_to_dict(template)
print("".join(template))
print("".join(interpretation))
# print(tree.get_extension_names())
update_tree_template(tree, temp_dict)
update_tree_interpret(tree, interpretation, temp_dict)
if tree.get_node_by_name("t_grid") != None:
    tree.get_node_by_name("t_grid").set_objects_to_form_of_intuition()
if tree.get_node_by_name("t_cell") != None:
    tree.get_node_by_name("t_cell").set_objects_to_form_of_intuition()

# tree.get_node_by_name('t_sensor').set_objects([Object('obj_sensor')])
# print(tree.get_extension_names())
# tree.set_acc_marks([1,2,3])
# print(tree.get_node_by_name("t_2").get_concept_by_name("c_p4").get_rules())
# print(json.dumps(tree.to_dict(), indent = 4))
print(tree.get_pretty_structure())
# print(tree.get_node_by_name("t_grid").get_object_by_name("obj_grid").get_form_of_intuition())
# print(tree.get_path_to_node("t_test3"))
with open('mem_extra/mem_tree_display.json', 'w') as file:
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
