import shutil
import sys
import os
import pickle
from mem_code import *


# take in filename
dir = sys.argv[1]
input_name = sys.argv[2]
flag = sys.argv[3]
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
    # os.remove(f'memory/{filename}_template_in.txt')
    shutil.rmtree(f"memory/{filename}")
    os.mkdir(f"memory/{filename}")



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
    print(senses_list)
    # Retrieve essential marks from tree depending on input
    temp_dict = build_template(tree, input, senses_list)
    # for t in temp_dict:
    #     template = mem_to_template(t, dir, input_name)
    #     print(template)
    # print('----------------------------------------')
    # print(temp_dict)
    # print('----------------------------------------')     
    go = True
    # temp_dict = temp_dict[0]
    

    if temp_dict != []: #[0]["types"]
        count = 0
        stats = f"% {filename}\n"
        for i, t in enumerate(temp_dict):
            print("Using memory tree")
            template = mem_to_template(t, dir, input_name)
            filedata = template.splitlines(True)
            print(template)
            interpretations = build_interpretation(tree, t, senses_list, dir, input_name)
            for j, interpretation in enumerate(interpretations):
                count = count + 1
                stats = stats + f"{i},{j}\n"

                # Replace the target string
                for k, line in enumerate(filedata):
                    if 'aux' in line:
                        filedata[k] = line.replace('[]', f'["{filename}/{filename}_interpret_mem_{i}_{j}.lp"]')
                        if not 'interpret' in filedata[k]:
                            filedata[k] = line.replace(']', f',"{filename}/{filename}_interpret_mem_{i}_{j}.lp"]')
                
                # Write the file out again
                with open(f'memory/{filename}/{filename}_template_in_{i}_{j}.txt', 'w') as file:
                    file.writelines(filedata)


                if "1" in flag:
                    print("Using empty interpretation file")
                    interpretation = ""
                
                with open(f'asp/{filename}/{filename}_interpret_mem_{i}_{j}.lp', 'w') as file:
                        file.write(interpretation)
        
        # stats = stats + f"count = {count}"
        # with open(f'memory/{filename}/{filename}_stats.txt', 'w') as file:
        #                 file.write(stats)
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
        
        # with open(f'memory/{filename}/{filename}_stats.txt', 'w') as file:
        #     file.write(stats)
        







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

    # with open(f'memory/{filename}/{filename}_stats.txt', 'w') as file:
    #         file.write(stats)

    if "1" in flag:
        print("Using empty interpretation file")
        interpretation = ""
    else:
        with open(f'memory/{filename}_interpret_mem.lp', 'r') as file:
            interpretation = file.read()
    
    with open(f'asp/{filename}/{filename}_interpret_mem_0_0.lp', 'w') as file:
            file.write(interpretation)

    # shutil.copyfile(f'memory/{filename}_interpret_mem.lp', f'asp/{filename}_interpret_mem.lp')

# if "3" not in flag:
#     os.remove(f'memory/{filename}/{filename}_stats.txt')
