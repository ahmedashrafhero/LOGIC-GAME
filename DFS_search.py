import node
class DFS_search:
    def __init__(self):
        pass
    def DFS(self,S,solution_path,time):#I compute the time of each state when visiting them dynamically also
        S.calculate_time(time)
        if(S.timer<29 and S.right_list==[] and S.left_list==[1,3,6,7,8]):#the condition of this game to reach the goal
            solution_path.append(S)
            return True#here , I mark the goal state with retuning true for last calling function and so on until returning to start state
        if(S.childeren==[]):# this state is leaf but not goooaaal
            return False
        for x in S.childeren:
            for k in S.childeren:
                list1 = []
                list2 = []
                for i in S.right_list:
                    list1.append(i)
                for i in S.left_list:
                    list2.append(i)
            a=self.DFS(x,solution_path,S.timer)
            if(a==True):
                solution_path.append(S)
                return True
        return False
             
            
         
        
        
    
       
    
