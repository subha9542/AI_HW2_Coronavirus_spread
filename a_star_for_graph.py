
class Node:
    def __init__(self, parent=None,name=None,position=None):
        self.parent = parent
        self.name = name
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

def get_neighbours(child):
    neighs = [i for i in G.neighbors(child)]
    if i is None:
      return None
    else:
      dict = {ne:G.nodes[ne]['pos'] for ne in neighs}
      sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
      #positions = [k for i,k in sorted_dict]
    return dict

def search(G, cost, start,start_name, end,end_name):


    # Create start and end node with initized values for g, h and f
    start_node = Node(None,start_name, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None,end_name, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    yet_to_visit_list = []  
    visited_list = [] 
    
    yet_to_visit_list.append(start_node)
    
    outer_iterations = 0
    max_iterations = (len(G) // 2) ** 10
    
    while len(yet_to_visit_list) > 0:
        outer_iterations += 1    

        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        if outer_iterations > max_iterations:
            print ("giving up on pathfinding too many iterations")
            return visited_list
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        if current_node.name == end_node.name:
            return [i.name for i in visited_list]

        # Generate children from all adjacent squares
        children = []
        move = get_neighbours(current_node.name)
        for new_ in move.items():
            node_position = (new_[1][0], new_[1][1])

            new_node = Node(current_node,new_[0], node_position)

            children.append(new_node)

        for child in children:
            
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            child.g = current_node.g + G[current_node.name][child.name]['weight']
            child.h = (((G.nodes[child.name]['pos'][0] - G.nodes[end_node.name]['pos'][0]) ** 2) + 
                       ((G.nodes[child.name]['pos'][1] - G.nodes[end_node.name]['pos'][1]) ** 2)) 
            child.f = child.g + child.h

            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            yet_to_visit_list.append(child)


if __name__ == '__main__':

    
    start = [29.5112,	-95.1979] 
    start_name = 'Galveston'
    end = [35.1989,	-101.831] 
    end_name = 'Amarillo'
    path = search(G,cost, start,start_name, end,end_name)
    print(path)
