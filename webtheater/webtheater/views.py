from django.shortcuts import render

from webtheater.categoria import Categoria
from webtheater.video import Video

video1 = Video(
    1, 
    "Mr. Sunshine, um raio de sol", 
    'video/mr-sunshine.mp4', 
    'img/capa_mrsunshine.png', 
    "Miseuteo Syeonsyain é uma série de televisão sul-coreana exibida  pela emissora tvN entre 7 de julho a 30 de setembro de 2018, com um total de 24 episódios, a série também estreou internacionalmente pela plataforma Netflix.", 
    3240, 
    4000, 
    '07/07/2021',
    'mr_sunshine_um_raio_de_sol')

video2 = Video(
    2, 
    "Crash Landing on You", 
    'video/cloy.mp4', 
    'img/capa_cloy.png', 
    "O drama é sobre uma herdeira rica chamada Yoon Se Ri, que, enquanto voava de parapente, é forçada a aterrissar na Coreia do Norte por causa dos ventos fortes. Um oficial norte-coreano chamado Ri Jung Hyuk a esconde e protege, assim, começando a amá-la", 
    4203, 
    3210, 
    '05/12/2020',
    'crash_landing_on_you'
    )

video3 = Video(
    3, 
    "Descendents of the Sun", 
    'video/descendentes-do-sol.mp4', 
    'img/capa_dots.png', 
    "O capitão Yoo Shi Jin das forças especiais se apaixona pela cirurgiã Kang Mo Yeon. Os dois lutam para viver um romance em meio a um país devastado pela guerra.", 
    3921, 
    2800, 
    '05/03/2020',
    'descendents_of_the_sun')

video4 = Video(
    4,
    "Desafiando Gigantes",
    'video/desafiando-gigantes.mp4',
    'img/capa_desafiando_gigantes.png',
    "Cultivando Valores - União. Comprometer-se com o único propósito, reconhecendo que precisamos uns dos outros para entregar tudo com excelência.",
    4020,
    3200,
    '29/12/2019',
    'desafiando_gigantes'
)

video5 = Video(
    5,
    "Zootopia",
    'video/zootopia.mp4',
    'img/capa_zootopia.png',
    "Zootopia é uma cidade diferente de tudo o que você já viu. Formada por “bairros-habitat”, como a elegante Praça Sahara e a gelada Tundralândia, essa metrópole abriga uma grande diversidade de animais irreverentes sempre prontos para encarar uma nova e divertida aventura.",
    3860,
    2340,
    '04/04/2020',
    'zootopia'
)

video6 = Video(
    6,
    "WiFi Ralph: Quebrando a Internet",
    'video/detona-ralph.mp4',
    'img/capa_ralph.png',
    "Ralph, o mais famoso vilão dos videogames, e Vanellope, sua companheira atrapalhada, iniciam mais uma arriscada aventura. Após a gloriosa vitória no Fliperama Litwak, a dupla viaja para a world wide web, no universo expansivo e desconhecido da internet. ",
    2350,
    1990,
    '05/03/2020',
    'detona_ralph'
)

video7 = Video(
    7,
    "You Say",
    'video/you-say.mp4',
    'img/capa_yousay.png',
    "By Lauren Daigle",
    4550,
    4390,
    '10/05/2021',
    'you_say'
)

video8 = Video(
    8,
    "Além do Rio Azul",
    'video/alem-do-rio-azul.mp4',
    'img/capa_rioazul.png',
    "Cover by Júlia Vitória",
    3350,
    2890,
    '05/07/2021',
    'alem_do_rio_azul'
)

video9 = Video(
    9,
    "Enough",
    'video/enough.mp4',
    'img/capa_enough.png',
    "By Koryn Hawthorne",
    3050,
    2670,
    '18/11/2021',
    'enough'
)

videos_drama = [video1, video2, video3]
videos_filme = [video4, video5, video6]
videos_musica = [video7, video8, video9]

categoria_drama = Categoria(1, "Drama", "Dramas sul-coreanos", 'static/img/categoria_drama.png', videos_drama)
categoria_filme = Categoria(2, "Filme", "Filmes que inspiram...", 'static/img/categoria_filme.png', videos_filme)
categoria_musica = Categoria(3, "Música", "Músicas para motivar", 'static/img/categoria_musica.png', videos_musica)
categorias = [categoria_drama, categoria_filme, categoria_musica]

def index(request):
    return render(request, 'index.html', {'categorias': categorias})

def exibir_drama(request, url:str):
    for drama in videos_drama:
        if drama.get_url() == url:
            return render(request, 'video.html', {'video': drama})
    return render(request, 'video.html', {'video': drama})

def exibir_filme(request, url:str):
    for filme in videos_filme:
        if filme.get_url() == url:
            return render(request, 'video.html', {'video': filme})
    return render(request, 'video.html', {'video': filme})

def exibir_musica(request, url:str):
    for musica in videos_musica:
        if musica.get_url() == url:
            return render(request, 'video.html', {'video': musica})
    return render(request, 'video.html', {'video': musica})