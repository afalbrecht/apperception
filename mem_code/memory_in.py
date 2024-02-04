import shutil
import sys
import os
import pickle
import time
from mem_code import *


# take in filename
dir = sys.argv[1]
input_name = sys.argv[2]
flag = sys.argv[3]
if "4" in flag:
    aux_files = '\"bnn.lp\",\"visual_sokoban.lp\",'
else:
    aux_files = ""
if "5" in flag:
    optimize = True
else:
    optimize = False
filename = dir + '_' + input_name


if not os.path.isdir(f"asp/{filename}"):
    os.mkdir(f"asp/{filename}")
if not os.path.isdir(f"memory/{filename}"):
    os.mkdir(f"memory/{filename}")
else:
    shutil.rmtree(f"memory/{filename}")
    os.mkdir(f"memory/{filename}")
    shutil.rmtree(f"asp/{filename}")
    os.mkdir(f"asp/{filename}")
stats = f"% {filename}\ncount = 1"

# Delete template_in files
if "3" in flag:
    print("Deleting template_in files")
    shutil.rmtree(f"memory/{filename}")
    os.mkdir(f"memory/{filename}")


with open('mem_extra/timing.txt', 'a') as f:
    f.write(' '.join(sys.argv[1:]).replace("_", "\\_") + "\n")
    f.write(str(time.time()) + "\\\\\n")


if "0" in flag and "3" not in flag:
    print("Using memory if possible")

    # Load in tree from JSON file
    with open('mem_code/mem_tree.pickle', 'rb') as f:
        tree = pickle.load(f)
    # data_tree = TreeNode.from_dict(data)

    # Read in sensory sequence input from input file
    with open(f'data/{dir}/{input_name}.lp', 'r') as file:
        input = file.read()
    
    

    

    # Parse input to isolate "senses" facts
    senses_list = parse_input(input)

    # Retrieve essential marks from tree depending on input
    temp_dict = build_template(tree, input, senses_list, optimize)
  
    go = True

    

    if temp_dict != []: 
        count = 0
        stats = f"% {filename}\n"
        for i, t in enumerate(temp_dict):
            print("Using memory tree")
            template = mem_to_template(t, dir, input_name)
            filedata = template.splitlines(True)
            interpretations = build_interpretation(tree, t, senses_list, dir, input_name)
            for j, interpretation in enumerate(interpretations):
                count = count + 1

                # Replace the target string
                for k, line in enumerate(filedata):
                    if 'aux' in line:
                        line = "aux_files = []"
                        filedata[k] = line.replace('[]', f'[{aux_files}"{filename}/{filename}_interpret_mem_{i}_{j}.lp"]')
                
                # Write the file out again
                with open(f'memory/{filename}/{filename}_template_in_{i}_{j}.txt', 'w') as file:
                    file.writelines(filedata)


                if "1" in flag:
                    print("Using empty interpretation file")
                    interpretation = ""
                
                with open(f'asp/{filename}/{filename}_interpret_mem_{i}_{j}.lp', 'w') as file:
                    file.write(interpretation)
        
        go = False


    elif os.path.isfile(f'memory/{filename}_template_out.txt'):
        print("Using template files")
        # Read in template file
        with open(f'memory/{filename}_template_out.txt', 'r') as file:
            filedata = file.readlines()
        with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
            interpretation = file.read()
    else:
        go = False
        



    if go:
        # Replace the target string
        for i, line in enumerate(filedata):
            if 'aux' in line:
                filedata[i] = line.replace('[]', f'["{filename}/{filename}_interpret_mem_0_0.lp"]')
                if not 'interpret' in filedata[i]:
                    filedata[i] = line.replace(']', f',"{filename}/{filename}_interpret_mem_0_0.lp"]')

        # Write the file out again
        with open(f'memory/{filename}/{filename}_template_in_0_0.txt', 'w') as file:
            file.writelines(filedata)

        if "1" in flag:
            print("Using empty interpretation file")
            interpretation = ""
        
        with open(f'asp/{filename}/{filename}_interpret_mem_0_0.lp', 'w') as file:
                file.write(interpretation)
        


if os.path.isfile(f'memory/{filename}_template_out.txt') and "2" in flag and "3" not in flag:
    print("Using saved template")
    # Read in the file
    with open(f'memory/{filename}_template_out.txt', 'r') as file:
        filedata = file.readlines()

    # Replace the target string
    for i, line in enumerate(filedata):
        if 'aux' in line:
            filedata[i] = line.replace('[]', f'["{filename}/{filename}_interpret_mem_0_0.lp"]')
            if not 'interpret' in filedata[i]:
                filedata[i] = line.replace(']', f',"{filename}/{filename}_interpret_mem_0_0.lp"]')

    # Write the file out again
    with open(f'memory/{filename}/{filename}_template_in_0_0.txt', 'w') as file:
        file.writelines(filedata)

    if "1" in flag:
        print("Using empty interpretation file")
        interpretation = ""
    else:
        with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
            interpretation = file.read()
    
    with open(f'asp/{filename}/{filename}_interpret_mem_0_0.lp', 'w') as file:
            file.write(interpretation)


