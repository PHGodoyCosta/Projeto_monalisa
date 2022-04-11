import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
import warnings
import time
from skimage import img_as_ubyte
import winsound
from os import chdir

def DeepFake(nome):
    warnings.filterwarnings("ignore")

    #dire = f"C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{video}.mp4"
    source_image = imageio.imread('C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Imagens\\05.png')
    driving_video = imageio.mimread(f'C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Postador\\exemplos\\{nome}.mp4')


    #O modelo atual só funciona com as dimensões 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    def display(source, driving, generated=None):
        fig = plt.figure(figsize=(8 + 4 * (generated is not None), 6))

        ims = []
        for i in range(len(driving)):
            cols = [source]
            cols.append(driving[i])
            if generated is not None:
                cols.append(generated[i])
            im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
            plt.axis('off')
            ims.append([im])

        ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
        plt.close()
        return ani

    #imageio.mimsave('../Video_modelo_gerado.mp4', [img_as_ubyte(frame) for frame in driving_video])
    #HTML(display(source_image, driving_video).to_html5_video())

    print("Importando o treinamento")
    time.sleep(1)

    from demo import load_checkpoints
    generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', checkpoint_path='C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Imagens\\vox-cpk.pth.tar')

    print("Fazendo o video!!")
    time.sleep(1)

    from demo import make_animation
    from skimage import img_as_ubyte

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

    #save resulting video
    chdir("C:\\Users\\Windows 10\\OneDrive\\Futuristas\\I.As\\Projeto_Monalisa\\Resultados\\danca_com_a_cara")
    imageio.mimsave('arquivo_gerado.mp4', [img_as_ubyte(frame) for frame in predictions])
    #video can be downloaded from /content folder

    #HTML(display(source_image, driving_video, predictions).to_html5_video())
    winsound.Beep(500, 1000)