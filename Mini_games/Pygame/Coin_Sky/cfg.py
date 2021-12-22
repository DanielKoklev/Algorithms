import os

image_paths = {
    'gold': os.path.join(os.getcwd(), 'resources/images/gold.png'),
    'apple': os.path.join(os.getcwd(), 'resources/images/apple.png'),
    'background': os.path.join(os.getcwd(), 'resources/images/background.jpg'),
    'hero': [os.path.join(os.getcwd(), 'resources/images/%d.png' % i) for i in range(1, 11)]
    }

audio_paths = {
    'bgm': os.path.join(os.getcwd(), 'resources/audios/bgm.mp3'),
    'get': os.path.join(os.getcwd(), 'resources/audios/get.wav'),
    }

font_path = os.path.join(os.getcwd(), 'resources/font/font.TTF')

highest_score_record_filepath = 'highest.rec'

screensize = (800, 600)

background_color = (0, 160, 233)

fps = 30
