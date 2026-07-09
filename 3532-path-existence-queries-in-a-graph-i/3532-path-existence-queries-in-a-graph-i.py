class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Array to store the component ID for each node
        component = [0] * n
        current_component_id = 0
        
        # Traverse the sorted array and assign component IDs
        for i in range(1, n):
            # If the gap exceeds maxDiff, we start a new, disconnected component
            if nums[i] - nums[i - 1] > maxDiff:
                current_component_id += 1
            component[i] = current_component_id
            
        # Answer each query by comparing the component IDs of the two nodes
        answer = []
        for q in queries:
            u, v = q[0], q[1]
            answer.append(component[u] == component[v])
            
        return answer