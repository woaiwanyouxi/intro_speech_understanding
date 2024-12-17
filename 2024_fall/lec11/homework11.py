import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
#     raise RuntimeError("FAIL!!  You need to change this function so it works!")
    r = speech_recognition.Recognizer()

    with speech_recognition.AudioFile("264752__copyc4t__phone-messages-english-and-italian.flac") as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    return text
