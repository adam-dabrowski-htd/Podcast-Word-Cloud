from transcriber import transcribe
import subprocess

file_output = 'podcast.flac'
url = 'https://content.production.cdn.art19.com/episodes/1869f87a-edca-4737-b3fe-cad55c90559f/bf53c9567ac7dd803490004ceb6c37681f369a079afe9354696d472fca8f977ce5640787f81a3650a40bc29eda89cb846f8ae5a7d76db605ae3208166fac2088/TheTimFerrissShow_Patrick%20Collison.mp3#t=420'

def create_file(url, file_output):
    output = subprocess.check_output(['./converter.sh',str(url),str(file_output)])

def transcription_to_str():
    transcription = transcribe(file_name=file_output)
    str = ''.join(transcription)
    return str

def get_word_count(str):
    import operator
    word_counts = dict()
    for word in str.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=operator.itemgetter(1))

    return sorted_words[:10]

if __name__ == "__main__":
    create_file(url=url, file_output=file_output)
    transcription = transcription_to_str()
    print (get_word_count(transcription))
