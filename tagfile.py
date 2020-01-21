import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

# 1 Recupera os arquivos MP3
# Lista os arquivos MP3 em uma determinada pasta e subpastas
def encontraArquivosEmPastaRecursivamente(pasta, extensao):
    print(pasta)
    print(extensao)
    arquivosMP3 = []
    caminhoAbsoluto = os.path.abspath(pasta)
    for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
        arquivosMP3.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith(extensao)])
    return arquivosMP3

# 2 Monta lista e testa atualização
def atualizaTagArquivos(diretorio,arquivos,delimitador_arquivo,atualizar):
    total_de_arquivos = 0

    for arq in arquivos:
        nome_mp3 = (arq.split('\\')[2])
        delimitador = nome_mp3.find(delimitador_arquivo)

        if ( delimitador > 0 ):
            total_de_arquivos += 1
            musica = nome_mp3.split(delimitador_arquivo)[1]
            # Retira o ".mp3" do nome da música
            musica = musica.replace('.mp3','')
            # Retira espaços do nome da música
            musica = musica.strip(' ')
            artista = nome_mp3.split(delimitador_arquivo)[0]
            # Retira espaços do nome do artista
            artista = artista.strip(' ')
            print('arquivo original: [{}]  \n   musica: {}  \n  artista: {}'.format(nome_mp3, musica, artista))

            # Atualiza tags
            if ( atualizar == 'S' ):
                print('Vai atualizar a música: {} '.format(musica))
                atualizarArquivos(diretorio, nome_mp3, artista, musica)

    print('--------------------------------------------------')
    print('Total de Arquivos MP3 lidos: {}. '.format(total_de_arquivos))

# 3 Atualiza
def atualizarArquivos(diretorio,nome_arquivo, artista, musica):
    barra = '\\'
    nome_completo_arquivo = diretorio + str(barra) + str(nome_arquivo)
    print(nome_completo_arquivo)
    mp3 = MP3File(nome_completo_arquivo)
    tags = mp3.get_tags()
    print(' Tags Antes:\n {}'.format(tags))
    # Seta o novo artista
    mp3.artist = artista
    mp3.song = musica
    mp3.save()
    tags = mp3.get_tags()
    print(' Tags Depois:\n {}'.format(tags) )



if __name__ == '__main__':
    arquivos = []
    diretorio = 'E:\Teste'
    extensao = 'mp3'

    #Recebe os arquivos MP3
    arquivos = encontraArquivosEmPastaRecursivamente(diretorio,extensao)
    delimitador = '-'


    #Lista os arquivos MP3
    print('-------------------Arquivos MP3--------------------')
    atualizaTagArquivos(diretorio,arquivos,delimitador,'S')
    print('--------------------------------------------------')
