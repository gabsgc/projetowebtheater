class Video():
    def __init__(self, id: int, titulo: str, url_video: str, url_imagem: str, descricao: str, views: int, likes: int, data_publicacao: str, url:str):
        self._id = id
        self._titulo = titulo
        self._url_video = url_video
        self._url_imagem = url_imagem
        self._descricao = descricao
        self._views = views
        self._likes = likes
        self._data_publicacao = data_publicacao
        self._url = url

    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
    
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, value):
        self._titulo = value

    def get_url_video(self):
        return self._url_video
        
    def set_url_video(self, value):
        self._url_video = value

    def get_url_imagem(self):
        return self._url_imagem
        
    def set_url_imagem(self, value):
        self._url_imagem = value

    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, value):
        self._descricao = value
    
    def get_views(self):
        return self._views
    
    def set_views(self, value):
        self._views = value

    def get_likes(self):
        return self._likes
    
    def set_likes(self, value):
        self._likes = value

    def get_data_publicacao(self):
        return self._data_publicacao

    def get_url(self):
        return self._url
    
    def set_url(self, value):
        self._url = value