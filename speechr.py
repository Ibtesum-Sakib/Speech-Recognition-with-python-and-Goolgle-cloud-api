#importing library for speech_recognition
import speech_recognition as sr
import csv
import os

#Go To File Directory
DIRNAME = r'D:\asr_bengali\data\000'#audio file directory
OUTPUTFILE = r'D:\asr_bengali\data\main1.txt'#output file directory in a txt file

#Retrieving the file path
def get_file_paths(dirname):
    file_paths = []
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

#processing the audio file
def process_file(file):
    r = sr.Recognizer() #Creating a recognizer instance
    a = ''
    with sr.AudioFile(file) as source:          #taking the file as a source
        r.adjust_for_ambient_noise(source)      #noise cancelation from source
        audio = r.record(source)                #record the source audio
        try:
            a =r.recognize_google(audio,language='bn')  #for recognizing google and set the language to bengali
        except sr.UnknownValueError:
            a = "Google Speech Recognition could not understand audio" #if recogninition cannot work
        except sr.RequestError as e:
            a = "Could not request results from Google Speech Recognition service; {0}".format(e) #if the server did not ready
    return a

#main file to recognize the speech
def main():
    files = get_file_paths(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
    for file in files:                              # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        file_name = os.path.basename(file)          # get the basename for writing to output file
        if ext == '.flac':                           # only interested if extension is '.flac'
            a = process_file(file)                  # result is returned to a
            with open(OUTPUTFILE, 'a',encoding='utf-8') as f:        # write results to file
                writer = csv.writer(f) # writer.writerow(['file_name','google'])
                writer.writerow([file_name, a])
        elif ext =='.wav':                                  # only interested if extension is '.wav'
            a = process_file(file)  # result is returned to a
            with open(OUTPUTFILE, 'a', encoding='utf-8') as f:  # write results to file
                writer = csv.writer(f)  # writer.writerow(['file_name','google'])
                writer.writerow([file_name, a])
    print("Hello ASR!!! Please check your text folder")
if __name__ == '__main__':
    main()