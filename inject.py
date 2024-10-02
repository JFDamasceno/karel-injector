import argparse
from ftplib import FTP
import subprocess
import webbrowser
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that compiles and injects Karel files into a controller"
    )
    parser.add_argument("-i","--ip", required=True , help='Robot ip address')
    parser.add_argument("-f","--file", required=True, help="file name to inject without the extension")
    parser.add_argument("-t","--test",action='store_true', help="enable if injecting a unit test")
    args = parser.parse_args()

    robotip = args.ip
    karelfile = args.file
    compiled = karelfile.lower() + '.pc'
    
    if os.path.exists(compiled):
        os.remove(compiled)

    subprocess.run(['ktrans',karelfile + '.kl'],timeout=20,capture_output=True,text=True)

    if not os.path.exists(compiled):
        raise TypeError('Ktrans did not compile successfully')

    with FTP(robotip) as ftp:
        ftp.login()
        file = open(compiled,'rb')
        ftp.storbinary('STOR '+ compiled,file)
        file.close()
        ftp.quit()
        
    if args.test:
        url= 'http://' + robotip + ':9001/KAREL/kunit?filenames=' + karelfile
        webbrowser.open_new_tab(url)