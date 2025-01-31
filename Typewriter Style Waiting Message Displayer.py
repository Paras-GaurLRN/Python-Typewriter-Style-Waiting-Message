def ArtDisplay(wdnlst):
    from os import system , name as OSname
    from time import sleep
    from art import text2art as t2a
    from colorama import Fore as _F, Back as _B , Style as _S , init as clrreset
    for wd in wdnlst:
        try:
            wl = wd.split(' ')
            count=1
            for w in wl:
                try:
                    w_art = t2a(w,font='dot matrix',sep='\n')
                    wl_art = []
                    for _ in range(len(w_art.split('\n'))):
                        wl_art += w_art.partition('\n')[0] + w_art.partition('\n')[1]
                        nmbr = len(w_art.partition('\n')[0]) + len(w_art.partition('\n')[1])
                        w_art = w_art[nmbr:]
                    clrreset(autoreset=True)
                    for x in wl_art: # Your Desired Colour Scheme Here
                        if count==1:
                            print(_F.RED + _B.BLACK + _S.BRIGHT + x, end='')
                            sleep(0.00625)
                        elif count==2:
                            print(_F.BLUE + _B.BLACK + _S.BRIGHT + x, end='')
                            sleep(0.00625)
                        elif count==3:
                            print(_F.GREEN + _B.BLACK + _S.BRIGHT + x, end='')
                            sleep(0.00625)
                        elif count==4:
                            print(_F.MAGENTA + _B.BLACK + _S.BRIGHT + x, end='')
                            sleep(0.00625)
                except Exception:
                    raise Exception('An Unknown Error Has Occured! Exiting Program...')
                    exit()
                finally:
                    count+=1
        except Exception:
            raise Exception('An Unknown Error Has Occured! Exiting Program...')
            exit()
        finally:
            if OSname == 'posix':
                system('clear')
            else:
                system('cls')

while True:
    nlist = ['System Sleeping zzz... Bye']
    ArtDisplay(nlist)
