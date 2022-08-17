class Solution:
    def distance_from_O(self, point: List[int]) -> int:
        return (point[0]) ** 2 + point[1] ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point_distance = self.distance_from_O(point)
            point.insert(0, point_distance)
        points.sort()
        
        result = []
        for i in range(k):
            result.append([points[i][1], points[i][2]])
        
        return result