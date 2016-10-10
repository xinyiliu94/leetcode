'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
from operator import itemgetter
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people = sorted(people,key=lambda x:x[0],reverse = True)
        print people
        queue = []
        tmp = []
        for i in xrange(len(people)):
            if not tmp:
                tmp.append(people[i])
            else:
                if tmp[-1][0]!=people[i][0]:
                    tmp = sorted(tmp,key=lambda x:x[1],reverse = True)
                    print tmp
                    while tmp:
                        person = tmp.pop()
                        queue.insert(person[1],person)
                tmp.append(people[i])
        if tmp:
            tmp = sorted(tmp,key=lambda x:x[1],reverse = True)
            while tmp:
                person = tmp.pop()
                queue.insert(person[1],person)
                print queue
        return queue
        
if __name__ =="__main__":
    s= Solution()
    s.reconstructQueue([[6,2],[1,5],[5,4],[6,0],[8,2],[5,2],[1,6],[8,0],[3,1],[9,0]])
    
