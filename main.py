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
        print("[SUCCESS] creating TRIE")    
    
    except:
        print("[ERROR] creating TRIE")

    #print(trie.search('저녁'))

    sentence = input("Input the sentence: ")
    syntatic_word = sentence.split(' ') # 어절로 문장 분리

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
        '''
        # table 출력
        for i in range(0, len_word):
            for j in range(len_word+1):
                print(ptable[i][j], end='\t\t')
            print()
        '''
        
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


                            
        
