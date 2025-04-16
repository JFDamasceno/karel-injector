import argparse
from ftplib import FTP
import subprocess
import webbrowser
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that compiles and injects Karel files into a controller"
    )
    parser.add_argument("file", help="Base name of the Karel file (without extension)")
    parser.add_argument("-i", "--ip",default="127.0.0.1", help="Robot IP address")
    parser.add_argument("-t", "--test", action="store_true", help="Enable unit test execution after injection")
    args = parser.parse_args()

    robotip = args.ip
    karelfile = args.file
    compiled = karelfile.lower() + ".pc"

    if os.path.exists(compiled):
        os.remove(compiled)

    result = subprocess.run(["ktrans", karelfile + ".kl"], timeout=20, capture_output=True, text=True)

    if not os.path.exists(compiled):
        print("Compilation failed:")
        print(result.stdout)
        print(result.stderr)
        raise TypeError("Ktrans did not compile successfully")

    with FTP(robotip) as ftp:
        ftp.login()
        with open(compiled, "rb") as file:
            ftp.storbinary("STOR " + compiled, file)
        ftp.quit()

    if args.test:
        url = f"http://{robotip}:9001/KAREL/kunit?filenames={karelfile}"
        webbrowser.open_new_tab(url)
