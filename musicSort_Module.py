import os,mutagen,shutil,re
from warnings import catch_warnings

def MusicSort(InPath,OutPath,metadata):
    try:
        def DirectoryManager(path,music,title,OutPath):           #음악 디렉토리 생성
            musicPath =  OutPath+'\\music\\'+music                     #이동할 경로


            if not os.path.exists(musicPath):           #폴더가 없으면 생성
                os.mkdir(musicPath)
                print('[{0}] 폴더 생성완료'.format(music))
            shutil.move(path,musicPath+'\\'+title)

        def searchMusic(originalpath,musics,title):   #음악파일 찾기
            for (path, dir, files) in os.walk(originalpath):
                for filename in files:
                    ext = os.path.splitext(filename)[-1]    #파일 확장자 확인
                    if ext == '.mp3' or '.flac' or '.aif':     #flac, mp3파일만 리스트에 추가
                        musics.append(path+'\\'+filename)
                        title.append(filename)

        originalpath = InPath

        if not os.path.exists(OutPath+'\\music'):           #폴더가 없으면 생성
                os.mkdir(OutPath+'\\music')

        musics = []   #음악 리스트
        title = []  #음악 제목

        searchMusic(originalpath,musics,title)

        for i in range(len(musics)):
            ext = os.path.splitext(musics[i])[-1]
            try:    #메타데이터 아티스트가져오기
                if ext == '.flac':
                    music = mutagen.File(musics[i])[metadata][0]
                elif ext == '.mp3' or '.aif':
                    if metadata == 'ARTIST':
                        music = mutagen.File(musics[i])["TPE1"][0]
                    elif metadata == 'ALBUM':
                        music = mutagen.File(musics[i])["TALB"][0]
                    elif metadata == 'DATE':
                        music = mutagen.File(musics[i])["TDRC"][0]
                music = re.sub(r"\/|\:|\<|\>|\\|\*|\?|\"|\||","", music)        #디렉토리 생성 규칙 준수
            except: #메타데이터 없으면 Unknown
                print('알수없는 메타데이터입니다. Unknown')
                if metadata == "ARTIST":
                    music = 'Unknown Artist'
                elif metadata == "ALBUM":
                    music = 'Unknown Album'
                elif metadata == "DATE":
                    music = 'Unknown Date'
                    
            DirectoryManager(musics[i],music,title[i],OutPath)
    except:
        print('에러발생')