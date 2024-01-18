import json
import pickle
from mem_code import *


if __name__ == '__main__':

    tree = TreeNode('Root')
    # tree.set_acc_marks([1,2,3])
    # tree.add_node(TreeNode('t_sensor', suff_marks=['obj_sensor']))
    # tree.add_node(TreeNode('t_object'))
    # tree.add_node(TreeNode('t_grid'))
    # letter = tree.add_node(TreeNode('t_letter', suff_marks=['c_letter'])) #, ess_marks=['misc_predict_4_template_out.txt', 'misc_predict_4_interpret_mem.lp']))
    # number = tree.add_node(TreeNode('t_number', suff_marks=['c_number'])) #, ess_marks=['misc_predict_4_num_template_out.txt', 'misc_predict_4_num_interpret_mem.lp']))
    # number.add_node(TreeNode('0', suff_marks=['obj_number_0']))
    # number.add_concept(Concept('test'))
    
    # with open('memory/misc_predict_4_template_out.txt', 'r') as f:
    #     template = f.read()
    #     letter.set_ess_marks([template])
    
    # with open('memory/misc_predict_4_interpret_mem.lp', 'r') as f:
    #     interpretation = f.read()
    #     letter.set_ess_marks(letter.get_ess_marks() + [interpretation])

    # with open('memory/misc_predict_4_num_template_out.txt', 'r') as f:
    #     template = f.read()
    #     number.set_ess_marks([template])
    
    # with open('memory/misc_predict_4_num_interpret_mem.lp', 'r') as f:
    #     interpretation = f.read()
    #     number.set_ess_marks(number.get_ess_marks() + [interpretation])

    # marks = recursive_traverse(tree, 'c_leteraospdifja')

    # take in filename
    dir = 'misc' #sys.argv[1]
    input_name = 'predict_2' #sys.argv[2]
    filename = dir + '_' + input_name

    # Read in sensory sequence input from input file
    with open(f'memory/{dir}_{input_name}_template_out.txt', 'r') as f:
        template = f.readlines()
        # letter.set_ess_marks([template])

    with open(f'memory/{dir}_{input_name}_interpret_mem.lp', 'r') as f:
        interpretation = f.readlines()
        # letter.set_ess_marks(letter.get_ess_marks() + [interpretation])

    # temp_dict = template_to_dict(template)
    # # print(temp_dict)
    # print(tree)
    # print(tree.get_extension_names())
    # update_tree_template(tree, temp_dict)
    # print(tree.get_extension_names())
    # tree.set_acc_marks([1,2,3])
    # print(tree)
    # print(tree.get_structure())
    # print(json.dumps(tree, indent = 4))
    # print(one, two)

    # with open('mem_code/mem_tree.json', 'w') as json_file:
    #     json.dump(tree, json_file)

    # with open('mem_code/mem_tree.json', 'r') as f:
    #     data = json.load(f)
    # data_tree = TreeNode.from_dict(data)

    with open('mem_code/mem_tree.pickle', 'wb') as pickle_file:
        pickle.dump(tree, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

    with open('mem_code/mem_tree.pickle', 'rb') as f:
        data = pickle.load(f)
    # print(data)
    # data_tree = TreeNode.from_dict(data)
    print(json.dumps(data.to_dict(), indent = 2))

    # print(json.dumps(data_tree, indent = 4))

    # with open('mem_code/mem_tree.json', 'w') as json_file:
    #     json.dump(data_tree, json_file)

    # for node in data_tree.get_extension():
    #     if 'c_letter' in node.get_suff_marks():
    #         print(node.get_name())