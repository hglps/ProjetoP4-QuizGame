import pandas as pd

df = pd.read_csv('perguntas.csv')


class Question():
    def __init__(self, question, a, b, c, d, answer):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer
        self.visited = False
    

questionList = []

for index, row in df.iterrows():
    question = row.iloc[1]
    a = row.iloc[2]
    b = row.iloc[3]
    c = row.iloc[4]
    d = row.iloc[5]
    answer = row.iloc[6]
    
    new = Question(question, a, b, c, d, answer)
    
    questionList.append(new)

# for i in range(len(questionList)):
#     print(questionList[i].question+'\n')
