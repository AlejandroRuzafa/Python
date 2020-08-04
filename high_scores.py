class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores) 
    def personal_top(self):
        lista_ordenada = sorted(self.scores,reverse=True)
        return lista_ordenada[0:3]
    def report(self):
        ulti_ele = self.latest() 
        mejor_punt = self.personal_best()
        diferencia = (mejor_punt - ulti_ele)
        if ulti_ele == mejor_punt :
            return f"Your latest score was {ulti_ele}. That's your personal best!"
        else:
            return f"Your latest score was {ulti_ele}. That's {diferencia} short of your personal best!"
        




    

    






