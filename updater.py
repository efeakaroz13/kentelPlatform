import os
os.system("scp *.py efeakaroz13@kentel.dev:/home/efeakaroz13/kentelPlatform")
os.system("scp -r templates/* efeakaroz13@kentel.dev:/home/efeakaroz13/kentelPlatform/templates")
os.system("scp -r static/* efeakaroz13@kentel.dev:/home/efeakaroz13/kentelPlatform/static")
wannaContinue=input("wanna upload to the server_2 as well? (y/n):")
if wannaContinue == "y":
    os.system("scp SERVER_2/*.py efeakaroz13@192.168.1.65:/home/efeakaroz13/kentelPlatform/SERVER_2/")
