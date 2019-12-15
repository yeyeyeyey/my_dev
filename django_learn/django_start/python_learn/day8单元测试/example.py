class Dict(dict):
    def __init__(self,**kw):
        super.__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError :
            raise AttributeError(r"字典中没有找到%s 这个键值"%key)
    def __setattr__(self, key, value):
        self[key] = value
