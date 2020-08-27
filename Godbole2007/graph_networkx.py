import lexicon_builder
import networkx

if __name__ == '__main__':
    seeded_word_list = [('good', 1), ('bad', -1)]
    # seeded_word_list = [('good', 1)]
    connections = lexicon_builder.build_connections(0, seeded_word_list, [], seeded_word_list)

    g = networkx.Graph()

    g.add_edges_from(connections)

    print(g.number_of_nodes())

    g = lexicon_builder.flip_filter(g, seeded_word_list, 3)

    print(g.number_of_nodes())

    lexicon_builder.draw_word_graph(g)

    