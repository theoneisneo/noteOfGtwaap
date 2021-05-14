class UnionFind():
    def __init__(self):
        # the group below is a "set".
        self.leader = {}  # dict, key: group member, value: group's leader
        self.group = {}  # dict, key: group's leader , value: group
        
    def make_set(self, member):
        if member not in self.leader:
            self.leader[member] = member
            
    def find_set(self, member):
        return self.leader.get(member)
    
    def union(self, member1, member2):
        leader1 = self.leader.get(member1)  # if member1 is not in self.leader, would get None.
        leader2 = self.leader.get(member2)

        if leader1 is not None:
            if leader2 is not None:
                if leader1 == leader2:  # member1 and member2 are in the same group already.
                    return
                
                group1 = self.group[leader1]
                group2 = self.group[leader2]
                
                # exchange for faster union
                if len(group1) < len(group2):
                    leader1, leader2 = leader2, leader1
                    group1, group2 = group2, group1
                    # member1, member2 = member2, member1  # have not use after

                group1 |= group2  # union group1 and group2, and assign value to variable group1
                del self.group[leader2]  # no need it anymore
                for k in group2:
                    self.leader[k] = leader1  # update leader
            else:
                # member2 has no leader, just add to group of leader1 and update leader value
                self.group[leader1].add(member2)
                self.leader[member2] = leader1
        else:
            if leader2 is not None:
                # member1 has no leader, just add to group of leader2 and update leader value
                self.group[leader2].add(member1)
                self.leader[member1] = leader2
            else:
                self.leader[member1] = member1
                self.leader[member2] = member1
                self.group[member1] = set([member1, member2])
