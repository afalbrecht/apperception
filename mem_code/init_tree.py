import json
from mem_code import *


if __name__ == '__main__':

    tree = TreeNode('Root')
    tree.add_node(TreeNode('t_sensor', suff_marks=['obj_sensor']))
    tree.add_node(TreeNode('t_object'))
    tree.add_node(TreeNode('t_grid'))
    letter = tree.add_node(TreeNode('t_letter', suff_marks=['c_letter'])) #, ess_marks=['misc_predict_4_template_out.txt', 'misc_predict_4_interpret_mem.lp']))
    number = tree.add_node(TreeNode('t_number', suff_marks=['c_number'])) #, ess_marks=['misc_predict_4_num_template_out.txt', 'misc_predict_4_num_interpret_mem.lp']))
    number.add_node(TreeNode('0', suff_marks=['obj_number_0']))
    
    with open('memory/misc_predict_4_template_out.txt', 'r') as f:
        template = f.read()
        letter.set_ess_marks([template])
    
    with open('memory/misc_predict_4_interpret_mem.lp', 'r') as f:
        interpretation = f.read()
        letter.set_ess_marks(letter.get_ess_marks() + [interpretation])

    with open('memory/misc_predict_4_num_template_out.txt', 'r') as f:
        template = f.read()
        number.set_ess_marks([template])
    
    with open('memory/misc_predict_4_num_interpret_mem.lp', 'r') as f:
        interpretation = f.read()
        number.set_ess_marks(number.get_ess_marks() + [interpretation])

    print(recursive_traverse(tree, 'c_letteraospdifja'))

    with open('mem_code/mem_tree.json', 'w') as json_file:
        json.dump(tree, json_file)

    with open('mem_code/mem_tree.json', 'r') as f:
        data = json.load(f)
    data_tree = TreeNode.from_dict(data)
    # print(json.dumps(data_tree, indent = 4))

    for node in data_tree.get_extension():
        if 'c_letter' in node.get_suff_marks():
            print(node.get_name())