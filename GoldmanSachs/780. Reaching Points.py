class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        APPROACH 1: Recursive
        Each point have 2 children to explore

        TC - O(2^(tx + ty)) i.e. exponential
        SC - O(tx * ty) for size of the call stack
        '''
        def reachingPointsRecursive(x, y):
            if (x > tx or y > ty): return False
            if (x == tx and y == ty): return True

            return reachingPointsRecursive(x + y, y) or reachingPointsRecursive(x, x + y)
        
        '''
        APPROACH 2: Memo
        Memoize the points

        TC - O(tx * ty) i.e. tx * ty points are searched once per point
        SC - O(tx * ty) for size of the call stack
        '''
        def reachingPointsMemo():
            seen = set()
            def search(x, y):
                if (x, y) in seen: return
                if x > tx or y > ty: return
                
                seen.add((x, y))
                search(x + y, y)
                search(x, x + y)
            
            search(sx, sy)
            return (tx, ty) in seen

        '''
        APPROACH 3: Work backwards (from target to source)

        TC - O(max(tx, ty)) i.e. tx * ty points are searched once per point
        SC - O(1)
        '''
        def reachingPointsBackwards(tx, ty):
            while tx >= sx and ty >= sy:
                if sx == tx and sy == ty: return True

                if tx > ty:
                    tx -= ty
                else:
                    ty -= tx
            return False
        
        '''
        APPROACH 4: Work backwards Optimized (from target to source)
        - Using modulo for cases (1, 9) -> (100, 9)
        - Check edge case (3, 3) -> (21, 9)
        - Video: https://www.youtube.com/watch?v=tPr5Uae6Drc&ab_channel=TonyTeaches

        TC - O(max(tx, ty)) i.e. tx * ty points are searched once per point
        SC - O(1)
        '''
        def reachingPointsBackwardsOptimized(tx, ty):
            while tx >= sx and ty >= sy:
                if sx == tx and sy == ty: return True

                if tx > ty:
                    tx %= ty
                else:
                    ty %= tx
                
                if tx == sx:
                    if (ty - sy) % tx == 0: 
                        return True
                    else:
                        return False
                

                if ty == sy:
                    if (tx - sx) % ty == 0:
                        return True
                    else:
                        return False
            return False
        
        # return reachingPointsRecursive(sx, sy)
        # return reachingPointsMemo()
        # return reachingPointsBackwards(tx, ty)
        return reachingPointsBackwardsOptimized(tx, ty)