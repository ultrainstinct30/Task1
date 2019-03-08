class StateMachine:
    def __init__(self):
        self.min=0
        self.max=8
        self.li=5
        self.inside=[7,3]
        self.up=[6,4]
        self.down=[2]
        self.last=5
        self.beforetrns=5


    def runlift(self):

        d1,l1=self.path_dud()
        d2,l2=self.path_udu()
        if d1<=d2:
            for i in l1:
                print i,
        elif d1>d2:
            for i in l2:
                print i,

    
    def moveup(self):

        last=self.last
        d=0
        l=[]
        for i in range(self.beforetrns,self.max+1):
            self.beforetrns=i
            if i in self.inside or i in self.up:
                d+=abs(i-last)
                last=i
                l.append(i)
                if i in self.up:
                    self.up.remove(i)
                if i in self.inside:
                    self.inside.remove(i)
                if self.inside==[] and self.up==[] and self.down==[i]:
                    self.down.remove(i)
        
            if i==self.max and i in self.down:
                self.down.remove(i)
        self.last=last
        return d,l
    

    def movedown(self):
        l=[]
        d=0
        last=self.last
        for i in range(self.last,self.min-1,-1):
            self.beforetrns=i
            if i in self.inside or i in self.down:
                d+=(last-i)
                last=i
                l.append(i)
                if i in self.down:
                    self.down.remove(i)
                if i in self.inside:
                    self.inside.remove(i)
                if self.inside==[] and self.down==[] and self.up==[i]:
                    self.up.remove(i)
        
            if i==self.min and i in self.up:
                self.up.remove(i)
        self.last=last
        return d,l
    
    def path_dud(self):
        d21,l21=self.movedown()
        d22,l22=self.moveup()
        d23,l23=self.movedown()
        self.li=5
        self.inside=[7,3]
        self.up=[6,4]
        self.down=[2]
        self.last=5
        self.beforetrns=5
        return d21+d22+d23,[self.li]+l21+l22+l23

    def path_udu(self):
        d21,l21=self.moveup()
        d22,l22=self.movedown()
        d23,l23=self.moveup()
        return d21+d22+d23,[self.li]+l21+l22+l23

  

    
m = StateMachine()
m.runlift()