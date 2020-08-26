import networkx

import lexicon_builder

import matplotlib.pyplot as plt

if __name__ == '__main__':
    seeded_word_list = [('good', 1), ('bad', -1)]

    connections = lexicon_builder.build_connections(0, seeded_word_list, [], seeded_word_list)

    g = networkx.Graph()

    g.add_edges_from(connections)

    networkx.draw(g, with_labels=True)

    plt.show()