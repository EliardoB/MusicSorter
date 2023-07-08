import os
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from mutagen.easyid3 import EasyID3
from tqdm import tqdm
import pyautogui

dsktfolder = os.path.expanduser('~/Desktop')
sdocfolder = os.path.expanduser('~/Documents')
destfolder = 'D:\Music'  


def progress_indicator(future):
    print('.', end='', flush=True)

def sortmp3(archivo, destfolder):

    mp3 = EasyID3(archivo)
    anomp3 = mp3.get('date', [''])[0]  
    albummp3 = mp3.get('album', ['Unknown albummp3'])[0]

    datefolder = os.path.join(destfolder, anomp3)
    albumfolder = os.path.join(datefolder, albummp3)

    if not os.path.exists(datefolder):
        os.makedirs(datefolder)
    if not os.path.exists(albumfolder):
        os.makedirs(albumfolder)

    destino = os.path.join(albumfolder, os.path.basename(archivo))
    shutil.copy(archivo, destino)

def getsortmp3(srcfolder, destfolder):

    archivos = []
    for directorio in [srcfolder]:
        for root, _, files in os.walk(directorio):
            for archivo in files:
                if archivo.endswith('.mp3'):
                    ruta_archivo = os.path.join(root, archivo)
                    archivos.append(ruta_archivo)

    with tqdm(total=len(archivos), desc='Progreso', unit='archivo') as pbar:
        for archivo in archivos:
            sortmp3(archivo, destfolder)
            pbar.update(1)



def tomar_screenshot(self, destfolder):
    while True:
        screenshot = pyautogui.screenshot()

        timestamp = time.strftime('%Y%m%d%H%M%S')
        ss_nombre = f'screenshot_{timestamp}.png'
        ruta_archivo = os.path.join(destfolder, ss_nombre)
        screenshot.save(ruta_archivo)

        if stop_thread == False:
            break

stop_thread = True
screenshot_thread = threading.Thread(target=tomar_screenshot, args=(1, destfolder))
screenshot_thread.start()

getsortmp3(dsktfolder, destfolder)
getsortmp3(sdocfolder, destfolder)

stop_thread = False
screenshot_thread.join()