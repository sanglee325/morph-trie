# Assignment 1

## 설명

TRIE 자료 구조를 활용하여 tabular parsing을 구현한 과제 입니다.

## 실행환경

* Ubuntu 18.04.4 LTS
* python==3.7.7

## requirements

* pandas==1.2.3

## 사용법

* `main.py` 파일을 실행합니다.
    ``` bash
    $ python main.py
    ```
    ``` bash
    [SUCCESS] load grammar
    [SUCCESS] load dictionary
    [SUCCESS] creating TRIE
    Input the sentence: 나는 어제 저녁을 먹고 집에 갔다
    나는: 나/(대명사) 는/(보조사)
    어제: 어제/(일반부사)
    저녁을: 저녁/(일반명사) 을/(목적격조사)
    먹고: 먹/(동사) 고/(연결어미)
    집에: 집/(일반명사) 에/(부사격조사)
    갔다: 갔/(동사) 다/(종결어미)
    ```
