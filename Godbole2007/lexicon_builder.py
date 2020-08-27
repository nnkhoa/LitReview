import itertools

import matplotlib.pyplot as plt

import networkx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

from nltk.corpus import wordnet as wn

def get_sense_key(wn_key):
    sense_attributes = wn_key.split('%')
    
    return int(sense_attributes[1].split(':')[0])


def get_synonym_antonym(seeded_word):
    synonym = []
    antonym = []

    syns = wn.synsets(seeded_word[0]) 
    for syn in syns:
        for lemma in syn.lemmas():
            sense_key = get_sense_key(lemma.key())
            if sense_key <= 4:
                if lemma.name() != seeded_word[0]:    
                    synonym.append(lemma.name())
                if lemma.antonyms():
                    antonym.append(lemma.antonyms()[0].name())

    synonym = build_attribute(list(set(synonym)), seeded_word, 'synonym')
    antonym = build_attribute(list(set(antonym)), seeded_word, 'antonym')

    return synonym, antonym


def flip_polarity(list_type, seeded_polarity):
    if list_type == 'antonym':
        return -(seeded_polarity)
    return seeded_polarity


def get_shortest_distance(candidate_word, seed_word):
    min = 0
    
    for wn_1 in wn.synsets(candidate_word):
        for wn_2 in wn.synsets(seed_word):
            try:
                distance = 1/wn_1.path_similarity(wn_2)
            except TypeError:
                distance = 0
            if min == 0:
                min = distance
            elif distance < min and distance != 0:
                min = distance
    
    return min


def build_attribute(word_list, seed_word, list_type):
    return [(candidate_word, 
            flip_polarity(list_type, seed_word[1])) 
                for candidate_word in word_list]


def build_connections(depth, parent_word_list, connections, seeded_word_list):
    
    for word in parent_word_list:
        synonyms, antonyms = get_synonym_antonym(word)

        connections.extend((word, syno) for syno in synonyms if (syno, word) not in connections)
        connections.extend((word, anto) for anto in antonyms if (anto, word) not in connections)

        if depth < 2:
            build_connections(depth+1, synonyms, connections, seeded_word_list)
            build_connections(depth+1, antonyms, connections, seeded_word_list)
        
    if depth == 0:
        connections = list(set(connections))
        seeded_pair = itertools.combinations(seeded_word_list, 2)
        
        for pair in seeded_pair:
            connections.remove(pair)
            # connections.remove(pair[::-1])

        return connections


def check_duplicate_seed(word, seeded_word_list):
    for seeded_word in seeded_word_list:
        if word[0] in seeded_word:
            return True
    
    return False


def draw_word_graph(word_graph):
    names = [node[0] for node in word_graph.nodes()]
    
    labels = {word_graph.nodes()[i] : names[i]  for i in range(len(names))}

    positive_node = [node for node in word_graph.nodes() if node[1] == 1]
    negative_node = [node for node in word_graph.nodes() if node not in positive_node]

    pos = networkx.spring_layout(word_graph)
    
    networkx.draw_networkx_nodes(word_graph, pos, nodelist=positive_node, 
                                                node_color='r', 
                                                node_size=600, 
                                                alpha=1)
    networkx.draw_networkx_nodes(word_graph, pos, nodelist=negative_node, 
                                                node_color='g', 
                                                node_size=600, 
                                                alpha=1)

    networkx.draw_networkx_edges(word_graph, pos, width=1.0, alpha=1)
    networkx.draw_networkx_labels(word_graph, pos, labels=labels, font_size=6)

    plt.axis('off')
    plt.show()


def count_flip(path):
    count = 0
    for i, j in zip(range(0, len(path) - 1), range(1, len(path))):
        if path[i][1]*path[j][1] == -1:
            count+=1
    return count


def flip_filter(word_graph, seeded_word_list, threshold):
    for node in word_graph.nodes():
        if node in seeded_word_list:
            continue
        for seeded_word in seeded_word_list:
            for path in networkx.all_simple_paths(word_graph, seeded_word, node):
                count = count_flip(path)
        if count > threshold:
            word_graph.remove_node(node)
            
    return word_graph        

def get_significance_score(word_graph, seeded_word_list, constant=1.1):
    if constant <= 1:
        print('constant will be set to 1.1')
        constant = 1.1
    
    sig_score = []

    for node in word_graph.nodes():
        if node in seeded_word_list:
            continue
        for seeded_word in seeded_word_list:
            for path in networkx.all_simple_paths(word_graph, seeded_word, node):
                score+=1/pow(constant, len(path))
        
        sig_score.append({node:score})
    
    return sig_score