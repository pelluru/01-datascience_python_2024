def find_parent(node, parent):
    if node == parent[node]: return node
    return find_parent(parent[node], parent)

def union(u, v, parent, rank):
    u = find_parent(u, parent)
    v = find_parent(v, parent)
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1


# Time Complexity Analysis
# O(M Log(M))  +  O(M * O(4α))

# Final --> O(M log M)

# Explanation
# O(M Log(M)) -> Sorting edges array
# O(M * O(4α)) -> iterating over edges array and computingg union and findparent
# M represents number of edges

# Space Complexity
# O(M) + O(N) + O(N)

# Final --> O(N)
# Where N represent the number of nodes stored in both parent and rank arrays
# Where M represent number of edges stored in mst array
def kruskals_algo(edges, n):
    edges.sort(key=lambda x :x[2])
    parent, rank = [], []
    for i in range(n):
        rank.append(0)
        parent.append(i)
    
    mst_cost, mst = 0, []
    for edge in edges:
        u, v, weight = 0, 1, 2
        if find_parent(edge[u], parent) != find_parent(edge[v], parent):
            mst_cost += edge[weight]
            mst.append(edge)
            union(edge[u], edge[v], parent, rank)

    return mst_cost

data = [[0,1,2], [0,3,6], [1,3,8], [1,2,3], [1,4,5], [2,4,7]]

print(kruskals_algo(data, 5))