#GFG PROBLEM- Get minimum element from stack
#Using  2x-minelement to find the min element and also the previous minimum element before adding the present min element in the stack without using extra space 
class stack:
    def __init__(self):
        self.s=[]
        self.minele=None

    def push(self,x):
        #I used (2x-minele) formula to update the stack
        if len(self.s)==0:
            self.minele=x
        if len(self.s)==0 or x>=self.minele:
            self.s.append(x)
        elif x<self.minele:
            z=2*x-self.minele
            self.minele=x
            self.s.append(z)
        
    
    def pop(self):
        if len(self.s)==0:
            return -1
        if self.s[-1]<self.minele:
            ans=self.minele
            m=self.s.pop()
            self.minele=2*self.minele-m
        else:
            ans=self.s.pop()
        return ans
        

    def getMin(self):
        if len(self.s)==0:
            return -1
        return self.minele
