import json
import copy
from itertools import combinations



class TreeNode():
    """ TreeNode defines a class for the memory tree 
    TreeNode defines the following attributes: 
    Name: name of the node 
        - String
    Permanents: permanents the object is involved in 
        - List
    Form of Intuition: whether the object is not a real 'object', but a structure 
    of a form of intuition, thus a moment in time or a part of space. 
        - None, Space or Time
    Exo flag: a flag to indicate that the object can be (or has been) treated as exogenous
        - True or False"""
    def __init__(self, name, objects=[], 
                concepts=[], extension=None):
        super().__init__()
        # self.__dict__ = self
        self.name = name
        # self.suff_marks = suff_marks
        # self.ess_marks = ess_marks
        # self.acc_marks = acc_marks
        # self.disjunction = disjunction
        self.objects = objects
        self.concepts = concepts
        self.extension = list(extension) if extension is not None else []
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent = 3) 

    def __repr__(self):
        return self.__str__()
    
    # Get functions
    def get_name(self):
        return self.name

    def get_objects(self):
        return self.objects
    
    def get_object_names(self):
        return [o.get_name() for o in self.objects]

    def get_concepts(self):
        return self.concepts
    
    def get_concept_names(self):
        return [c.get_name() for c in self.concepts]
    
    def get_extension(self):
        return self.extension

    # set functions    
    def set_objects(self, objects):
        self.objects = objects
    
    def set_concepts(self, concepts):
        self.concepts = concepts

    # Add functions
    def add_object(self, obj):
        if obj.get_name() not in self.get_object_names():
            self.objects = self.get_objects() + [obj]

    def add_concept(self, concept):
        add = True
        for c in self.concepts:
            if c.get_name() == concept.get_name():
                if c.get_types() == concept.get_types():
                    add = False
        if add:
            self.concepts = self.get_concepts() + [concept]
                
    def add_node(self, node):
        self.extension = self.get_extension() + [node]
        return node

    # Various complex functions
    def get_child_names(self):
        return [n.get_name() for n in self.get_extension()]

    def get_full_extension_names(self):
        output = []
        for node in self.get_extension():
            output += [node.get_name()]
            output += node.get_full_extension_names()
        return output
    
    def get_structure(self):
        output = []
        for i, node in enumerate(self.get_extension()):
            output += [[node.get_name()]]
            output[i] += node.get_structure()
        return output

    def get_pretty_structure(self, level=0):
        indent = "   " * level
        output = f"{indent}{self.name}\n"
        for child in self.get_extension():
            output += child.get_pretty_structure(level + 1)
        return output
    
    def get_node_by_name(self, name):
        if self.get_name() == name:
            return self
        for node in self.get_extension():
            result = node.get_node_by_name(name)
            if result is not None:
                return result
        return None

    def get_path_to_node(self, name):
        if self.get_name() == name:
            return []
        for node in self.get_extension():
            result = node.get_path_to_node(name)
            if result is not None:
                return result + [node.get_name()]
        return None

    def get_node_depth(self, name):
        return len(self.get_path_to_node(name))
    
    def get_node_by_object(self, object_name):
        if object_name in self.get_object_names():
            return self
        for node in self.get_extension():
            result = node.get_node_by_object(object_name)
            if result is not None:
                return result
        return None

    def get_object_by_name(self, object_name):
        for obj in self.get_objects():
            if obj.get_name() == object_name:
                return obj
        return None
    
    def get_nodes_by_concept(self, concept_name, output=[]):
        if concept_name in self.get_concept_names():
            output = output + [self.get_name()]    
        for node in self.get_extension():
            output = node.get_nodes_by_concept(concept_name, output)
        return output

    def get_node_pairs_by_concept(self, concept_name, output=[]):
        if concept_name in self.get_concept_names():
            types = self.get_concept_by_name(concept_name).get_types()
            if types not in output:
                output = output + [types]    
        for node in self.get_extension():
            output = node.get_node_pairs_by_concept(concept_name, output)
        return output

    def get_concept_by_name(self, concept_name):
        for concept in self.get_concepts():
            if concept.get_name() == concept_name:
                return concept
        return None

    def set_objects_to_form_of_intuition(self):
        for object in self.get_objects():
            object.set_form_of_intuition(True)

    # Construct a dictionary containing the nodes by name
    def get_n_n_dict(self):
        output = {}
        for node in self.get_extension():
            output[node.get_name()] = node
            output.update(node.get_n_n_dict())
        return output

    def to_dict(self):
        return {
            "name": self.name,
            "objects": [object.to_dict() for object in self.objects],
            "concepts": [concept.to_dict() for concept in self.concepts],
            "extension": [node.to_dict() for node in self.extension]
        }

    @staticmethod
    def from_dict(dict_):
        """ Recursively (re)construct TreeNode-based tree from dictionary. """
        node = TreeNode(dict_['name'], dict_['objects'],
            dict_['concepts'], dict_['extension'])
#        node.extension = [TreeNode.from_dict(child) for child in node.extension]
        node.extension = list(map(TreeNode.from_dict, node.extension))
        return node


class Concept():
    """ Concept defines a class for the different possible concepts (permanent,
    fluid, static etc.) 
    Concept defines the following attributes: 
    Name: name of the concept
        - String
    Concept: TODO: decide on whether to use this, maybe for defining reflexivity etc.
    Types: the types of the objects over which the concept is defined
        - List of types
    Sort: flag to indicate whether the concept is fluid or static
        - None, Fluid or Static
    Construct: flag to indicate whether a permanent concept is Given or Constructed
        - None, Given or Constructed 
    Exo flag: a flag to indicate that the concept can be (or has been) treated as exogenous
        - True or False
    Rules: a list containing Rules in which this concept figures"""
    def __init__(self, name, concept=None,
                types=[], sort=None,
                construct=None, exo_flag=False,
                rules=[]):
        super().__init__()
        # self.__dict__ = self
        self.name = name
        self.concept = concept
        self.types = types
        self.sort = sort
        self.construct = construct
        self.exo_flag = exo_flag
        self.rules = rules

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "name": self.name,
            "concept": self.concept,
            "types": self.types,
            "sort": self.sort,
            "construct": self.construct,
            "exo_flag": self.exo_flag,
            "rules": [rule.to_dict() for rule in self.rules]
        }

    # Get functions
    def get_name(self):
        return self.name

    def get_concept(self):
        return self.concept

    def get_types(self):
        return self.types

    def get_sort(self):
        return self.sort

    def get_construct(self):
        return self.construct

    def is_exo_flag(self):
        return self.exo_flag
    
    def get_rules(self):
        return self.rules
    
    def get_rule_heads(self):
        return [rule.get_head() for rule in self.rules]

    # Set functions
    def set_name(self, name):
        self.name = name
    
    def set_concept(self, concept):
        self.concept = concept

    def set_types(self, types):
        self.types = types

    def set_sort(self, sort):
        self.sort = sort

    def set_construct(self, construct):
        self.construct = construct

    def set_exo_flag(self, exo_flag):
        self.exo_flag = exo_flag

    def set_rules(self, rules):
        self.rules = rules
    
    def add_rule(self, rule):
        add = True
        head_body = [rule.get_head()] + rule.get_body()
        for r in self.get_rules():
            if head_body == [r.get_head()] + r.get_body():
                add = False
        if add:
            self.rules = self.rules + [rule]
        return add
    
    def is_permanent(self):
        if self.get_construct() == None:
            return False
        return True






class Object():
    """ Object defines a class for the various objects instantiated in the AE environment,
    which allows the memory tree to track which permanent concepts are associated with 
    which objects.
    Object defines the following attributes: 
    Name: name of the object 
        - String
    Permanents: permanents the object is involved in 
        - List
    Form of Intuition: whether the object is not a real 'object', but a structure 
    of a form of intuition, thus a moment in time or a part of space. 
        - None, Space or Time
    Exo flag: a flag to indicate that the object can be (or has been) treated as exogenous
        - True or False
    """
    def __init__(self, name, type=None, permanents=[],
                form_of_intuition=None, exo_flag=False):
        super().__init__()
        self.name = name
        self.type = type
        self.permanents = permanents
        self.form_of_intuition = form_of_intuition
        self.exo_flag = exo_flag

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "permanents": self.permanents,
            "form_of_intuition": self.form_of_intuition,
            "exo_flag": self.exo_flag
        }

    # Get functions
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    def get_permanents(self):
        return self.permanents

    def get_form_of_intuition(self):
        return self.form_of_intuition

    def is_exo_flag(self):
        return self.exo_flag

    # Set functions
    def set_name(self, name):
        self.name = name
    
    def set_type(self, type):
        self.type = type
    
    def set_permanents(self, permanents):
        self.permanents = permanents
    
    def add_permanent(self, permanent):
        if permanent not in self.permanents:
            self.permanents = self.get_permanents() + [permanent]

    def set_form_of_intuition(self, form_of_intuition):
        self.form_of_intuition = form_of_intuition

    def set_exo_flag(self, exo_flag):
        self.exo_flag = exo_flag




class Rule():
    """ Object defines a class for the various objects instantiated in the AE environment,
    which allows the memory tree to track which permanent concepts are associated with 
    which objects.
    Object defines the following attributes: 
    Name: name of the object 
        - String
    Permanents: permanents the object is involved in 
        - List
    Form of Intuition: whether the object is not a real 'object', but a structure 
    of a form of intuition, thus a moment in time or a part of space. 
        - None, Space or Time
    Exo flag: a flag to indicate that the object can be (or has been) treated as exogenous
        - True or False
    """
    def __init__(self, head=[], body=[],
                concepts=[], types=[]):
        super().__init__()
        self.head = head
        self.body = body
        self.concepts = concepts
        self.types = types

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "head": self.head,
            "body": self.body,
            "concepts": self.concepts,
            "types": self.types
        }

     # Get functions
    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_concepts(self):
        return self.concepts

    def get_types(self):
        return self.types

    # Set functions
    def set_head(self, new_head):
        self.head = new_head
        return self

    def set_body(self, new_body):
        self.body = new_body
        return self

    def set_concepts(self, new_concepts):
        self.concepts = new_concepts
        return self

    def set_types(self, new_types):
        self.types = new_types
        return self

    def add_to_body(self, line):
        if line not in self.get_body():
            self.body = self.body + [line]
        return self
    
    def add_concept_types(self, line):
        """Splits and strips the rule line to add the concepts and 
        types contained in the line to the Rule attributes,
        concepts are saved as tuples or triples of the form
        [concept, type] or [concept, type, type]"""\

        split_line = line.replace(")).","").split("(")[2].split(",")
        concept = split_line[0]
        types = [f"t_{'_'.join(var.split('_')[1:-1])}" for var in split_line[1:]]
        conc_types = [concept] + types

        if conc_types not in self.concepts:
            self.concepts = self.concepts + [conc_types]
            for type in types:
                if type not in self.types:
                    self.types = self.types + [type]

        return self







#---------------------------------------------------------------------
# Functions for the input side of memory, thus traversing the tree 
# and giving a template + interpretation as output
#---------------------------------------------------------------------

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




    
#---------------------------------------------------------------------
# Functions for the output side of memory, thus for reading in the 
# template and interpretation given by the haskell+clingo program for 
# a given input, and then adding these to the memory tree in the right
# location
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Converting a template_out file to a usable dict
#---------------------------------------------------------------------

def template_to_dict(template):
    """Generate the initial dictionary from a temple_out file"""
    output = {}
    for line in template:
        if '=' in line:
            key, value = line.replace('\n', '').split(' = ')
            output[key] = value
    return process_dict(output)
            
def process_dict(temp_dict):
    """Process the initial dictionary to a full fledged template dictionary to 
    be used for updating the memory tree"""
    temp_dict['types'] = catch_empty(temp_dict['types'].strip('[]').split(','))
    temp_dict['type_hierarchy'] = process_hierarchy(temp_dict['type_hierarchy'])
    temp_dict['objects'] = process_objects(temp_dict['objects'])
    temp_dict['exogeneous_objects'] = catch_empty(temp_dict['exogeneous_objects'].strip('[]').split(','))
    temp_dict['permanent_concepts'] = process_perms(temp_dict['permanent_concepts'])
    temp_dict['fluid_concepts'] = process_hierarchy(temp_dict['fluid_concepts'])
    temp_dict['input_concepts'] = catch_empty(temp_dict['input_concepts'].strip('[]').split(','))
    temp_dict['static_concepts'] = catch_empty(temp_dict['static_concepts'].strip('[]').split(','))
    temp_dict['vars'] = process_objects(temp_dict['vars'])
    temp_dict['var_groups'] = catch_empty([x.split(',') for x in temp_dict['var_groups'].strip('[]').split('],[')])
    return temp_dict

def process_hierarchy(hierarchy):
    if hierarchy == '[]':
        return []
    output = {}
    temp = hierarchy.strip('[]()').split('),(')
    for h in temp:
        k, v = h.strip(']').split(',[')
        output[k] = [x for x in v.split(',')]
    return output

def process_objects(objects):
    if objects == '[]':
        return []
    output = {}
    temp = objects.strip('[]()').split('),(')
    for o in temp:
        v, k = o.split(',')
        if k in output:
            output[k].append(v)
        else:
            output[k] = [v]
    return output

# Convert list with empty string to empty list
def catch_empty(l):
    if l == ['']:
        return []
    else: return l

def process_perms(perms):
    if perms == '[]':
        return []
    output = []
    temp = perms.replace('[', '').replace(']', '').strip('()').split('),(')
    for p in temp:
        p_split = p.split(',')
        output.append(Concept(p_split[0], construct=p_split[1], types=p_split[2:]))
    return output






#---------------------------------------------------------------------
# Functions for adding the entries to the template dict to a memory tree
#---------------------------------------------------------------------

#TODO: make this code safe by continually returning the tree?
def update_tree_template(tree, template):
    """Update the tree using the template dictionary"""
    x = update_type_hierarchy(tree, template)
    update_types(tree, template)
    update_objects(tree, template)
    update_fluid_concepts(tree, template)
    update_permanent_concepts(tree, template)


# Add types to the tree, according to the hierarchy given in the template
def update_type_hierarchy(tree, template):
    for t in template['type_hierarchy']:
        present_types = tree.get_full_extension_names()
        if t not in present_types:
            node = tree.add_node(TreeNode(t))
        for e in template['type_hierarchy'][t]:
            if e not in present_types:
                tree.get_node_by_name(t).add_node(TreeNode(e))
    return tree

# Add types to tree, if there is no hierarchical ordering present
def update_types(tree, template):
    present_types = tree.get_full_extension_names()
    for t in template['types']:
        if t not in present_types:
            tree.add_node(TreeNode(t))

# Add objects as accidental marks to their corresponding types
def update_objects(tree, template):
    for key in template['objects']:
        n = tree.get_node_by_name(key)
        if n is not None:
            for obj in template['objects'][key]:
                n.add_object(Object(obj, type=n.get_name()))

# Add fluid concepts to their corresponding type
def update_fluid_concepts(tree, template):
    for concept, types in template['fluid_concepts'].items():
        for t in types:
            node = tree.get_node_by_name(t)
            node.add_concept(Concept(concept, types=types, sort='fluid'))

def update_permanent_concepts(tree, template):
    for concept in template['permanent_concepts']:
        for t in concept.get_types():
            node = tree.get_node_by_name(t)
            node.add_concept(concept)






#---------------------------------------------------------------------
# Functions for updating the memory tree with the interpret_mem file
#---------------------------------------------------------------------

# TODO: Add way to add rules to the mem_tree, in concert with variables of course
def convert_interpret_mem(inter):
    """Parses the interpret_mem file to convert the relevant lines,
    fact statements for permanent assignments for a p_ function into a neat list,
    and the rules into a dict with the rule index (r1, r2, etc) as keys and the 
    a list of lines with the corresponding rule index as values"""
    perms = []
    rules = {}
    for line in inter:
        if line.startswith("permanent(isa2(p_"):
            t = strip_string(line.replace("permanent(isa2(", "")).split(",")
            perms = perms + [t]
        if line.startswith("permanent(isa(p_"):
            t = strip_string(line.replace("permanent(isa(", "")).split(",")
            perms = perms + [t]
        if line.startswith("rule_"):
            rule_index = f"r{line.split('(r')[1].split(',')[0]}"
            if rule_index not in rules.keys():
                rules[rule_index] = []
            rules[rule_index] = rules[rule_index] + [line.replace("\n","")]
    return perms, rules

def strip_string(str):
    return str.replace(")", "").replace(".", "").replace("\n", "")

def update_tree_interpret(tree, inter, temp_dict):
    """Adds permanents and rules from interpret_mem file to the 
    right location in the memory tree"""
    perms, rules = convert_interpret_mem(inter)
    tree = update_perms(tree, perms)
    tree = update_rules(tree, rules, temp_dict)
    return tree

def update_perms(tree, perms):
    """Adds permanents to the memory tree"""
    for perm in perms:
        for obj in perm[1:]:
            node = tree.get_node_by_object(obj)
            for o in node.get_objects():
                if o.get_name() == obj:
                    o.add_permanent(perm)
    return tree

def update_rules(tree, rules, temp_dict):
    """Adds rules to the memory tree"""

    seen_vars = {}
    seen_types = set()
    for index in rules.keys():
        rule = Rule()

        for line in rules[index]:
            var_line, seen_vars, seen_types = replace_vars(line, temp_dict, seen_vars, seen_types)
            if var_line.startswith("rule_head") or var_line.startswith("rule_arrow"):
                rule = rule.set_head(var_line.replace(index, "ruleindex"))
            else:
                rule = rule.add_to_body(var_line.replace(index, "ruleindex"))
            rule = rule.add_concept_types(var_line)

        for c in rule.get_concepts():
            if not c[0].startswith("p_"):
                for node in tree.get_nodes_by_concept(c[0]):
                    concept = tree.get_node_by_name(node).get_concept_by_name(c[0])
                    concept.add_rule(rule)

    return tree

def replace_vars(line, temp_dict, seen_vars, seen_types):
    """ Replace the variables in the lines of the rules with conventional 
    names that encode the types in the name, like var_object_1 instead of var_x.
    Also replace the rule indices like r1, r2 with 'ruleindex' """
    # TODO: Note that the variable for now only works with 2 variables of the same type,
    # to add more variables this code should be amended

    index = "1"
    for type in temp_dict["vars"].keys():
        for var in temp_dict["vars"][type]:
            if var in line:
                if var in seen_vars.keys():
                    encoded_var = seen_vars[var]
                else:
                    if type in seen_types:
                        index = "2"
                    encoded_var = f"var_{type[2:]}_{index}"
                    seen_vars[var] = encoded_var
                line = line.replace(var + ',', encoded_var + ',')
                line = line.replace(var + ')', encoded_var + ')')
                seen_types.add(type)


    return line, seen_vars, seen_types


#---------------------------------------------------------------------
# Functions for the input side of memory, thus for comparing the input
# to the entries in the memory tree to construct a template and 
# interpretation file usable by the haskell+clingo combination
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Functions for retrieving a template from a memory tree
#---------------------------------------------------------------------

def build_template(tree, input, senses):
    """Constructor function for building a template and interpretion dict
    to be converted into a template_in file and an interpret_mem file"""

    temp_dict = {'types':[], 'objects':[], 'concepts':[], 'type_hierarchy':[],
             'constraints':[]}

    temp_dict = add_space_cells(tree, input, temp_dict)
    temp_list = [temp_dict]
    temp_list = iterative_senses(senses, temp_list, tree)
    output = []
    # for t in temp_list:
    #     t_list = add_speculative_concepts(tree, senses, t)        
    #     for t0 in t_list:
    #         t0_list = add_hierarchy_types(tree, senses, t0)
    #         for t1 in t0_list:
    #             output = output + add_apriori_objects(tree, senses, t1)
    for t in temp_list:
        t_list = add_speculative_concepts(tree, senses, t)#[1:]        
        for t0 in t_list:
            t0_list = add_hierarchy_types(tree, senses, t0)[1:]
            for t1 in t0_list:
                output = output + add_apriori_objects(tree, senses, t1)[:-1]
    # for i, o in enumerate(output):

    # output = output + [add_apriori_objects(tree, senses, o) for o in output]
    # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # for o in output:
    #     print([t.get_name() for t in o["objects"]])
    
    output = [construct_hierarchy(tree, o) for o in output]
    # output = [add_apriori_objects(tree, senses, o) for o in output]

    # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # for o in output:
    #     print([t.get_name() for t in o["objects"]])

    return output

def add_hierarchy_types(root, senses, temp_dict):
    """Adds the types to the temp_dict positioned above the types found in 
    recursive senses, as well as the types and concepts associated with these
    types."""

    minimal = copy.deepcopy(temp_dict)
    apriori = copy.deepcopy(temp_dict)
    # extended = copy.deepcopy(temp_dict)
    for type in apriori["types"]:
        for t in root.get_path_to_node(type):
            if t not in apriori["types"]:
                apriori["types"] = apriori["types"] + [t]
                # extended["types"] = extended["types"] + [t]
                apriori = fill_type(root, root.get_node_by_name(t), apriori)
                # extended = fill_type(root, root.get_node_by_name(t), extended, extend=True)

    return [minimal, apriori]

def add_speculative_concepts(root, senses, temp_dict):
    """Adds the types to the temp_dict positioned above the types found in 
    recursive senses, as well as the types and concepts associated with these
    types."""

    output = copy.deepcopy(temp_dict)
    for type in temp_dict["types"]:
        temp_dict = fill_type(root, root.get_node_by_name(type), temp_dict, extend=True)

    return [output, temp_dict]

def add_apriori_objects(root, senses, temp_dict):
    """Adds each object with the form of intuition tag as True contained under
    the present types to the output. These objects represent parts/structures 
    of the a priori form of intuition in question."""

    output = copy.deepcopy(temp_dict)
    for type in temp_dict["types"]:
        temp_dict = fill_type(root, root.get_node_by_name(type), temp_dict, apriori_forms=True)

    return [output, temp_dict]

# TODO: fix hoe het gedaan wordt met reflexieve concepten 
def fill_type(root, node, output, extend=False, apriori_forms=False):
    """Adds concepts from the type selected in the tree to the template file
    if not already present in the output, which also prompts it to add 
    the other types present in the concept"""

    for concept in node.get_concepts():
        if not is_concept_in_list(concept, output['concepts']):
            if set(concept.get_types()).issubset(output['types']) and\
                (concept.is_permanent() or extend):
                output['concepts'] = output['concepts'] + [concept]
            elif apriori_forms: # Ik denk stiekem dat deze else een tab naar links moet
                output = add_extra_types(root, concept, output)

    return output

def add_extra_types(root, concept, output):
    """Adds types and objects to the template that haven't been seen in the input,
    these can be hypothetical types that are added in some templates and removed
    in others, or apriori types that are involved in the forms of intuition like space
    and time."""

    for type in concept.get_types():
        if type not in output["types"]:
            node = root.get_node_by_name(type)
            for obj in node.get_objects():
                if obj.get_form_of_intuition() == True:
                    if type not in output["types"]:
                        output["types"] = output["types"] + [type]
                    if not is_concept_in_list(concept, output['concepts']):
                        output["concepts"] = output["concepts"] + [concept]
                    output["objects"] = output["objects"] + [obj]
                    output = fill_type(root, node, output)

    return output


def recursive_senses(node, senses, output, root, count=0):
    """Recursively walks through the tree and appends the essential marks 
    of each node that has sufficient marks present in the input to the output"""

    for child in node.get_extension():
        output = check_senses(child, senses, output, root)
        output = fill_type(root, child, output)
        # count = count + add
        # if count == len(senses):
        #     return output, count
        if child.get_extension() != []:
            output = recursive_senses(child, senses, output, root, count)
    return output

def iterative_senses(senses, output, root, index=0, concept_dict={}):

    if index == len(senses):
        return output
    fact = senses[index]
    print(fact)
    node_pairs = root.get_node_pairs_by_concept(fact[0])
    print(node_pairs)
    node_pairs = strip_pairs(node_pairs, fact, root)
    print(node_pairs)
    all_nodes = root.get_nodes_by_concept(fact[0])
    nodes = select_lowest_nodes(root, all_nodes)

    # TODO: figure out what do do when the concept is not known, but the objects are
    if all_nodes == []:
        # output = [iter_add_new_concept(fact, output[0], root)]
        output = iterative_senses(senses, output, root, index + 1)

    # If the amount of possible types found corresponds to the amount of types in the 
    # fact, then there is only one possible concept to be used.
    elif len(node_pairs) == 1: #len(node) == len(fact) - 1:
        # print("Only possible type(s) for the concept:")
        # print(nodes)
        for pair in node_pairs:
            for n in pair:
                node = root.get_node_by_name(n)
                concept = node.get_concept_by_name(fact[0])
                output = [iter_add_type_concept(concept, fact, output[0], root)]
                # print([c.get_name() for c in output[0]['concepts']])
                output = [iter_fill_type(root, node, output[0])]
                # print([c.get_name() for c in output[0]['concepts']])
        output = iterative_senses(senses, output, root, index + 1, concept_dict)
        # print([c.get_name() for c in output[0]['concepts']])
    
    # If the concept in the fact has been seen at an earlier stage and the objects
    # in the fact can be subsumed under the types in the concept then we continue
    # with building the specific template
    elif len(fact_check(root, fact, output[0])) > 0:
        print("Concept or both objects have been seen earlier:")
        # print(nodes)
        for type in fact_check(root, fact, output[0]):
            print(fact[0])
            # print(type)
            node = root.get_node_by_name(type)
            concept = node.get_concept_by_name(fact[0])
            output = [iter_add_type_concept(concept, fact, output[0], root)]
            output = [iter_fill_type(root, node, output[0])]
        output = iterative_senses(senses, output, root, index + 1, concept_dict)

    # TODO: Fix this for binary concepts where there can thus be 4 types for a concept 
    # FIXED (i think)
    else:
        recur = []


        print("Going to iterate over the following nodepairs:")
        print(node_pairs)
        # for n in nodes:
        for pair in node_pairs:     
            for n in pair:       
                # print("----Iter step----")
                # print(index)
                # print(n)
                node = root.get_node_by_name(n)
                poss_output = copy.deepcopy(output)
                concept = node.get_concept_by_name(fact[0])
                print("This concept will be added to the dict:")
                print(fact[0])
                print("This type with these objects will be added to the dict:")
                print(n, node.get_object_names())
                poss_output = [iter_add_type_concept(concept, fact, poss_output[0], root)]
                poss_output = [iter_fill_type(root, node, poss_output[0])]
            recur = recur + iterative_senses(senses, poss_output, root, index + 1, concept_dict)
        output = recur    

    return output


def iter_add_new_concept(fact, output, root):
    """Adds a concept to the template which is not present in the memory tree
    if the objects present in the fact are known."""

    # TODO: add this functionality

    return output




def strip_pairs(pairs, fact, root):
    """ Strips node pairs of types that do not correspond to the objects
    in the facts"""

    output = []
    for pair in pairs:
        if len(pair) == 1:
            if fact[1] in root.get_node_by_name(pair[0]).get_object_names():
                output = output + [pair]
        else:
            n0 = root.get_node_by_name(pair[0])
            n1 = root.get_node_by_name(pair[1])
            # This is a hacky way to get a priori objects into the template, which can
            # in principle be made nicer but for it to actually be cleaner requires 
            # a larger overhaul. This is not future proof for that overhaul though. 
            if (fact[1] in n0.get_object_names() or "cell" in fact[1]) and \
                (fact[2] in n1.get_object_names() or "cell" in fact[2]):
                output = output + [pair]
    
    return output


def select_lowest_nodes(root, nodes):
    """ Checks if any of the nodes in the list lies in the extension of 
    any of the other nodes, and from these two nodes selects the lowest nodes
    on the basis of the 'specificity assumption' """

    output = copy.deepcopy(nodes)
    
    for node in nodes:
        path = root.get_path_to_node(node)
        for n in path[1:]:
            if n in nodes:
                output.remove(n)
    
    output = nodes
    return output
                

def fact_check(root, fact, temp_dict):
    """ Returns a list of the types of the concept or object in the fact if the
    concept or the object has already been assigned a type"""

    output = []

    # Returns a list of the types of the concept if the concept has already been
    # assigned in the temp_dict
    for concept in temp_dict["concepts"]:
        if fact[0] == concept.get_name():
            types = concept.get_types()
            if len(types) != len(fact) - 1:
                continue
            for i, type in enumerate(types):
                node = root.get_node_by_name(type)
                if fact[i+1] not in node.get_object_names():
                    continue
            print("The concept has been seen earlier")
            print(concept.get_name())
            return types
    
    # Returns a list of the types of the objects if the objects have already been assigned
    # a type in the temp_dict, but the concept has not been added yet.
    for obj in fact[1:]:
        if obj not in [o.get_name() for o in temp_dict["objects"]]:
            print("This object has not been seen yet:")
            print(obj)
            return []
        else:
            print("This object has been seen:")
            print(obj)
            output = output + [o.get_type() for o in temp_dict["objects"] if o.get_name() == obj]

    # print("These objects have been seen earlier:")
    # print(output)
    return output


# TODO: Moet dit een stuk beter fixen voor reflexive concepts en gewoon concepts waar de 
# types omgewisseld zijn voor onbeduidende redenen. Sowieso moet ik wat doen aan concepts
# met arbitrair omgewisselde types die niet reflexief zijn etc etc
def iter_add_type_concept(concept, fact, output, root):
    """Adds concepts, objects and types to template file, if it can find the the objects
    it encounters in the senses facts in the memory tree"""
    t = concept.get_types()
    # print(output)
    # If the senses fact holds a singleton concept
    if len(fact) == 2:
        # print("JA")
        node = root.get_node_by_name(t[0])
        # print(node.get_name())
        # print(node.get_object_names())
        # print(fact[1])
        if fact[1] in node.get_object_names():
            # print("NEE")

            # Add type to output if the type is not already present
            if node.get_name() not in output['types']:
                output['types'] = output['types'] + [node.get_name()]

            # Add object to output if the object is not already present
            obj = node.get_object_by_name(fact[1])
            if fact[1] not in [o.get_name() for o in output['objects']]:
                # print("The following object has been added to the dict:")
                # print(obj.get_name())
                output['objects'] = output['objects'] + [obj]

            # Add concept to output if the concept is not already present
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]
        
        # Add object that is not present in tree to temp_dict 
        # TODO: Slightly incomplete now, as it only adds the object if the type has already been seen,
        # but the type could of course be seen only later
        else:
            # if node.get_name() in output['types']:
            if fact[1] not in [o.get_name() for o in output['objects']]:
                obj = Object(fact[1], type=node.get_name())
                print("The following object not present in the tree has been added to the dict:")
                print(obj.get_name())
                output['objects'] = output['objects'] + [obj]
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]

    # If the senses fact holds a binary concept            
    if len(fact) == 3:
        n0 = root.get_node_by_name(t[0])
        n1 = root.get_node_by_name(t[1])
        if fact[1] in n0.get_object_names() and fact[2] in n1.get_object_names():

            # Add type to output if the type is not already present
            if n0.get_name() not in output['types']:
                output['types'] = output['types'] + [n0.get_name()]
            if n1.get_name() not in output['types']:
                output['types'] = output['types'] + [n1.get_name()]

            # Add object to output if the object is not already present    
            obj = n0.get_object_by_name(fact[1])
            if fact[1] not in [o.get_name() for o in output['objects']]:
                output['objects'] = output['objects'] + [obj]
            obj = n1.get_object_by_name(fact[2])
            if fact[2] not in [o.get_name() for o in output['objects']]:
                output['objects'] = output['objects'] + [obj]

            # Add concept to output if the concept is not already present    
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]

        # Add object that is not present in tree to temp_dict (speculative)
        else:
            # if node.get_name() in output['types']:
            if fact[1] not in [o.get_name() for o in output['objects']]:
                obj = Object(fact[1], type=n0.get_name())
                output['objects'] = output['objects'] + [obj]
                print("The following object not present in the tree has been added to the dict:")
                print(obj.get_name())
            if fact[2] not in [o.get_name() for o in output['objects']]:
                obj = Object(fact[2], type=n1.get_name())
                output['objects'] = output['objects'] + [obj]
                print("The following object not present in the tree has been added to the dict:")
                print(obj.get_name())  
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]

    return output 


# TODO: fix hoe het gedaan wordt met reflexieve concepten 
def iter_fill_type(root, node, output):
    """Adds concepts from the type selected in the tree to the template file
    if not already present in the output, which also prompts it to add 
    the other types present in the concept"""

    for concept in node.get_concepts():
        if not is_concept_in_list(concept, output['concepts']):
            if set(concept.get_types()).issubset(output['types']) and\
                concept.is_permanent():
                output['concepts'] = output['concepts'] + [concept]
            # else:
            #     output = iter_add_extra_types(root, concept, output)
    #         # TODO: Add a way to add concepts here whose types are not yet present in the 
    #         # input, but can still be added by virtue of them being possible solutions
    #         # or just a priori anschauungsformen like space and time etc

    return output

def iter_add_extra_types(root, concept, output):
    """Adds types and objects to the template that haven't been seen in the input,
    these can be hypothetical types that are added in some templates and removed
    in others, or apriori types that are involved in the forms of intuition like space
    and time."""

    for type in concept.get_types():
        if type not in output["types"]:
            node = root.get_node_by_name(type)
            for obj in node.get_objects():
                if obj.get_form_of_intuition() == True:
                    if type not in output["types"]:
                        output["types"] = output["types"] + [type]
                    output["objects"] = output["objects"] + [obj]
                    output = fill_type(root, node, output)

    return output





def is_concept_in_list(concept, conc_list):
    """Checker for fill_type to see if concept is in list"""
    con_dict = concept.to_dict()
    for c in conc_list:
        temp = True
        for k, v in c.to_dict().items():
            if con_dict[k] != v:
                temp = False
        if temp:
            return True

def check_senses(node, senses, output, root):
    """Adds node with essential marks to output if a concept contained under the 
    node is present in the senses facts glossed from the input"""
    # add = 0
    # filled = []
    for concept in node.get_concepts():
        for fact in senses:
            if concept.get_name() == fact[0]:
                # poss_nodes = get_nodes_by_concept(fact[0])
                # for poss_node in poss_nodes:
                #     poss_conc = poss_node.get_concept_by_name[fact[0]]
                #     # new_dict = 
                output = add_type_concept(concept, fact, output, root)
                # filled = filled + [fact]
                # add = add + 1
    return output


# TODO: Moet dit een stuk beter fixen voor reflexive concepts en gewoon concepts waar de 
# types omgewisseld zijn voor onbeduidende redenen. Sowieso moet ik wat doen aan concepts
# met arbitrair omgewisselde types die niet reflexief zijn etc etc
def add_type_concept(concept, fact, output, root):
    """Adds concepts, objects and types to template file, if it can find the the objects
    it encounters in the senses facts in the memory tree"""
    t = concept.get_types()

    # If the senses fact holds a singleton concept
    if len(fact) == 2:
        node = root.get_node_by_name(t[0])
        if fact[1] in node.get_object_names():

            # Add type to output if the type is not already present
            if node.get_name() not in output['types']:
                output['types'] = output['types'] + [node.get_name()]

            # Add object to output if the object is not already present
            obj = node.get_object_by_name(fact[1])
            if fact[1] not in [o.get_name() for o in output['objects']]:
                output['objects'] = output['objects'] + [obj]

            # Add concept to output if the concept is not already present
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]

    # If the senses fact holds a binary concept            
    if len(fact) == 3:
        n0 = root.get_node_by_name(t[0])
        n1 = root.get_node_by_name(t[1])
        if fact[1] in n0.get_object_names() and fact[2] in n1.get_object_names():

            # Add type to output if the type is not already present
            if n0.get_name() not in output['types']:
                output['types'] = output['types'] + [n0.get_name()]
            if n1.get_name() not in output['types']:
                output['types'] = output['types'] + [n1.get_name()]

            # Add object to output if the object is not already present    
            obj = n0.get_object_by_name(fact[1])
            if fact[1] not in [o.get_name() for o in output['objects']]:
                output['objects'] = output['objects'] + [obj]
            obj = n1.get_object_by_name(fact[2])
            if fact[2] not in [o.get_name() for o in output['objects']]:
                output['objects'] = output['objects'] + [obj]

            # Add concept to output if the concept is not already present    
            if not is_concept_in_list(concept, output["concepts"]):
                output['concepts'] = output['concepts'] + [concept]

    return output 

def parse_input(input):
    """Parses the input string to isolate the "senses" facts 
    and converts them to neat lists"""
    output = []
    for line in input.splitlines():
        if line.startswith("senses(s2("):
            t = line.replace("senses(s2(", "").replace(")", "").replace(" ", "").split(",")
            output = output + [t[:3]]
        if line.startswith("senses(s("):
            t = line.replace("senses(s(", "").replace(")", "").replace(" ", "").split(",")
            output = output + [t[:2]]
        if line.startswith("exogenous(s2("):
            t = line.replace("exogenous(s2(", "").replace(")", "").replace(" ", "").split(",")
            output = output + [t[:3]]
        if line.startswith("exogenous(s("):
            t = line.replace("exogenous(s(", "").replace(")", "").replace(" ", "").split(",")
            output = output + [t[:2]]
    return output

def add_space_cells(tree, input, temp_dict):
    """ Workaround function to add the pregiven spatial structure to the temp_dict,
    should be replaced when the spatial structure is generated procedurally"""

    t_cell = tree.get_node_by_name("t_cell")
    for line in input.splitlines():
        if line.startswith("is_cell(") and t_cell != None:
            if "t_cell" not in temp_dict['types']:
                temp_dict["types"] = temp_dict["types"] + ["t_cell"]
            o = line.replace("is_cell(", "").replace(").", "")
            obj = t_cell.get_object_by_name(o)
            if obj == None:
                obj = Object(name=o, type="t_cell", form_of_intuition=True)
            temp_dict["objects"] = temp_dict["objects"] + [obj]
    
    return temp_dict

def construct_hierarchy(tree, temp_dict):
    """Constructs the type_hierarchy entry in the template by checking which
    added types are children of which other types"""    
    for type in temp_dict["types"]:
        node = tree.get_node_by_name(type)
        children = []
        for t in node.get_child_names():
            if t in temp_dict["types"]:
                children = children + [t]
        if children != []:
            h_string = f"({type},{to_string(children)})"
            temp_dict["type_hierarchy"] = temp_dict["type_hierarchy"] + [h_string]
    return temp_dict







#---------------------------------------------------------------------
# Functions for converting the template dict retrieved from the 
# memory tree into a template_in document
#---------------------------------------------------------------------

# def build_template(tree, input, senses):
#     """Constructor function for building a template_dict to be converted into 
#     a template_in file"""
#     output = {'types':[], 'objects':[], 'concepts':[], 'type_hierarchy':[]}
#     output, _ = recursive_senses(tree, input, senses, output, tree)
#     return output

def mem_to_template(temp_dict, dir, name):
    """Converts a template dict to a template_in file"""
    start = f"% {dir}_{name}\n\n"
    temp_stats = gen_temp_stats(temp_dict, dir, name)
    frame = gen_frame(temp_dict, dir, name)
    return start + temp_stats + frame

# TODO: Fix exogeneous objects and static_concepts + vars when working on interpretation
def gen_frame(temp_dict, dir, name):
    """Uses the template dict to generate the frame part of the template_in file"""
    perm_concepts, fluid_concepts, input_concepts = stringify_concepts(temp_dict["concepts"])
    vars, var_groups = construct_vars_and_groups(temp_dict["concepts"])

    output = f"""\n\n% Frame
types = {to_string(temp_dict["types"])}
type_hierarchy = {to_string(temp_dict["type_hierarchy"])}
objects = {to_string(stringify_objects(temp_dict["objects"]))}
exogeneous_objects = []
permanent_concepts = {to_string(perm_concepts)}
fluid_concepts = {to_string(fluid_concepts)}
input_concepts = {to_string(input_concepts)}
static_concepts = {gen_static_concepts(input_concepts, dir)}
vars = {to_string(vars)}
var_groups = {to_string(var_groups)}
aux_files = []""" #"{dir}_{name}/{dir}_{name}_interpret_mem_0_0.lp"

    return output

def gen_static_concepts(input_concepts, dir):
    if "sok" in dir and "c_p1" in input_concepts:
        return "[c_p1,c_p2,c_p3,c_p4]"
    else:
        return "[]"

# TODO: improve the input_concepts part by adding a concept attribute to the Concept class
def stringify_concepts(concepts):
    perm_concepts = []
    fluid_concepts = []
    input_concepts = []

    for c in concepts:
        if c.get_construct() == None:
            c_string = f"({c.get_name()},{to_string(c.get_types())})"
            fluid_concepts = fluid_concepts + [c_string]
            input_concepts = input_concepts + [c.get_name()]
        else:
            c_string = f"({c.get_name()},{c.get_construct()},{to_string(c.get_types())})"
            perm_concepts = perm_concepts + [c_string]

    return perm_concepts, fluid_concepts, input_concepts

def stringify_objects(objects):
    output = []
    for o in objects:
        output = output + [f"({o.get_name()},{o.get_type()})"]
    return output


def to_string(list):
    return str(list).replace(" ", "").replace("'","")

def powerset_groups(groups):
    """Returns the powerset of the list of variables without the empty set"""
    return sum([list(map(list, combinations(groups, i))) for i in range(len(groups) + 1)], [])[1:]

def construct_vars_and_groups(concepts):
    """Generates variables according to a defined convention consisting of 
    "var_{typename}_{index}, where even variables with a single occurence 
    get an index of 1. Also gathers these into a list for the var_groups"""
    output = []
    groups = []

    for c in concepts:
        count = 1
        for t in c.get_types():
            var = f"var_{t[2:]}_{count}"
            if var not in groups:
                output = output + [(var,t)]
                groups = groups + [var]
            if len(c.get_types()) == 2 and c.get_types()[0] == c.get_types()[1]:
                count = 2

    return output, powerset_groups(groups)

# TODO: figure out how NOT to hardcode this
def gen_temp_stats(temp_dict, dir, name):
    """Generate template part of template_in file"""
    if "sok" in dir:
        miba, maba, nar, ncr, nvp, noise = 1, 4, 4, 8, "Nothing", "False"
    elif "sw" in dir:
        miba, maba, nar, ncr, nvp, noise = 2, 4, 4, 8, "Nothing", "False"
    elif "1" in name:
        miba, maba, nar, ncr, nvp, noise = 1, 1, 0, 2, "Nothing", "False"
    elif "2" in name:
        miba, maba, nar, ncr, nvp, noise = 1, 1, 0, 2, "Nothing", "False"
    elif "3" in name:
        miba, maba, nar, ncr, nvp, noise = 1, 1, 0, 4, "Nothing", "False" #2, 4, 4, 8,
    elif "4" in name:
        miba, maba, nar, ncr, nvp, noise = 2, 2, 0, 1, "Nothing", "False"
    output = f"""% Template
dir = {dir}
min_body_atoms = {miba}
max_body_atoms = {maba}
num_arrow_rules = {nar}
num_causes_rules = {ncr}
num_visual_predicates = {nvp}
use_noise = {noise}"""
    return output


# def process_dict(temp_dict):
#     temp_dict['types'] = catch_empty(temp_dict['types'].strip('[]').split(','))
#     temp_dict['type_hierarchy'] = process_hierarchy(temp_dict['type_hierarchy'])
#     temp_dict['objects'] = process_objects(temp_dict['objects'])
#     temp_dict['exogeneous_objects'] = catch_empty(temp_dict['exogeneous_objects'].strip('[]').split(','))
#     temp_dict['permanent_concepts'] = process_perms(temp_dict['permanent_concepts'])
#     temp_dict['fluid_concepts'] = process_hierarchy(temp_dict['fluid_concepts'])
#     temp_dict['input_concepts'] = catch_empty(temp_dict['input_concepts'].strip('[]').split(','))
#     temp_dict['static_concepts'] = catch_empty(temp_dict['static_concepts'].strip('[]').split(','))
#     temp_dict['vars'] = process_objects(temp_dict['vars'])
#     temp_dict['var_groups'] = catch_empty([x.split(',') for x in temp_dict['var_groups'].strip('[]').split('],[')])
#     return temp_dict









#---------------------------------------------------------------------
# Functions for retrieving the interpret_mem file from the memory tree
# using the template_dict constructed in the previous stage
#---------------------------------------------------------------------

def build_interpretation(tree, temp_dict, senses, dir, name):
    """Converts a template dict to an interpret_mem file"""
    start = f"% {dir}_{name}\n\n"
    permanents = gen_permanents(temp_dict)
    rules = gen_rules(temp_dict)
    output = [start + permanents + rules]
    # output = output + [start + permanents]  
    return output

def gen_permanents(temp_dict):
    """Generates strings of permanents using the template_dict for the 
    interpret_mem file"""

    output = "% Permanents\n"
    present_objects = [o.get_name() for o in temp_dict["objects"]]
    seen = []

    for object in temp_dict["objects"]:
        perms = object.get_permanents()
        for p in perms:
            if len(p) == 2 and p not in seen:
                output = output + f"permanent(isa({p[0]},{p[1]})).\n"
                seen = seen + [p]
            elif p[1] in present_objects and p[2] in present_objects and p not in seen:
                output = output + f"permanent(isa2({p[0]},{p[1]},{p[2]})).\n"
                seen = seen + [p]
    return output

def gen_rules(temp_dict):
    """Generates strings of rules using the template_dict for the 
    interpret_mem file"""
    output = "\n% Rules\n"
    index = 1
    seen = []

    present_concepts = []
    for concept in temp_dict["concepts"]:
        easy_form = [concept.get_name()] + concept.get_types()
        present_concepts = present_concepts + [easy_form]

    for concept in temp_dict["concepts"]:
        for rule in concept.get_rules():
            if rule.get_head().startswith("rule_arrow"):
                head_body = [rule.get_head()] + rule.get_body()
                if concept_check(rule.get_concepts(), present_concepts) \
                    and head_body not in seen:
                    output = output + rule_to_string(rule, index)
                    index = index + 1
                    seen = seen + [head_body]

    for concept in temp_dict["concepts"]:
        for rule in concept.get_rules():
            if not rule.get_head().startswith("rule_arrow"):
                head_body = [rule.get_head()] + rule.get_body()
                if concept_check(rule.get_concepts(), present_concepts) \
                    and head_body not in seen:
                    output = output + rule_to_string(rule, index)
                    index = index + 1
                    seen = seen + [head_body]
    
    return output


def rule_to_string(rule, index):
    "Converts a Rule to a string with a proper index"
    output = ""
    for line in rule.get_body():
        output = output + line.replace("ruleindex", f"r{index}") + "\n"
    output = output + rule.get_head().replace("ruleindex", f"r{index}") + "\n\n"
    return output
                
def concept_check(concepts, present_concepts):
    """Checks if all concepts present in a rule are present in the template"""
    for concept in concepts:
        if concept not in present_concepts:
            return False
    return True


#---------------------------------------------------------------------
# Functions to convert JSON tree to readable latex code
#---------------------------------------------------------------------


def json_to_latex(json_data):
    latex_code = r'''
\begin{figure}[ht!]
\begin{center}
    \begin{forest}
        for tree={draw}
'''
    latex_code += process_node(json_data, indent=8)
    latex_code += r'''
    \end{forest}
    \caption{Visual representation of a non-naive concept tree $\tau$ containing some \textit{a priori} elements.}
    \label{fig:predict_1}
\end{center}
\end{figure}
'''
    return latex_code

def process_node(node, indent):
    latex_code = ''
    # print(node)
    if node['name'] == 'Root':
        latex_code = ' ' * indent
        latex_code += f"[{node['name']} ,align=center,tier=above\n"

    if 'extension' in node and node['extension']:
        for subnode in node['extension']:
            latex_code += ' ' * (indent + 4)
            latex_code += f"[{subnode['name']} \\\\\\hline\n".replace('_', '\_')
            latex_code += ' ' * (indent + 8)
            latex_code += "\\textit{Objects: " + ', '.join([obj['name'].replace('_', '\_') for obj in subnode['objects']]) + "}\\\\\n"
            latex_code += ' ' * (indent + 8)
            latex_code += "\\textit{Concepts: " + ', '.join([concept['name'].replace('_', '\_') for concept in subnode['concepts']]) + "}\n"
            latex_code += process_node(subnode, indent + 4)
            latex_code += ' ' * (indent + 4)
            latex_code += "]\n"
    
    if node['name'] == 'Root':
        latex_code += ' ' * indent
        latex_code += "]"
    return latex_code

# # TODO: Fix exogeneous objects and static_concepts + vars when working on interpretation
# def gen_frame(temp_dict, dir, name):
#     """Uses the template dict to generate the frame part of the template_in file"""
#     perm_concepts, fluid_concepts, input_concepts = stringify_concepts(temp_dict["concepts"])
#     # vars, var_groups = gen_vars_and_groups(temp_dict["concepts"])
#     output = f"""\n\n% Frame
# types = {to_string(temp_dict["types"])}
# type_hierarchy = {to_string(temp_dict["type_hierarchy"])}
# objects = {to_string(temp_dict["objects"])}
# exogeneous_objects = []
# permanent_concepts = {to_string(perm_concepts)}
# fluid_concepts = {to_string(fluid_concepts)}
# input_concepts = {to_string(input_concepts)}
# static_concepts = []
# vars = [(var_l,t_letter),(var_l2,t_letter),(var_s,t_sensor)]
# var_groups = [[var_l,var_l2,var_s]]
# aux_files = ["{dir}_{name}_interpret_mem.lp"]"""
#     return output

# # TODO: improve the input_concepts part by adding a concept attribute to the Concept class
# def stringify_concepts(concepts):
#     perm_concepts = []
#     fluid_concepts = []
#     input_concepts = []
#     for c in concepts:
#         if c.get_construct() == None:
#             c_string = f"({c.get_name()},{to_string(c.get_types())})"
#             fluid_concepts = fluid_concepts + [c_string]
#             input_concepts = input_concepts + [c.get_name()]
#         else:
#             c_string = f"({c.get_name()},{c.get_construct()},{to_string(c.get_types())})"
#             perm_concepts = perm_concepts + [c_string]
#     return perm_concepts, fluid_concepts, input_concepts



#---------------------------------------------------------------------
# Functions for updating and maintaining the memory tree
#---------------------------------------------------------------------



# def recursive_update_objects(node, root):
#     """Recursively walks through the tree and changes every occurence of 
#     the objects into new Objects"""
#     for child in node.get_extension():
        

#         if child.get_extension() != []:
#             output = recursive_update_all(child, old, new, root)
#     return output


# # Add types to the tree, according to the hierarchy given in the template
# def update_type_hierarchy(tree, template):
#     for t in template['type_hierarchy']:
#         present_types = tree.get_full_extension_names()
#         if t not in present_types:
#             node = tree.add_node(TreeNode(t))
#         for e in template['type_hierarchy'][t]:
#             if e not in present_types:
#                 tree.get_node_by_name(t).add_node(TreeNode(e))
#     return tree






















