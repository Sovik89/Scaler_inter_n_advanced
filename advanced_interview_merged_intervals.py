#############################SCALER APPROACH  ##########################

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# class Solution:
#     # @param intervals, a list of Intervals
#     # @param newInterval, a Interval
#     # @return a list of Interval
#     def insert(self, intervals, newInterval):
#         ans=[]
#         i=0
#         n=len(intervals)
#         for i in range(n):
#             if intervals[i].end<newInterval.start:
#                 ans.append(intervals[i])
                
#             elif newInterval.end<intervals[i].start:
#                 ans.append(newInterval)
#                 for k in range(i,n):
#                     ans.append(intervals[k])
#                 return ans
                    
#             else:
#                 start= min(intervals[i].start,newInterval.start)
#                 end=max(intervals[i].end,newInterval.end)
#                 newInterval.start=start
#                 newInterval.end=end
#         ans.append(newInterval)
        
#         return ans

################################## IDE APPROACH #########################
        
def insert(intervals, newInterval):
    ans=[]
    i=0
    n=len(intervals)
    for i in range(n):
        if intervals[i][1]<newInterval[0]:
            ans.append(intervals[i][1])
            
        elif newInterval[1]<intervals[i][0]:
            ans.append(newInterval)
            for k in range(i,n):
                ans.append(intervals[k])
            return ans
                
        else:
            start= min(intervals[i][0],newInterval[0])
            end=max(intervals[i][1],newInterval[1])
            newInterval[0]=start
            newInterval[1]=end
    ans.append(newInterval)
    
    return ans

print(insert([[1, 3], [6, 9]],[2,5]))
        
            
            
        
        
        
    





