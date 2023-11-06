import json

class TreeNode(dict):
    def __init__(self, name, suff_marks=[], ess_marks=[], 
                acc_marks=[], disjunction=[], extension=None):
        super().__init__()
        self.__dict__ = self
        self.name = name
        self.suff_marks = suff_marks
        self.ess_marks = ess_marks
        self.acc_marks = acc_marks
        self.disjunction = disjunction
        self.extension = list(extension) if extension is not None else []
    
    def get_name(self):
        return self.name

    def get_suff_marks(self):
        return self.suff_marks
    
    def get_ess_marks(self):
        return self.ess_marks

    def get_acc_marks(self):
        return self.acc_marks

    def get_disjunction(self):
        return self.disjunction
    
    def get_extension(self):
        return self.extension
    
    def set_suff_marks(self, marks):
        self.suff_marks = marks

    def set_ess_marks(self, marks):
        self.ess_marks = marks
    
    def set_acc_marks(self, marks):
        self.acc_marks = marks

    def set_disjunction(self, disjunction):
        self.disjunction = disjunction

    def add_node(self, node):
        self.extension.append(node)
        return node

    def get_node(self, name):
        for n in self.get_extension():
            if n.get_name() == name:
                return n
            else:
                return None

    def get_node_names(self):
        return [n.get_name() for n in self.get_extension()]  

    @staticmethod
    def from_dict(dict_):
        """ Recursively (re)construct TreeNode-based tree from dictionary. """
        node = TreeNode(dict_['name'], dict_['suff_marks'], 
            dict_['ess_marks'], dict_['acc_marks'],
            dict_['disjunction'],  dict_['extension'])
#        node.extension = [TreeNode.from_dict(child) for child in node.extension]
        node.extension = list(map(TreeNode.from_dict, node.extension))
        return node

def check_input(marks, input):
    for mark in marks:
        if mark not in input:
            return False
    return True

def recursive_traverse(node, input):
    """Recursively walks through the tree and appends the essential marks 
    of each node found to the output"""
    output = []
    for child in node.get_extension():
        if check_input(child.get_suff_marks(), input):
            output += child.get_ess_marks()
            if child.get_extension() != []:
                output += recursive_traverse(child, input)
    return output
    
