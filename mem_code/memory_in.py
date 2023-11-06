import shutil
import sys
import os
from mem_code import *

# take in filename
dir = sys.argv[1]
input_name = sys.argv[2]
filename = dir + '_' + input_name

# print(recursive_traverse(tree, 'c_letter aospdifja'))

# Load in tree from JSON file
with open('mem_code/mem_tree.json', 'r') as f:
    data = json.load(f)
data_tree = TreeNode.from_dict(data)

# Read in sensory sequence input from input file
with open(f'data/{dir}/{input_name}.lp', 'r') as file:
    input = file.read()

# print(input)

template, interpretation = recursive_traverse(data_tree, input)

# if os.path.isfile(f'memory/{filename}_template_out.txt'):
#   # Read in the file
#   with open(f'memory/{filename}_template_out.txt', 'r') as file:
#     filedata = file.readlines()

filedata = template.splitlines(True)

# Replace the target string
for i, line in enumerate(filedata):
  if 'aux' in line:
    filedata[i] = line.replace('[]', f'["{filename}_interpret_mem.lp"]')
    if not 'interpret' in filedata[i]:
      filedata[i] = line.replace(']', f',"{filename}_interpret_mem.lp"]')

  # filedata = filedata.replace('aux_files = []', 'aux_files = ['+filename+'_interpret_mem.lp]')

  # Write the file out again
  with open(f'memory/{filename}_template_in.txt', 'w') as file:
    file.writelines(filedata)

  with open(f'asp/{filename}_interpret_mem.lp', 'w') as file:
    file.write(interpretation)
  
  # shutil.copyfile(f'memory/{filename}_interpret_mem.lp', f'asp/{filename}_interpret_mem.lp')

# if os.path.isfile(f'memory/{filename}_template_out.txt'):
#   # Read in the file
#   with open(f'memory/{filename}_template_out.txt', 'r') as file:
#     filedata = file.readlines()

# # Replace the target string
# for i, line in enumerate(filedata):
#   if 'aux' in line:
#     filedata[i] = line.replace('[]', f'["{filename}_interpret_mem.lp"]')
#     if not 'interpret' in filedata[i]:
#       filedata[i] = line.replace(']', f',"{filename}_interpret_mem.lp"]')

#   # filedata = filedata.replace('aux_files = []', 'aux_files = ['+filename+'_interpret_mem.lp]')

#   # Write the file out again
#   with open(f'memory/{filename}_template_in.txt', 'w') as file:
#     file.writelines(filedata)

#   shutil.copyfile(f'memory/{filename}_interpret_mem.lp', f'asp/{filename}_interpret_mem.lp')


