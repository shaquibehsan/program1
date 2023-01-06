
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]


    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'F': 1,
        }

        return H[n]

    def a_star_algorithm(self, start, stop):

        open_lst = set([start])
        closed_lst = set([])

        cost = {}
        cost[start] = 0

        adj_list = {}
        adj_list[start] = start

        while len(open_lst) > 0:
            
            n = None
            for v in open_lst:
                if n == None or cost[v] + self.h(v) < cost[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None
            if n == stop:
                reconst_path = []

                while adj_list[n] != n:
                    reconst_path.append(n)
                    n = adj_list[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path


            for (m, weight) in self.get_neighbors(n):

                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    adj_list[m] = n
                    cost[m] = cost[n] + weight

                else:
                    if cost[m] > cost[n] + weight:
                        cost[m] = cost[n] + weight
                        adj_list[m] = n

                        # if m in closed_lst:
                        #     closed_lst.remove(m)
                        #     open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None


adjac_lis = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5),('F', 2)],
    'C': [('D', 12)],
    'F': [('D',1)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')