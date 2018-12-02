class Graph:
    def __init__(self):
        self.point = []
	def is_square(val):
    if (math.sqrt(val))**2 == (math.floor(math.sqrt(val)))**2:
        return True
    else:
        return False
graph = Graph()
values = open('values.txt', 'r')
readable_values = values.readlines()
for line in readable_values:
    if not is_square(len(line)):
        print("wrong input")
        break
    else:
        manager_len = int(math.sqrt(len(line)))
        managers = [line[i:i + managers_len] for i in range(0, len(line), managers_len)]
        for managers in managers:
            graph.add_verticle(point(managers))
        for managers in managers:
            counter = 0
            for char in manager:
                if char == "Y":
                    graph.add_edge(point(manager), poitn(managers[counter]))
                counter += 1
    graph.topological_sort()
    summ = 0
    for verticle in graph.get_point():
        summ += verticle.salary
    print(summ)

    def get_point(self):
        return self.point
    def add_verticle(self, new_verticle):
        self.point.append(new_verticle)
    def dfs(self, current, visited):
        for i in current.connection:
            if not visited.get(i):
                self.dfs(i, visited)
                visited[i] = True
        if not current.connection:
            current.salary = 1
        else:
            for i in current.connection:
                current.salary += i.salary
	 def add_edge(self, point1, point2):
        counter = 0
        for i in self.point:
            if i.point == point1.point:
                point1 = self.point.pop(counter)
                break
            counter += 1
        counter = 0
        for i in self.point:
            if i.point == point2.point:
                point2 = self.point.pop(counter)
                break
            counter += 1
        point1.connection.append(point2)
        self.point.append(point1)
        self.point.append(point2)		
    def point_sort(self):
        visited = {point: False for point in self.point}
        for i in visited:
            if not visited[i]:
                self.dfs(i, visited)
                visited[i] = True
