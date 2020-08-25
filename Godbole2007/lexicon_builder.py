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
                if lemma.name() != seeded_word:    
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
            get_shortest_distance(candidate_word, seed_word[0]),
            flip_polarity(list_type, seed_word[2])) 
                for candidate_word in word_list]


def build_connections(depth, seeded_word_list, connections):
    
    for word in seeded_word_list:
        synonym, antonym = get_synonym_antonym(word)
        connections.extend((word, syno) for syno in synonym)
        connections.extend((word, anto) for anto in antonym)

        if depth < 2:
            build_connections(depth+1, synonym, connections)
            build_connections(depth+1, antonym, connections)
        
    if depth == 0:
        return connections