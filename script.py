import yt_dlp

url = 'https://www.youtube.com/watch?v=r7pMqU2kYqc&t=40s'
url = 'https://www.youtube.com/watch?v=U88M8YbAzQk'

ydl_opts = {
    'writesubtitles': True,  # Скачать субтитры
    'subtitleslangs': ['ru'],  # Языки субтитров (например, en, ru)
    'writeautomaticsub': True,  # Автоматические субтитры
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])