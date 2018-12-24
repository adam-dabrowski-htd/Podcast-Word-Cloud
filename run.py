from transcriber import transcribe
import subprocess
import operator
import os

file_output = 'podcast.mp3'
url = 'https://content.production.cdn.art19.com/episodes/1869f87a-edca-4737-b3fe-cad55c90559f/bf53c9567ac7dd803490004ceb6c37681f369a079afe9354696d472fca8f977ce5640787f81a3650a40bc29eda89cb846f8ae5a7d76db605ae3208166fac2088/TheTimFerrissShow_Patrick%20Collison.mp3#t=420'
flac_folder = '/home/ethan/Desktop/Sandbox/podcast/files/flacs'
incr = 50

def create_file(url, file_output):
    output = subprocess.check_output(['./converter.sh', url, incr])

def transcription_to_str(file, time_slot):
    transcription = transcribe(file_name=file)
    d = {}
    d['time_slot'] = time_slot
    d['str'] = ''.join(transcription)
    return d

def get_word_count(str, time_slot):
    word_counts = dict()
    for word in str['str']:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=operator.itemgetter(1))
    d = {}
    d['time_slot'] = time_slot
    d['word_count'] = dict(sorted_words)

    return d

def write_to_file(input, output):
    f = open('{}.txt'.format(output), 'a')# just put 'w' if you want to write to the file
    f.write(str(input) + '\n')
    f.close()

if __name__ == "__main__":
    create_file(url=url, file_output=file_output)
    time_inter = 0
    for file in os.listdir(flac_folder):

        transcription = transcription_to_str('{}/{}'.format(flac_folder,file), time_inter)

        write_to_file(input=transcription, output="transcription_output")
        write_to_file(input=get_word_count(transcription, time_inter), output="words_output")
        time_inter += incr
