# create visualization

#imports

import json
import pickle
from sklearn.tree._tree import TREE_LEAF

# read the pre-trained model

def getModel():
    model = 'models/decision_tree_model.sav'
    return pickle.load(open(model, 'rb'))

dt = getModel()

# prune the decision tree
def prune_index(inner_tree, index, threshold):
    if inner_tree.value[index].min() < threshold:
        # turn node into a leaf by "unlinking" its children
        inner_tree.children_left[index] = TREE_LEAF
        inner_tree.children_right[index] = TREE_LEAF
    # if there are shildren, visit them as well
    if inner_tree.children_left[index] != TREE_LEAF:
        prune_index(inner_tree, inner_tree.children_left[index], threshold)
        prune_index(inner_tree, inner_tree.children_right[index], threshold)

print(sum(dt.tree_.children_left < 0))

# start pruning from the root
prune_index(dt.tree_, 0, 5)
sum(dt.tree_.children_left < 0)

# create json
def rules(clf, features, labels, node_index=0):
    """Structure of rules in a fit decision tree classifier

    Parameters
    ----------
    clf : DecisionTreeClassifier
        A tree that has already been fit.

    features, labels : lists of str
        The names of the features and labels, respectively.

    """
    node = {}
    if clf.tree_.children_left[node_index] == -1:  # indicates leaf
        count_labels = zip(clf.tree_.value[node_index, 0], labels)
        node['name'] = ', '.join(('{} of {}'.format(int(count), label)
                                  for count, label in count_labels))
    else:
        feature = features[clf.tree_.feature[node_index]]
        threshold = clf.tree_.threshold[node_index]
        node['name'] = '{} > {}'.format(feature, threshold)
        left_index = clf.tree_.children_left[node_index]
        right_index = clf.tree_.children_right[node_index]
        node['children'] = [rules(clf, features, labels, right_index),
                            rules(clf, features, labels, left_index)]
    return node

features = ['is_banked',
            'code_module_x',
            'code_presentation_x',
            'gender',
            'region',
            'highest_education',
            'imd_band',
            'age_band',
            'num_of_prev_attempts',
            'disability',
            'code_module_y',
            'code_presentation_y']

target = 'final_result'

print(rules(dt, features, target))
#with open('static/datasets/rules.json', 'w') as f:
#    f.write(json.dumps(r))