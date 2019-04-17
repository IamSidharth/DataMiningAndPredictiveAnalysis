import csv
import math
import copy
from collections import Counter

class filereader:
  def __init__(self, filename):
    self.filename = filename
    self.read_csv_file()
    # removes the class label from the attributes list
    self.attributes = self.attributes[:-1]

  def read_csv_file(self):
    self.attributes = []
    self.data = []
    with open(self.filename, 'r') as csvfile:
      reader = csv.reader(csvfile)
      self.attributes = next(reader)
      for row in reader:
        processed_row = self.get_processed_row(row)
        self.data.append(processed_row)

  # generates a key value pair for each attribute
  def get_processed_row(self, row):
    processed_row = {}
    for i in range(len(row)):
      processed_row[self.attributes[i]] = row[i]
    return processed_row

class node:
  def __init__(self, name=None):
    # contains the attribute at the current node
    self.name = name
    # contains the value of the parent attribute used to get to this node
    self.next = None
    # contains nodes that are directly reached from here
    self.children = []

  def print_tree(self, space):
    spaces = "\t" * space
    if self.next != None:
      print(spaces, "PATH", self.next) 
    print(spaces, "NAME", self.name)
    for child in self.children:
      child.print_tree(space + 1)

class decision_tree:
  def __init__(self, data, attributes, class_label):
    self.data = data
    self.attributes = attributes
    self.class_label = class_label
    self.counts = Counter([x[self.class_label] for x in self.data])
    self.dataset_info = self.get_dataset_info()

  def get_majority_label(self):
    return self.counts.most_common(1)[0]

  def get_attribute_gain(self, attr):

    # get all possible paths
    paths = [x[attr] for x in self.data]
    path_counts = Counter(paths)

    # get paths with final outcome
    outcomes = [(x[attr], x[self.class_label]) for x in self.data]
    outcome_counts = Counter(outcomes)

    records_count = len(self.data)

    info = 0.0
    for outcome in outcome_counts:
      factor = path_counts[outcome[0]]
      term = outcome_counts[outcome] / factor
      info -= factor / records_count * term * math.log2(term)

    return self.dataset_info - info

  def get_dataset_info(self):
    dataset_info = 0.0
    records_count = len(self.data)
    for item in self.counts:
      term = self.counts[item] / records_count
      dataset_info -= term * math.log2(term)
    return dataset_info

  # returns attribute with maximum gain
  def get_best_attribute(self):
    gains = [(attr, self.get_attribute_gain(attr)) for attr in self.attributes]
    return max(gains, key=lambda x: x[1])[0]

  # checks if there is only one classlabel in the dataset
  def is_single_class_labelled(self):
    return len(self.counts) == 1

  # returns unique outcomes for a given attribute
  def get_attribute_outcomes(self, attr):
    return set([x[attr] for x in self.data])

  # returns dataset for a given outcome, while removing the attribute
  def get_child_dataset(self, attr, outcome):
    dataset = copy.deepcopy([x for x in self.data if x[attr] == outcome])
    for data in dataset:
      del data[attr]
    return dataset

  def compute(self):

    # if all are same class or there are no more attributes return majority class
    if self.is_single_class_labelled() or len(self.attributes) == 0:
      return node(self.get_majority_label()[0])

    best_attribute = self.get_best_attribute()
    self.attributes.remove(best_attribute)
    new_attributes = copy.deepcopy(self.attributes)
    root = node(best_attribute)

    # for each outcome from the splitting criterion
    for outcome in self.get_attribute_outcomes(best_attribute):
      child = node()
      new_dataset = self.get_child_dataset(best_attribute, outcome)

      # if new dataset is empty return majority class of current dataset
      if len(new_dataset) == 0:
        child.name = self.get_majority_label()
      else:
        subtree = decision_tree(new_dataset, new_attributes, self.class_label)
        child = subtree.compute()
      
      child.next = outcome
      root.children.append(child)
    
    return root


filename = 'Book1.csv'
class_label = 'PlayGolf'
contents = filereader(filename)
tree = decision_tree(contents.data, contents.attributes, class_label)
root = tree.compute()
root.print_tree(0)
