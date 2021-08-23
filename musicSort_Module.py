import os
import mutagen
import shutil
import re


def MusicSort(InPath, OutPath, metadata):
    def DirectoryManager(path, music, title, OutPath):  # 음악 디렉토리 생성
        musicPath = OutPath+r'/music/'+music  # 이동할 경로
        print(musicPath)
        if not os.path.exists(musicPath):  # 폴더가 없으면 생성
            os.mkdir(musicPath)
            print('[{0}] 폴더 생성완료'.format(music))
        shutil.move(path, musicPath+r'/'+title)

    def searchMusic(originalpath, musics, title):  # 음악파일 찾기
        for (path, dir, files) in os.walk(originalpath):
            for filename in files:
                ext = os.path.splitext(filename)[-1]  # 파일 확장자 확인
                if ext in exts:  # flac, mp3파일만 리스트에 추가
                    musics.append(path+r'/'+filename)
                    title.append(filename)

    originalpath = InPath
    musics = []  # 음악 리스트
    title = []  # 음악 제목
    exts = ['.flac', '.mp3', '.aif', '.wav']

    if not os.path.exists(OutPath+r'/music'):  # 폴더가 없으면 생성
        os.mkdir(OutPath+r'/music')

    searchMusic(originalpath, musics, title)

    for i in range(len(musics)):
        ext = os.path.splitext(musics[i])[-1]
        try:
            if ext == '.flac':
                music = mutagen.File(musics[i])[metadata][0]
            else:
                if metadata == 'ARTIST':
                    music = mutagen.File(musics[i])["TPE1"][0]
                elif metadata == 'ALBUM':
                    music = mutagen.File(musics[i])["TALB"][0]
                elif metadata == 'DATE':
                    music = mutagen.File(musics[i])["TDRC"][0]
            if metadata != 'DATE':
                music = re.sub(r"\/|\:|\<|\>|\\|\*|\?|\"|\||",
                               "", music)  # 디렉토리 생성 규칙 준수
            DirectoryManager(musics[i], music, title[i], OutPath)
        except:
            print('에러')
