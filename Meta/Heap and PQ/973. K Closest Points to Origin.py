# https://leetcode.com/problems/k-closest-points-to-origin/description/

from heapq import heappop, heappush

'''
APPROACH 1: SORTING

TC - O(NlogN) 
SC - O(N)
'''
def kClosest(points, K):
    points.sort(key = lambda P: P[0]**2 + P[1]**2)
    return points[:K]

'''
APPROACH 2: MAX HEAP

TC - O(Nlogk) 
SC - O(k)
'''
def kClosest2(points, k):
    maxHeap = []
    n = len(points)

    for i in range(n):
        x, y = points[i]
        distance = x*x + y*y

        heappush(maxHeap, (-distance, [x, y]))

        if len(maxHeap) > k:
            heappop(maxHeap)
    
    ans = []

    while maxHeap:
        distance, point = heappop(maxHeap)
        ans.append(point)
    
    return ans

'''
APPROACH 3: QUICKSELCT

TC - O(N) average; O(N^2) worst case
SC - O(N)
'''
def kClosest3(points, K):
    def quickselect(l, r):
        if l < r:
            p = partition(l, r)
            if p == K:
                return
            elif p < K:
                quickselect(p + 1, r)
            else:
                quickselect(l, p - 1)
     
    # LOMUTO'S PARTITIONING SCHEME       
    def partition(l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a
    
    quickselect(0, len(points) - 1)
    return points[:K]









class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2