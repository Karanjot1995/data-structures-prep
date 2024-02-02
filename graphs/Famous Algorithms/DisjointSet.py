
class DisjointSet():
  def __init__(self,n):
    self.rank = [0]*(n+1)
    self.parent = [i for i in range(n+1)]
    self.size = [1]*(n+1)

  # def DisjointSet(self,n):
  #   #right now rank is 0 for everyone and anyeyone is a parent of itslef
  #   for i in range(n+1):
  #     self.rank.append(0)
  #     self.parent.append(i)
  
  def findUParent(self,node):
    if node == self.parent[node]:
      return node
    self.parent[node] = self.findUParent(self.parent[node])
    return self.parent[node]
    # return self.findUParent(self.parent[node])

  def unionByRank(self, u, v):
    rank = self.rank
    parent = self.parent

    ulp_u = self.findUParent(u)
    ulp_v = self.findUParent(v)
    
    if ulp_u == ulp_v: return 

    if(rank[ulp_u] < rank[ulp_v]):
      parent[ulp_u] = ulp_v
    elif(rank[ulp_u] > rank[ulp_v]):
      parent[ulp_v] = ulp_u
    else:
      parent[ulp_v] = ulp_u
      rank[ulp_u]+=1
    print(ulp_u,ulp_v, rank, parent)


  def unionBySize(self, u, v):
    size = self.size
    parent = self.parent
    ulp_u = self.findUParent(u)
    ulp_v = self.findUParent(v)
    if ulp_u == ulp_v: return 

    if(size[ulp_u] < size[ulp_v]):
      parent[ulp_u] = ulp_v
      size[ulp_v] += size[ulp_u]
    else:
      parent[ulp_v] = ulp_u
      size[ulp_u] += size[ulp_v]
    print(ulp_u, ulp_v, size)


djs = DisjointSet(7)
djs.unionByRank(1,2)
djs.unionByRank(2,3)
djs.unionByRank(4,5)
djs.unionByRank(5,6)
djs.unionByRank(6,7)
# djs.unionByRank(3,7)

# djs.unionBySize(1,2)
# djs.unionBySize(2,3)
# djs.unionBySize(4,5)
# djs.unionBySize(5,6)
# djs.unionBySize(6,7)
# djs.unionBySize(3,7)

print(djs.findUParent(3), djs.findUParent(7))
        
# public: 
#     vector<int> parent, size;

#     DisjointSet(int n){
#         parent.resize(n+1);
#         size.resize(n+1);
#         for(int i = 0; i <= n; i++){
#             parent[i] = i;
#             size[i] = 1;
#         }
#     }

#     int findParent(int n){
#         if(n == parent[n]) return n;
#         return parent[n] = findParent(parent[n]);
#     }

#     void unionSize(int f, int k){
#         int ulu = findParent(f);
#         int ulv = findParent(k);

#         if(ulu == ulv) return;
#         if(size[ulu] > size[ulv]){
#             parent[k] = ulu;
#             size[ulu] += size[ulv];
#         }
#         else{
#             parent[f] = ulv;
#             size[ulv] += size[ulu];
#         }
#     }

# };

# class Solution {
# public:
#     vector<int> findRedundantConnection(vector<vector<int>>& edges) {
#         vector<int> ans(2);
#         int n = 0;
#         for(auto it : edges){
#             n = max(n,it[1]);
#         }

#         DisjointSet ds(n);
#         for(auto it: edges){
#             if(ds.findParent(it[0]) == ds.findParent(it[1])){
#                 ans[0] = it[0];
#                 ans[1] = it[1];
#             }
#             else{
#                 if(it[0] == 2 && it[1] == 5)
#                 cout<<ds.findParent(2)<<" "<<ds.findParent(5)<<endl;
#                 ds.unionSize(it[0],it[1]);
#                 ds.findParent(it[0]) == ds.findParent(it[1]);
#             }
#         }
#         if(n >= 5)
#         cout<<ds.findParent(2)<<" "<<ds.findParent(5);
#         return ans;
#     }
# };

