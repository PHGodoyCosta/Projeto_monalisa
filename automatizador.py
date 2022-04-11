import os
from selenium import webdriver
from moviepy.editor import *
import moviepy.editor as mp
import time
from PIL import Image
import pickle, gzip
from numpy import asarray
from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup
from executador import DeepFake

class Monalisa:

    def postado(self, nome):
        import shutil
        des1 = f"<caminho do meu vídeo>"
        des2 = f"<novo caminho do meu vídeo>"
        shutil.move(des1, des2)

    def identificador2(self, nome):
        print("Deixando ele 256x256")
        hehe.diminuindo_para_256(f"{nome}.mp4")
        print("Fazendo DeepFake")
        os.chdir("<Ele volta para esse pasta>") #Essa linha é necessária para usar a função DeepFake() de executador.
        DeepFake(nome)
        print("Editando deepfake")
        hehe.editor(nome)
        print("Postando...")
        hehe.tiktok_login(f"Monalisa_{nome}")
        hehe.postado(f"Monalisa_{nome}")

    def identificador(self):
        os.chdir("<Aqui ele entra em uma pasta alternativa, vamos chama-la de Postador>") #Uso essa pasta para salvar os vídeos e guardar alguns arquivos de textos que vão ser usados mais para frente.
        arquivo = open("videos.txt", "r").read()
        if arquivo == "":
            meus_arquivos = []
            cwd = os.getcwd()
            arquivos = os.listdir(cwd)
            for c in arquivos:
                n1 = len(c) - 4
                print(c[n1:], "\n")
                if c[n1:] == ".mp4":
                    meus_arquivos.append(c)
            if meus_arquivos == []:
                print("Não tenho muito o que fazer :(")
                return False
            else:
                import shutil
                print("Não tenho links mais tenho um video para editar")
                for video in meus_arquivos:
                    video = video[:len(video) - 4]
                    print(f"Meu video é {video}")
                    des1 = f"<Caminho do video localizado em Postador>"
                    des2 = f"<Caminho novo, para uma pasta chamada Exemplos>" #essa pasta está dentro de Postador
                    shutil.move(des1, des2)

                    hehe.identificador2(video)
                    os.chdir("<Caminho do postador>")
                    os.unlink(f"{video}.mp4")
        else:
            print("Tenho algum tik tok no meu txt")
            with open("videos.txt", "r") as arquivo:
                for linha in arquivo:
                    n1 = linha.split("\\")
                    if n1[1][len(n1) - 1] == "!":
                        nome = n1[1]
                    else:
                        nome = f"{n1[1]}"
                    linha = n1[0]
                    print(f"O nome escolhido foi: {nome}")
                    print("Baixando {}\n".format(linha))
                    #while True:
                    #    try:
                    hehe.baixando2(linha, nome)
                    #    except Exception as erro:
                    #        print("Não consegui baixar :(")
                    #        print(erro)
                    #    else:
                    #        break
                    hehe.identificador2(nome)
                    print("Agora que eu postei vou anotar no meu log")
                    os.chdir("<Caminho do postador>")
                    from datetime import datetime
                    h1 = datetime.now()
                    h2 = h1.date()
                    h3 = h1.hour
                    h4 = h1.minute
                    h5 = h1.second
                    h6 = h1.weekday()
                    dias = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo")
                    if len(str(h3)) == 1:
                        h3 = f"0{h3}"
                    if len(str(h4)) == 1:
                        h4 = f"0{h4}"
                    if len(str(h5)) == 1:
                        h5 = f"0{h5}"
                    with open("logs.txt", "a+") as arquivo:
                        arquivo.write(f"\nPostado: Monalisa_{nome}.mp4 // {h2} // {dias[h6]} // {h3}:{h4}:{h5}")
            with open("videos.txt", "w+") as arquivo2:
                arquivo2.write("")
    def baixando2(self, url, nome):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://snaptik.app/pt")
        time.sleep(4)
        caixa_input = driver.find_element_by_id("url").send_keys(url)
        time.sleep(1)
        download = driver.find_element_by_id("submiturl").click()
        time.sleep(5)
        div = driver.find_element_by_xpath('//*[@id="snaptik-video"]/article/div[2]/div')
        div = div.get_attribute("innerHTML")
        soup = BeautifulSoup(str(div), 'html.parser')
        a = soup.find_all("a")
        a = a[1]
        a = a['href']
        os.chdir("<Caminho de exemplos>")
        req = requests.get(f"{str(a)}")
        with open(f"{nome}.mp4", "wb") as f:
            f.write(req.content)
        driver.close()

    def baixando_tiktok(self, url, nome):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://pt.savefrom.net/download-from-tiktok")
        time.sleep(5)
        link = driver.find_element_by_xpath('//*[@id="sf_url"]').click()
        try:
            link.send_keys(url)
        except:
            link = driver.find_element_by_xpath('//*[@id="sf_url"]')
            link.click()
            link.send_keys(url)
        baixa = driver.find_element_by_xpath('//*[@id="sf_submit"]')
        baixa.click()
        time.sleep(10)
        os.chdir("<Caminho de exemplos>")
        html = driver.find_element_by_tag_name("html")
        html = html.get_attribute("innerHTML")
        soup = BeautifulSoup(str(html), 'html.parser')
        div = soup.find("div", {"class":"def-btn-box"})
        a = div.find("a")
        a = a['href']
        print(a)
        req = requests.get(str(a))
        with open(f"{nome}.mp4", "wb") as f:
            f.write(req.content)
        driver.close()

    def diminuindo_para_256(self, nome):
        #É importante diminuir o vídeo antes de joga-lo para o algotimo pois, ele só aceita videos com essas proporções.
        os.chdir("<Caminho de exemplos>")
        clipe = VideoFileClip(f"<Caminho do video que será diminuido>") #Esse video se encontra na pasta exemplos.
        clipe = clipe.resize((256, 256))
        clipe.ipython_display(width=256)
        os.unlink(nome)
        os.rename("__temp__.mp4", nome)


    def tiktok_login(self, nome):
        agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=" + agent)
        options.add_argument("--headless")
        #options.add_argument("--profile-directory=Default")
        #options.add_argument("--user-data-dir={}".format(dir_cookie))
        driver = self.driver = webdriver.Chrome(chrome_options=options)
        objeto = (
            <"Cookies da minha conta do tik tok">
        )
        driver.get("https://www.tiktok.com/login")
        for c in objeto:
            driver.add_cookie(c)
            print(c, "\n")
        time.sleep(2)
        driver.get("https://www.tiktok.com/upload?lang=pt-BR")
        time.sleep(4)
        try:
            cancelar = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[3]/div[5]/div[3]/button[1]').click()
        except:
            pass
        video = f"<Pasta onde está o video pronto>"
        arquivo = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div/div/input')
        arquivo.send_keys(video)
        time.sleep(5)
        legenda = f"{nome}! #foryou #vaiparaofycaramba #deepfake #trend #trending #viral #fy #fyp #facedance #monalisa"
        try:
            imagem = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/img[2]').click()
        except:
            print("Não consegui selecionar a imagem correta")
        time.sleep(2)
        l2 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div').click()
        time.sleep(2)
        #l1 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/div/div[1]/input')
        l1 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/span')
        l1.send_keys(legenda)
        time.sleep(3)

        publicar = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[3]/div[6]/button[2]').click()
        print("postado com sucesso :)")
        time.sleep(5)
        driver.close()
    
    def existente(self):
        os.chdir("<Caminho do postador>")
        cwd = os.getcwd()
        files = os.listdir(cwd)
        for file in files:
            #if file[len(file) - 1] == "4":  // Caso eu queira fazer com todos os videos :)
            if file == "arquivo_gerado_Slomo.mp4": #"build_bitch.mp4":
                clipe = VideoFileClip(f"<Caminho do postador>\\{file}")
                right_now = VideoFileClip(f"<Caminho do postador>\\right_now-2.mp4")
                a, l = clipe.size
                print("O Clipe {} tem {}x{}".format(file, a, l))
                duracao = int(right_now.duration)
                print("O tamanho da musica é {}".format(duracao))
                print(f"Seu tipo é {type(duracao)}")
                clipe = clipe.speedx(final_duration=duracao)
                clipe = clipe.set_audio(right_now.audio)
                clipe.ipython_display(width=256)

    def editor(self, arquivo):
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
        with VideoFileClip("Caminho do vídeo pronto") as clipe:
            with VideoFileClip(f"<Caminho de Exemplos>\\{arquivo}.mp4") as danca:
                a, l = clipe.size
                print("O Clipe tem {}x{}".format(a, l))
                duracao = int(danca.duration)
                print("O tamanho da musica é {}".format(duracao))
                print(f"Seu tipo é {type(duracao)}")
                clipe = clipe.speedx(final_duration=duracao)
                os.chdir("<Pasta onde está o video pronto (Vamos chama-la de danca_com_a_cara)>")
                clipe = clipe.set_audio(danca.audio)

                os.chdir("<Caminho de danca_com_a_cara>")
                clipe.ipython_display(width=480)
                os.rename("__temp__.mp4", f"Monalisa_{arquivo}.mp4")
                clipe = "opa"
                danca = "Opa"
                print("Esperando o tempo suficiente")
                time.sleep(1)
        os.chdir("<Caminho de danca_com_a_cara>")
        os.unlink("arquivo_gerado.mp4")

        os.chdir("<Caminho de exemplos>")
        os.unlink(f"{arquivo}.mp4")

    def redimencionador_facial(self):
        os.chdir("<Caminho do postador>")
        clip = VideoFileClip("<Caminho do postador>\\Modelo 2-3-1.mp4")
        clip = clip.subclip(0, 5)
        frame = clip.get_frame(3)
        plt.imshow(frame, interpolation ='nearest')
        plt.savefig('teste.png', format='png')
        #video = cv2.VideoCapture("Modelo 2-3-1.mp4")
        foto_redimensionada = Image.open("teste.png")
        foto_redimensionada = foto_redimensionada.resize((256, 256), Image.LANCZOS)
        foto_redimensionada.save("<Caminho do postador>\\renderizada.png")
        os.unlink("teste.png")
        if __name__ == "__main__":
            hehe.extraindo_face()
        
        #facenet = load_model()
        print("tudo certo")
    
    def extraindo_face(self):
        detector = MTCNN() #Chama o modulo que converte os arquivos
        img = Image.open("<Caminho do postador>\\renderizada.png") #Carrega a foto no pillow
        img = img.convert("RGB") #Converte em RGB caso ainda não esteja
        array = asarray(img) #Transforma a foto em um array estilo numpy // é necessario pq o o MTCNN só aceita arrays em numpy
        results = detector.detect_faces(array) #Detecta a face
        x1, y1, width, height = results[0]['box']
        x2 = x1 + width
        y2 = y1 + height
        face = array[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image.save("<Caminho do postador>\\face.png")
        os.unlink("renderizada.png")
    
    def zoom(self):
        size = (1920, 1080)

        img = 'https://www.colorado.edu/cumuseum/sites/default/files/styles/widescreen/public/slider/coachwhip2_1.jpg'

        slide = mp.ImageClip(img).set_fps(25).set_duration(10).resize(size)

        slide = slide.resize(lambda t: 1 + 0.04 * t)  # Zoom-in effect
        slide = slide.set_position(('center', 'center'))
        slide = mp.CompositeVideoClip([slide], size=size)

        slide.write_videofile('zoom-test-1.mp4')

if __name__ == "__main__":
    hehe = Monalisa()
    hehe.identificador()
    hehe.identificador()
