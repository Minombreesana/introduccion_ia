import numpy as np

class Indexing:

    def __init__(self, user_id):
        self.user_id = user_id
    
    def get_user_id(self):
        indexing = self.user_id[idx]
        idx_req = idx_request
        return indexing[idx_req]

    def get_user_idx(self):
        indexing = self.user_id[idx]
        id_req = id_request
        index = np.where(indexing == id_req)
        return index[0]

   
id = Indexing(np.array([-1,4,5,-1,-1,-1,-1,-1,-1,-1,3,-1,1,-1,2,0]))
idx = np.arange(16)

idx_request = int(input(f'Inserte número de idx: '))
id_request = int(input(f'Inserte número de id: '))

print(id.get_user_id())
print(id.get_user_idx())


