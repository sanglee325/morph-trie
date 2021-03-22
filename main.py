import pandas as pd

from data_loader import grammar, dictionary
from TRIE import TRIE

if __name__=='__main__':
    # load grammar
    G = grammar()
    G.load('./data/grammar.txt')

    # load dictionary
    D = dictionary()
    D.load('./data/dictionary.txt')

    # define TRIE data structure
    trie = TRIE()

    # loading words to TRIE
    try:
        for index, data in D.data.iterrows():
            trie.insert(word=data['word'], pos=data['pos'])
        #print("[SUCCESS] creating TRIE")    

    except:
        print("[ERROR] creating TRIE")

    sentences = [
            "그는 빨리 집에 가고 싶어한다",
            "나는 어제 저녁을 먹고 집에 갔다",
            "운이 매우 좋은 그에게 운동은 운명이 그를 시험하려 던진 과제다",
            "강아지조차 키울 수 없는 아파트 속에 나는 애완동물을 사육하고 있는 것이다",
            "그날 밤 고양이는 새끼를 모조리 잡아먹고 달랑 대가리만 남겨 피 칠한 입으로 밤새 시끄럽게 울었다"
            ]

    for ii, (sentence) in enumerate(sentences):
        syntatic_word = sentence.split(' ') # 어절로 문장 분리
        print('[%02d] %s'%(ii+1, sentence))

        for idx, (word) in enumerate(syntatic_word):
            ptable = []
            len_word = len(word)
            print('%s: '%(word), end='')
            # create parse table
            for i in range(len_word+1):
                ptable.append([])
                for j in range(len_word+1):
                    ptable[i].append([])

            for i in range(len_word):
                for j in range(len_word):
                    curr_word = word[i:j+1]
                    if trie.search(curr_word): # TRIE 사전에 단어가 있는 경우
                        ptable[i][j+1].append(curr_word)

            # 형태소 문법 확인
            for i in range(len_word):
                for j in range(1, len_word+1):
                    element = ptable[i][j]
    
                    if element:
                        for k in range(j, len_word+1):
                            if ptable[j][k]:
                                gcheck, pos1, pos2 = G.check(trie.pos(element), trie.pos(ptable[j][k]))
                                if gcheck:
                                    print('%s/(%s) %s/(%s)'%(element[0], pos1, ptable[j][k][0], pos2), end=' ')

            element = ptable[0][len_word]
            if element:
                none_list = ['-']
                gcheck, pos1, pos2 = G.check(trie.pos(element), none_list)
                if gcheck:
                    print('%s/(%s)'%(element[0], pos1), end=' ')

            print()
        print()



