

class Repository:
    def __init__(self, model):
        self.model = model

    def save_obj(self, obj):
        return obj.save()

'''    def valida_login(self, obj):
        return self.save_obj(obj)
    
    def valida_avaliacao(self, obj):
        return obj.save()'''
