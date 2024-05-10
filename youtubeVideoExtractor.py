from pytube import YouTube
from deepgram import Deepgram, DeepgramClient, FileSource, PrerecordedOptions
import requests
import json


def text_to_speech(text):
    CHUNK_SIZE = 1024         
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"       
    headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "85f3656363820e0d71070a7bbebac0f6"
  }
    data = {
  "text": text,
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
 }
    response = requests.post(url, json=data, headers=headers)
    
    with open('newVoice.wav', 'wb') as f:
     for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk) 
    print("progress:100%,","Text is Changed to new Voice and saved to content/newVoiceAudio.wav")       
            



def audioToText(PATH_TO_FILE):
    DEEPGRAM_API_KEY = "c1bd57e7cb1579f4a561ba8e684f385a7e81d3e9"
   
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, "rb") as file:
        buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }  

        options = PrerecordedOptions(
            smart_format=True,
            summarize="v2",
        )  

        file_response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        jsonData = file_response.to_json()
        # print(f"{json}")
        parsedData= json.loads(jsonData)
        with open('audioToJsonText.json', 'w') as json_file:
         json.dump(parsedData, json_file)
         print("progress:60%,","Json is saved in content/audioToJsonText.json") 
      
        text = parsedData['results']['channels'][0]['alternatives'][0]['transcript']
        text_to_speech(text)    
        with open("audioToText.txt", 'w') as file:
          file.write(text)
          print("progress:80%,","text is saved in content/audioToText.txt")
        
     






def Url_to_video(url, video_output_path="video.mp4",audio_output_path="audio.wav"):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    audio_stream=yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    video_stream.download(filename=video_output_path)
    print("progress:20%,","Video is saved in content/video.mp4")
    
    audio_stream.download(filename=audio_output_path)
    print("progress:40%,","Audio is saved in content/audio.wav")

          
  

Url_to_video("https://youtu.be/jljcEmaHryA?si=1a8lVMrepgn1enYK")
audioToText("audio.wav") 

         
     
         
         
  
  





 
            
            
            
            





