import node
import DFS_search
import State_Space_Generator
class  tree_creation :
    def __init__(self):
      pass

    def getPath(self):
        listOfLevel=[]
        generator=State_Space_Generator.State_Space_Generator()
        start_state=node.node(0, 0, 2)#create start node
        start_state.set_lists([],[])
        generator.generate_childeren(start_state)#generate its childeren
        for k in start_state.childeren:
            subList=generator.generate_childeren(k)#list for each childeren of one state
            for i in subList:#pool of all states in new created level
                listOfLevel.append(i)
        while(True):#create nodes level by level until leaves
            state=listOfLevel.pop(0)
            subList=generator.generate_childeren(state)
            if(subList==[] and listOfLevel==[]):#exit from loop if big list became empty and list of childs became empty also
                break
            for i in subList:
                listOfLevel.append(i)
        print('done')
        solution_path=[]
        worked_solution_path=[]
        search=DFS_search.DFS_search()
        search.DFS(start_state,solution_path,0)#here I fill the list with nodes of solution path only to can use it in GUI
        for i in solution_path:
            print(i.person1,i.person2,i.rever_side,i.timer)
            path_node_contains = (i.person1, i.person2, i.rever_side, i.timer)
            # put each node in the list for GUI
            worked_solution_path.append(path_node_contains)

        return worked_solution_path
