#https://www.youtube.com/watch?v=3Q_oYDQ2whs
schedule1 = ([
        ['9:00','10:30'],
        ['12:00','13:00'],
        ['16:00','18:00']
    ],
    ['9:00','20:00'])
schedule2 = ([
        ['10:00','11:30'],
        ['12:30','14:30'],
        ['14:00','15:00'],
        ['16:00','17:00']
    ],['10:00','18:30'])
meeting_length = 30

class Scheduler:
    def __init__(self, ml) -> None:
        self.ml = ml
        self.day = [None for i in range(2400)]
        self.clock()
    
    def start_scheduling(self, sch1, sch2):
        self.schedule(sch1)
        self.schedule(sch2)
        self.get_free_time()

    def get_free_time(self):
        free_slots = []
        for i in enumerate(self.day):
            status = i[1]
            if status == False:
                free_slots.append(i)
        self.free_slots_to_time(free_slots)
        
    def free_slots_to_time(self, free_slots):
        c= True
        n = None
        s = 0
        free_time_slots = []
        for i in free_slots:
            time = i[0]
            if n == None:
                n = time
                s = time
            elif time-n != 1:
                free_time_slots.append([s,n])
                n = None
            else:
                n = time
        self.int_time_str(free_time_slots)

    def int_time_str(self,free_time_slots):
        time_slot = []
        for slot in free_time_slots:
            start = slot[0]
            end = slot[1]
            start = str(start)[0:2]+":"+str(start)[2:]
            end = str(end)[0:2]+":"+str(end)[2:]
            time_slot.append([start,end])
        print(time_slot)

    def schedule(self, sch):
        wh = sch[1]
        meetings = sch[0]
        meetings.append(["0:00",wh[0]])
        meetings.append([wh[1],"23:59"])
        for meeting in meetings:
            self.scheduler(meeting)

    def clock(self):
        for h in range(0,24):
            for m in range(0,60):
                t = h*100+m
                self.day[t] = False
    def scheduler(self, l):
        for i in enumerate(l):
            index = i[0]
            ele = i[1]
            ele = ele.replace(':','')
            ele = int(ele)
            l[index] = ele
        
        for i in range(l[0],l[1]):
            self.day[i] = True

    
s = Scheduler(meeting_length)
s.start_scheduling(schedule1, schedule2)