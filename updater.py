import os
os.system("scp *.py efeakaroz13@45.155.124.85:/home/efeakaroz13/kentelPlatform")
os.system("scp -r templates/* efeakaroz13@45.155.124.85:/home/efeakaroz13/kentelPlatform/templates")
os.system("scp -r static/* efeakaroz13@45.155.124.85:/home/efeakaroz13/kentelPlatform/static")
os.system("scp -r other efeakaroz13@45.155.124.85:/home/efeakaroz13/kentelPlatform")
wannaContinue=input("wanna upload to the server_2 as well? (y/n):")
if wannaContinue == "y":
    os.system("scp SERVER_2/*.py efeakaroz13@192.168.1.65:/home/efeakaroz13/kentelPlatform/SERVER_2/")

#update
