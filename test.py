g = {'a': ['b', 'c'],
     'b': ['c', 'd'],
     'c': ['e'],
     'd': ['f'],
     'e': ['f']
     }


def traverse(q):
    from collections import deque
    q = deque()
    visited = {'a'}
    q.appendleft('a')
    while len(q) != 0:
        print(q)
        x = q.popleft()
        print(x)
        edges = g.get(x)
        if edges is not None:
            for e in edges:
                if e not in visited:
                    q.appendleft(e)
                    visited.add(e)


traverse(g)

#11