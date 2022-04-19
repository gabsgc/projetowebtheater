from webtheater.video import Video

class Categoria():
    def __init__(self, id: int, titulo: str, descricao: str, url_imagem: str, videos: list[Video]):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._url_imagem = url_imagem
        self._videos = videos
        
    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
    
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, value):
        self._titulo = value

    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, value):
        self._descricao = value
    
    def get_url_imagem(self):
        return self._url_imagem
    
    def set_url_imagem(self, value):
        self._url_imagem = value
    
    def get_videos(self):
        return self._videos
    
    def set_videos(self, video):
        self._videos.append(video)