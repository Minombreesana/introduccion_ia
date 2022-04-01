import numpy as np

class Average_quiery_precision:

    def __init__(self, array):
        self.array = array

    def av_precision(self, predicted_rank, truth_relevance):
        id_cero = np.where(predicted_rank.array == 0)[0]

        TR_1 = truth_relevance.array[:id_cero[1]].astype(int)
        TR_2 = truth_relevance.array[id_cero[1]:id_cero[2]].astype(int)
        TR_3 = truth_relevance.array[id_cero[2]:id_cero[3]].astype(int)
        TR_4 = truth_relevance.array[id_cero[3]:].astype(int)

        precision_1 = np.count_nonzero(TR_1 == 1)/len(TR_1) 
        print(f'la precision para el quiery 1 es: {precision_1}')
        precision_2 = np.count_nonzero(TR_2 == 1)/len(TR_2)
        print(f'la precision para el quiery 2 es: {precision_2}')
        precision_3 = np.count_nonzero(TR_3 == 1)/len(TR_3)
        print(f'la precision para el quiery 3 es: {precision_3}')
        precision_4 = np.count_nonzero(TR_4 == 1)/len(TR_4)
        print(f'la precision para el quiery 4 es: {precision_4}')

        aqp = (precision_1 + precision_2 + precision_3 + precision_4) / 4

        return aqp

q_id = Average_quiery_precision(np.array([1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4]))
predicted_rank = Average_quiery_precision(np.array([0,1,2,3,0,1,2,0,1,2,3,4,0,1,2,3]))
truth_relevance =Average_quiery_precision(np.array([True, False, True, False, True, True, True, False, False, False, False, False, True, False, False, True]))

print(f'El Averge Query Precision es: {q_id.av_precision(predicted_rank,truth_relevance)}')
    
    





