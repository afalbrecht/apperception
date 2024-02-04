import shutil
import sys
import os
import pickle
import json
import copy
import time
from mem_code import *

# take in filename
dir = sys.argv[1] 
input_name = sys.argv[2] 
filename = dir + '_' + input_name

with open('mem_extra/timing.txt', 'r') as f:
    t0 = f.readlines()[-1].replace("\\\\\n", "")

with open('mem_extra/timing.txt', 'a') as f:
    t1 = time.time()
    f.write(str(t1) + "\\\\\n")
    f.write(str(t1-float(t0)) + "\n\n")

# # Load in tree from pickle file
with open('mem_code/mem_tree.pickle', 'rb') as f:
    tree = pickle.load(f)

# Read in sensory sequence input from input file
with open(f'memory/{dir}_{input_name}/{dir}_{input_name}_template_out.txt', 'r') as f:
    template = f.readlines()


with open(f'memory/{dir}_{input_name}/{dir}_{input_name}_interpret_mem.lp', 'r') as f:
    interpretation = f.readlines()


temp_dict = template_to_dict(template)
print("".join(template))
print("".join(interpretation))

update_tree_template(tree, temp_dict)
update_tree_interpret(tree, interpretation, temp_dict)
if tree.get_node_by_name("t_grid") != None:
    tree.get_node_by_name("t_grid").set_objects_to_form_of_intuition()
if tree.get_node_by_name("t_cell") != None:
    tree.get_node_by_name("t_cell").set_objects_to_form_of_intuition()


print(tree.get_pretty_structure())


with open('mem_extra/mem_tree_display.json', 'w') as file:
    file.write(str(tree))

with open(f'mem_extra/latex_tree.tex', 'w') as file:
    file.write(json_to_latex(json.loads(str(tree))))

with open('mem_code/mem_tree.pickle', 'wb') as pickle_file:
    pickle.dump(tree, pickle_file)
