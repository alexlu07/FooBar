def solution(map):
    h = len(map)
    w = len(map[0])
    dist = [[float("inf") for j in range(h*w)] for i in range(h*w)]
    dist[0][0] = 0
    nodes = [[i * w + j for j in range(w)] for i in range(h)]
    neighbors = [[] for i in range(h*w)]
    walls = [[] for i in range(h*w)]
    adjacent = [[] for i in range(h*w)]
    passable = []
    for i in range(h):
        for j in range(w):
            neighbor = []

            if i > 0:
                neighbor.append([i-1, j])
            if i < h-1:
                neighbor.append([i+1, j])
            if j > 0:
                neighbor.append([i, j-1])
            if j < w-1:
                neighbor.append([i, j+1])

            if map[i][j] == 0:
                passable.append(nodes[i][j])
            for i_neighbor, j_neighbor in neighbor:
                adjacent[nodes[i][j]].append(nodes[i_neighbor][j_neighbor])
                if map[i_neighbor][j_neighbor] == 0:
                    dist[nodes[i][j]][nodes[i_neighbor][j_neighbor]] = 1
                    neighbors[nodes[i][j]].append(nodes[i_neighbor][j_neighbor])
                else:
                    walls[nodes[i][j]].append(nodes[i_neighbor][j_neighbor])


    for k in passable:
        for i in passable:
            for j in passable:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # for i in passable:
    #     print(i, neighbors[i])
    #     print(dist[i])
    result = dist[0][h*w-1]
    for i in passable:
        for wall in walls[i]:
            least = min(neighbors[wall], key=lambda x: dist[x][h*w-1])
            new_dist = dist[least][h*w-1] + 2
            total_dist = dist[0][i] + new_dist

            if total_dist < result:
                # print(result, total_dist)
                result = total_dist

    # print(neighbors)
    # print(nodes)
    # print(dist)
    # print(passable)
    # print(f"result: {result}")

    return result + 1

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
