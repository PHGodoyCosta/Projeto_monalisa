import os
from selenium import webdriver
from moviepy.editor import *
import moviepy.editor as mp
import time
#import cv2
#from tensorflow.keras.models import load_model
#from mtcnn.mtcnn import MTCNN
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
        des1 = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Resultados\\danca_com_a_cara\\{nome}.mp4"
        des2 = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Resultados\\danca_com_a_cara\\Postados\\{nome}.mp4"
        shutil.move(des1, des2)

    def identificador2(self, nome):
        print("Deixando ele 256x256")
        hehe.diminuindo_para_256(f"{nome}.mp4")
        print("Fazendo DeepFake")
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\deepfake1imagem")
        DeepFake(nome)
        print("Editando deepfake")
        hehe.editor(nome)
        print("Postando...")
        hehe.tiktok_login(f"Monalisa_{nome}")
        hehe.postado(f"Monalisa_{nome}")

    def identificador(self):
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
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
                    des1 = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\{video}.mp4"
                    des2 = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{video}.mp4"
                    shutil.move(des1, des2)

                    hehe.identificador2(video)
                    os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
                    os.unlink(f"{video}.mp4")
        else:
            print("Tenho algum tik tok no meu txt")
            with open("videos.txt", "r") as arquivo:
                for linha in arquivo:
                    #https://www.tiktok.com/@bellapoarch/video/6879839839039032581?lang=pt-BR&is_copy_url=1&is_from_webapp=v1\Fofinho
                    #https://www.tiktok.com/@bellapoarch/video/6953691011474410757?lang=pt-BR&is_copy_url=1&is_from_webapp=v1\O nome que vc quer
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
                    os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
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
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos")
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
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos")
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
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos")
        clipe = VideoFileClip(f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{nome}")
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
            {"name":"bck","value":"F53C20E932835C10AE7C0BA6BEFA6DD7~-1~YAAQ3zfkusKiN1h6AQAA12sYZgbMjNC+hFCPSN0LMfspgGXe4mZ9TUBthZwj5WfH8pNJ/X9VaHAAuTfDJafuxTkP0pJDNtr0Y6/ujMhE7ZglcIkgnw3xCk+aSAhFl8PKtZAU2t5NVuGccobvoi9nqZjxtl3dhSacQKKj94rOT/Bs81yXf4J1Yvj+4XvPBOaQGUrq6n/YSHF30pw8fz/cYu50xTUdnjaU+f4cPIo6QF/nL91jAUlCNtdcmzts2zXNw1c4o9Mgk/i3aqrACw7/6eRkC1+K0N4gchtBpaCA0g92+3uNPWzeY2lZwUhfj8Jy5pg/RH4IWQK3jYbDyGS9iRoCWC4lPgI5yZlpQ5N6EpCvJ+AuFvppKu+U+fQceH9SJrseLI8/MVXpXgcSDaWuqeAUk2pEnIwY3A==~-1~-1~-1"},
            {"name":"bm_sv","value":"ECDD323DBD95798607608EF50D7A0FD0~vs/C8LQHfFbrMrAttq3Q99FWdacoaE1YJpvLPONVMEevz5rqxe16MFMYJPinbS4G7bgmenf+3dIuFFx6mdHgbyOzfkSIqUIM8Gdrp/unLVCjlo2sfsboDhwW5wsOX4I40gDnZMp3ksIH8LRxIx4J5FH4KqftARylJSax+EvKgO0="},
            {"name":"passport_fe_beating_status","value":"true"},
            {"name":"s_v_web_id","value":"verify_kqlxj7o4_rmzZPHoD_h1gq_4bOG_BV1B_mGbEEG2P0q1k"},
            {"name":"sid_tt","value":"6ba611a1660ef10f483bf52a282de0d7"},
            {"name":"ak_bmsc","value":"669E55FCA85EC2EAA8723369AF4EB664~000000000000000000000000000000~YAAQ3zfkuoyiN1h6AQAAd44FZgz39qz5ZMXU2LGNWpKBWG+7sBHyFNzB6t0d/oCLBJVjwR8f0p7NcWZkYdAYYW+IcWqDztwNn6DIoRb1NybA3F/jY53KmMAh3AeY8aPy8SjpX78Mmm1BU5HJvDu0pad1vL+mnlsaOZChokWrDnjHSEDZRuhJFMOrXJ0psuShS/FDOZQDMeNfCk3PK47FFmZEMgiLd7f0CoZrEfMcpj7seSEjrJcErs150ctS7G+Jz441jKCUnX63NS4bt2c/4gfYYGk70ml/Vgi1ceFwTY4L6c9ywZ9PUqRUnmC6gfpGVtmAZDHRaS0ZdGs7NowZO1CEQNbh/S9g2mPnkwdWWHrACMENYDo5vgiGRINLURN0d/5hOiD5c6hLpLoq"},
            {"name":"R6kq3TV7","value":"AOijkmV6AQAAuHw6agno67fUAHBPYlQyEaqNbcj5qxFoADAlP_yr4fKO1Am9|1|0|bfe585782c78051a383cd2c34e6b0c77de209a66"},
            {"name":"xgplayer_device_id","value":"79360462586"},
            {"name":"sessionid","value":"6ba611a1660ef10f483bf52a282de0d7"},
            {"name":"MONITOR_WEB_ID","value":"6,94E+18"},
            {"name":"sessionid_ss","value":"6ba611a1660ef10f483bf52a282de0d7"},
            {"name":"uid_tt_ss","value":"7d724ae9cf526bcbdd1d233e98ba72fe7528763c50ecda1f80c96e4ee12f1334"},
            {"name":"xgplayer_user_id","value":"9,65E+11"},
            {"name":"cmpl_token","value":"AgQQAPNkF-RMpbDkaskMPV08-iY6W_xRP4fvYP7XDQ"},
            {"name":"store-country-code","value":"br"},
            {"name":"passport_csrf_token_default","value":"c025769cce755867a956e86e275f515b"},
            {"name":"uid_tt","value":"7d724ae9cf526bcbdd1d233e98ba72fe7528763c50ecda1f80c96e4ee12f1334"},
            {"name":"sid_guard","value":"6ba611a1660ef10f483bf52a282de0d7%7C1625077195%7C5184000%7CSun%2C+29-Aug-2021+18%3A19%3A55+GMT"}
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
        video = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Resultados\\danca_com_a_cara\\{nome}.mp4"
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
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
        cwd = os.getcwd()
        files = os.listdir(cwd)
        for file in files:
            #if file[len(file) - 1] == "4":  // Caso eu queira fazer com todos os videos :)
            if file == "arquivo_gerado_Slomo.mp4": #"build_bitch.mp4":
                clipe = VideoFileClip(f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\{file}")
                right_now = VideoFileClip(f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\right_now-2.mp4")
                #audios = AudioClip("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\dancinha_leve.mp3")
                a, l = clipe.size
                print("O Clipe {} tem {}x{}".format(file, a, l))
                #Propriedades: Clipe.size, clipe.duration(em segundos), clipe.fps, clipe.ipython_display(Plota o video :))
                #clipe2 = concatenate_videoclips([clipe, lazaro])
                duracao = int(right_now.duration)
                print("O tamanho da musica é {}".format(duracao))
                print(f"Seu tipo é {type(duracao)}")
                clipe = clipe.speedx(final_duration=duracao)
                clipe = clipe.set_audio(right_now.audio)
                clipe.ipython_display(width=256)
                #clipe2 = clipe.subclip(t_end=(0,0,30)) // Horas, minutos, e segundos
                #clipe2.write_videofile("Diretorio :)") //Escrevendo o video no disco

    def editor(self, arquivo):
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
        with VideoFileClip("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\Projeto_Monalisa\\Resultados\\danca_com_a_cara\\arquivo_gerado.mp4") as clipe:
            with VideoFileClip(f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{arquivo}.mp4") as danca:
                #clipe = VideoFileClip("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\Projeto_Monalisa\\Resultados\\danca_com_a_cara\\arquivo_gerado.mp4")
                #danca = VideoFileClip(f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{arquivo}.mp4")
                a, l = clipe.size
                print("O Clipe tem {}x{}".format(a, l))
                duracao = int(danca.duration)
                print("O tamanho da musica é {}".format(duracao))
                print(f"Seu tipo é {type(duracao)}")
                clipe = clipe.speedx(final_duration=duracao)
                os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Resultados\\danca_com_a_cara")
                clipe = clipe.set_audio(danca.audio)

                os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\Projeto_Monalisa\\Resultados\\danca_com_a_cara")
                clipe.ipython_display(width=480)
                os.rename("__temp__.mp4", f"Monalisa_{arquivo}.mp4")
                clipe = "opa"
                danca = "Opa"
                print("Esperando o tempo suficiente")
                time.sleep(1)
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\Projeto_Monalisa\\Resultados\\danca_com_a_cara")
        os.unlink("arquivo_gerado.mp4")

        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos")
        os.unlink(f"{arquivo}.mp4")

    def redimencionador_facial(self):
        os.chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador")
        clip = VideoFileClip("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\Modelo 2-3-1.mp4")
        clip = clip.subclip(0, 5)
        frame = clip.get_frame(3)
        plt.imshow(frame, interpolation ='nearest')
        plt.savefig('teste.png', format='png')
        #video = cv2.VideoCapture("Modelo 2-3-1.mp4")
        foto_redimensionada = Image.open("teste.png")
        foto_redimensionada = foto_redimensionada.resize((256, 256), Image.LANCZOS)
        foto_redimensionada.save("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\renderizada.png")
        os.unlink("teste.png")
        if __name__ == "__main__":
            hehe.extraindo_face()
        
        #facenet = load_model()
        print("tudo certo")
    
    def extraindo_face(self):
        detector = MTCNN() #Chama o modulo que converte os arquivos
        img = Image.open("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\renderizada.png") #Carrega a foto no pillow
        img = img.convert("RGB") #Converte em RGB caso ainda não esteja
        array = asarray(img) #Transforma a foto em um array estilo numpy // é necessario pq o o MTCNN só aceita arrays em numpy
        results = detector.detect_faces(array) #Detecta a face
        x1, y1, width, height = results[0]['box']
        x2 = x1 + width
        y2 = y1 + height
        face = array[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image.save("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\face.png")
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
