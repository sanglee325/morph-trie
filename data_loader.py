import pandas as pd

class grammar:
    def __init__(self):
        self.rule = None
        
    def load(self, path):
        try:
            self.rule = pd.read_csv(path, sep = " ", names=['pos1', 'pos2'])
            print("[SUCCESS] load grammar")
            return self.rule
        except:
            print("[ERROR] load grammar")

    def check(self, pos1, pos2):
        for index, data in self.rule.iterrows():
            if data['pos1'] in pos1 and data['pos2'] in pos2:
                return True, data['pos1'], data['pos2']
        
        return False, None, None


class dictionary:
    def __init__(self):
        self.data = None

    def load(self, path):
        try:
            self.data = pd.read_csv(path, sep = "/", names=['word', 'pos'])
            print("[SUCCESS] load dictionary")
            return self.data
        except:
            print("[ERROR] load dictionary")