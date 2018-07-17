class node :#el m7toa bta3 elnod elwa7da fe eltree
    def __init__(self,person1,person2,rever_side):
        self.person1=person1
        self.person2=person2
        self.rever_side=rever_side#if 1 then boat in right side and will go , if 2 then boat in left side and will return
        self.right_list=[]#this list represent the cuurent persons in right side
        self.left_list=[]#this list represent the cuurent persons in left side
        self.timer=0#represent the cuurent time for each path
        self.childeren=[]

    def add_childeren(self,childeren):
        for i in childeren:
            self.childeren.append(i)
    def calculate_time(self,time):
        if(self.person1>self.person2):
            a=self.person1
        else:
            a=self.person2
        self.timer=time+a

    def set_lists(self,right_list,left_list):
        if(self.person1==0 and self.person2==0):#start state
            self.right_list=[1,3,6,7,8]
            self.left_list=[]
        else:
            self.right_list=right_list#intialize them with lists of parent then i will them according to the case od this state
            self.left_list=left_list#intialize them with lists of parent then i will them according to the case od this state
            if(self.rever_side==1):#two persons will leave right side and go to left side
                self.right_list.remove(self.person1)
                self.right_list.remove(self.person2)
                self.left_list.append(self.person1)
                self.left_list.append(self.person2)
            else:#one person will leave left side and return to left side
                self.left_list.remove(self.person1)
                self.right_list.append(self.person1)
        self.right_list.sort()#I must sort all lists of nodes to be able to compare them
        self.left_list.sort()#I must sort all lists of nodes to be able to compare them
        print(self.person1,self.person2)#I represent here how will become two sides in each state all states
        print(self.left_list,self.right_list)#I represent here how will become two sides in each state all states