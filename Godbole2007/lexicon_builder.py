import itertools

from nltk.corpus import wordnet as wn
from WordGraph import Node, Graph

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