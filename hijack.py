import sys
import io
import time
import youtube_dl
import pychromecast
from pychromecast.controllers.youtube import YouTubeController
from contextlib import redirect_stdout

video_id = "dQw4w9WgXcQ" # Last part of YouTube music video URL

# Prints list of Google Cast devices available to hijack on the network (name, model, UUID)
def print_device_details(devices):
    for i in range(0, len(devices)):
        print("\nDevice " + str(i+1) + ": \"" + devices[i].device.friendly_name +"\"")
        print("\t" + devices[i].device.model_name + " (UUID: " + str(devices[i].device.uuid) + ")")

# Prints message confirming device has been hijacked
def success(device):
    print("\nSuccess! " + device.device.friendly_name + " is playing Never Gonna Give You Up by Rick Astley.")

# Prints message stating device could not be hijacked
def error(device):
    print("\nSorry... " + device.device.friendly_name + " was not able to be hijacked.")

# Checks if hijacking was successful and calls success or error function
def verify_hijacking(device, content):
    time.sleep(1) # Give the device a chance to get content and play before checking status

    if device.media_controller.status.content_id == content:
        success(device)
    else:
        error(device)

# Generates URL to audio of YouTube video on the fly
def generate_audio_url():
    video_url = "http://www.youtube.com/watch?v=" + video_id
    ydl = youtube_dl.YoutubeDL({'format':'bestaudio/best', 'quiet':True})
    with redirect_stdout(io.StringIO()):
        with ydl:
            result = ydl.extract_info(video_url,download=False)
    url = result.get('url')
    
    return url

# Hijacks the specified device by playing audio of Never Gonna Give You Up by Rick Astley
def rick_roll_audio(device):
    audio_url = generate_audio_url()
    controller = device.media_controller
    controller.play_media(audio_url, "audio/mp3")
    controller.block_until_active()

    verify_hijacking(device, audio_url)

# Hijacks the specified device by playing video of Never Gonna Give You Up by Rick Astley
def rick_roll_video(device):
    yt = YouTubeController()
    device.register_handler(yt)
    yt.play_video(video_id)

    verify_hijacking(device, video_id)

# Prompts for user input to orchestrate hijackings
def run_hijacker():
    print("One moment please...")
    devices = pychromecast.get_chromecasts()

    if len(devices) == 0:
        print("It looks like there aren't any Google Cast devices available to hijack on this network.")
        sys.exit()
    else:
        print("\nYou're in luck! There are " + str(len(devices)) + " Google Cast device(s) available to hijack on this network.")
        print_device_details(devices)
        targets = input("\nType the device numbers you would like to hijack, separated by spaces. Leave blank to hijack no devices, or type 'a' to hijack all devices.\n")

        if targets == "":
            print("No devices are being hijacked. See you next time.")
            sys.exit()
        elif targets.lower() == "a":
            target_nums = list(range(1, len(devices) + 1))
        else:
            target_nums = list(map(int, targets.split(" ")))

        if len(target_nums) > 0:
            for num in target_nums:
                device = devices[num-1]
                
                if "TV" in device.model_name:
                    rick_roll_video(device)
                else:
                    rick_roll_audio(device)   

run_hijacker()


