import heapq
from collections import defaultdict

class Solution(object):
    def processQueries(self, c, connections, queries):
        parent = list(range(c))
        size = [1]*c
        mp = defaultdict(list)
        off = [False]*c

        for i in range(c):
            mp[i].append(i)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            ma = mp[a]
            mb = mp[b]
            if len(mb) > len(ma):
                ma, mb = mb, ma
                mp[a], mp[b] = mp[b], mp[a]
            for x in mb:
                heapq.heappush(ma, x)
            mp[b] = []

        for u, v in connections:
            union(u-1, v-1)

        ans = []
        for t, x in queries:
            x -= 1
            if t == 1:
                if not off[x]:
                    ans.append(x+1)
                    continue
                r = find(x)
                h = mp[r]
                while h and off[h[0]]:
                    heapq.heappop(h)
                ans.append(h[0]+1 if h else -1)
            else:
                off[x] = True

        return ans