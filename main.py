import numpy as np
import networkx as nx
from createRatingMatrix import create_ratings
#from matplotlib import pyplot as plt


def create_mMatrix(trainset, tpath):
    G = nx.DiGraph()
    G.add_nodes_from(list(trainset.all_users()))
    print("nodes :" + str(G.number_of_nodes()))

    with open(tpath, 'r') as file:
        for line in file.readlines():
            user1 = line.split(' ')[0]
            user2 = line.split(' ')[1]
            print("user1 user2 " + str(user1) + " " + str(user2))
            if (int(user2) > 1508) or (int(user1) > 1508):
                print("yes they bigger")
                continue
            try:
                inner_u1 = trainset.to_inner_uid(user1)
                inner_u2 = trainset.to_inner_uid(user2)
                G.add_edge(inner_u1, inner_u2)
                print("edges :" + str(G.number_of_edges()))
            except ValueError:
                print("error")
                pass
    # nx.draw_networkx(G)
    # plt.show()
    return np.asarray(nx.directed_modularity_matrix(G)), np.asarray(nx.adjacency_matrix(G).todense())


if __name__ == '__main__':
    rpath = "cvtrain1.txt"
    rating_scale = (0.5, 4)
    trainset = create_ratings(rpath, rating_scale)
    tpath = "trust.txt"
    print(create_mMatrix(trainset, tpath))
