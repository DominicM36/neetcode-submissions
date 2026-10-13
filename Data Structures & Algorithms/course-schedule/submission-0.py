class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #second item in 2dim of list is prereq
        #idea is no cycle in the graph
        #need to track courses in a current path
        #make adjacency list
        preMap = {i: [] for i in range(numCourses)}
        
        #populate adj list
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True