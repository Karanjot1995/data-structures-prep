# https://docs.google.com/document/d/1DtDEC4ocQ4z3BpPxe-_R-8UI6JqQeRMNA3WPdBCpGyo/edit

from collections import namedtuple
Interval = namedtuple("Interval", "start_time end_time price")

# Class to store node level data in BST
class Node(object):
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None 
        input_intervals.sort(key = lambda x: x.price)

class BST(object):
    def __init__(self):
        self.root = None
        self.sorted_intervals = []
    
    # Actual function to insert node into the tree
    def insert_helper(self, root, current):
        # Excess to the left - trim and push
        if current.start_time < root.interval.start_time:
            new_interval = Interval(current.start_time , min(current.end_time, root.interval.start_time), current.price)

            if root.left:
                self.insert_helper(root.left, new_interval)
            else:
                root.left = Node(new_interval)
        
        # Excess to the right - trim and push
        if current.end_time > root.interval.end_time:
            new_interval = Interval(max(current.start_time , root.interval.end_time), current.end_time, current.price)

            if root.right:
                self.insert_helper(root.right, new_interval)
            else:
                root.right = Node(new_interval)
    
    # Public function to insert node into the tree
    def insert_node(self, interval):
        if not self.root:
            self.root = Node(interval)
        
        else:
            self.insert_helper(self.root, interval)
    
    # Actual recursive function to do inorder traversal
    def dfs(self, node):
        if not node:
            return None

        if node.left:
            self.dfs(node.left)
        
        self.sorted_intervals.append(node.interval)
        
        if node.right:
            self.dfs(node.right)

    def inorder(self):
        self.sorted_intervals = []
        self.dfs(self.root)
        # return (self.sorted_intervals)
        
        return self.sorted_intervals

def get_lowest_prices(input_intervals):

    if not input_intervals:
        raise Exception("input_intervals has 0 elements")
    
    for each_interval in input_intervals:
        if not each_interval:
            raise Exception("input intervals has a Null element")
        if each_interval.start_time >= each_interval.end_time:
            raise Exception("start_time greater than or equal to end_time for an interval")
        if each_interval.start_time < 0 or each_interval.end_time < 0 or each_interval.price < 0:
            raise Exception("vendor information has negative values")
    
    '''
    Why sort on price?
    - As the first tuple after sorting will be the root and we will work around it
    - Also, since we will have the min price at the starting this tuple will not merge with anyone (merging only takes place if we have a price lower than the intervals being merged) 
    '''
    # input_intervals = sorted(input_intervals, key = lambda x: x.price)
    input_intervals.sort(key = lambda x: x.price)

    bst = BST()

    for each_interval in input_intervals:
        bst.insert_node(each_interval)
    
    return bst.inorder()

# op: (1, 7, 13), (7, 10, 8), (10, 20, 13)
input_intervals = [Interval(1, 20, 13), Interval(7, 10, 8), Interval(3, 8, 15), Interval(1, 5, 20)]
print(get_lowest_prices(input_intervals))
print("")

# op: (1, 20, 4)
input_intervals2 = [Interval(7, 10, 8), Interval(3, 8, 15), Interval(1, 5, 20), Interval(1, 20, 4)]
print(get_lowest_prices(input_intervals2))
print("")

# op: (1, 3, 3), (3, 5, 2), (5, 8, 1), (8, 9, 3)
input_intervals3 = [Interval(3, 6, 2), Interval(1, 9, 3), Interval(5,8, 1)]
print(get_lowest_prices(input_intervals3))
print("")