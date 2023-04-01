import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
import math
import pickle

class Recommender():
    def __init__(self):
        filename = 'movie_data.csv'
        self.df = pd.read_csv(filename)
        self.df=self.df.set_index('title')
        self.title_list = list(self.df.index.values)

    
    def cosine_sim(self,a,b):
        return np.dot(a,b)/((math.sqrt(sum(i**2 for i in a)))*(math.sqrt(sum(i**2 for i in b))))
    
    def Sort_Tuple(self,tup):
        tup.sort(key = lambda x: x[1],reverse = True) 
        return tup
    
    def recommend(self,movie):
        self.similarity_score = []
        if movie in self.title_list:
            for i in self.title_list:
                if i != movie:
                    self.similarity_score.append((i,self.cosine_sim(self.df.loc[movie],self.df.loc[i])))
                
        else:
            print('Movie not in the list\nNo recommendations available')
            
        self.similarity_score = self.Sort_Tuple(self.similarity_score)
        
        self.recommendation_list = []

        for i in range(10):
            self.recommendation_list.append(self.similarity_score[i][0])
    
        return self.recommendation_list

# if __name__ == '__main__':
#     obj = Recommender()
#     pickle.dump(obj,open('model.pkl','wb'))
#     model=pickle.load(open('model.pkl','rb'))
