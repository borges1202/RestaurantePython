
class Avaliacao():
    def __init__(self, client , notation):
        self.client = client
        self.notation = notation
     
    @property 
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        if not isinstance(client, str):
            raise ValueError('Coloque apenas textos')
        else:
            self._client = client.title().strip()

    @property
    def notation(self):
        return self._notation
    
    @notation.setter
    def notation(self, notation):
        if not isinstance(notation, int):
            raise ValueError('Coloque apenas numeros')
        else:
            self._notation = notation
            
    @staticmethod
    def average_rating(self):
        if not self._assessment_list:
            return 0
        else:
            average = sum(avaliacao.notation for avaliacao in self._assessment_list)/len(self._assessment_list)
        return round(average,1)
