class Solution:
    def canChange(self, start: str, target: str) -> bool:
    '''
        Since, L and R can only move to their respective sides and can't jump over,
        we can remove all '_' and check if start and target are equal
        if they are we need to check if all L in start come at or after corresponding L's in
        target...Similarly for R
    '''
        if ''.join(target.split('_')) != ''.join(start.split('_')):
            return False
        
        n = len(start)
        start_L_indices = []
        start_R_indices = []
        target_L_indices = []
        target_R_indices = []

        for i in range(n):
            if target[i] == 'L':
                target_L_indices.append(i)
            elif target[i] == 'R':
                target_R_indices.append(i)

        for i in range(n):
            if start[i] == 'L':
                start_L_indices.append(i)
            elif start[i] == 'R':
                start_R_indices.append(i)

        for i in range(len(start_L_indices)):
            if start_L_indices[i] < target_L_indices[i]:
                return False

        for i in range(len(start_R_indices)):
            if start_R_indices[i] > target_R_indices[i]:
                return False

        return True
