import json
from mem_code import *

if __name__ == '__main__':

    tree = TreeNode('Parent')
    tree.children.append(TreeNode('Child 1'))
    child2 = TreeNode('Child 2')
    tree.children.append(child2)
    child2.children.append(TreeNode('Grand Kid'))
    child2.children[0].children.append(TreeNode('Great Grand Kid'))

    json_str = json.dumps(tree, indent=2)
    # print(json_str)
    # print()
    pyobj = TreeNode.from_dict(json.loads(json_str))  # reconstitute
    # print('pyobj class: {}'.format(pyobj.__class__.__name__))  # -> TreeNode
    # print(json.dumps(pyobj, indent=4))

    with open('mem_code/mem_tree.json', 'w') as json_file:
        json.dump(pyobj, json_file)

# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }



    with open('mem_code/mem_tree.json', 'r') as f:
        data = json.load(f)

    print(json.dumps(data, indent = 4))