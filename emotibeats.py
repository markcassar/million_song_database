from stemming.porter2 import stem
import matplotlib.pyplot as plt
import pandas as pd

base_path = 'c:\\users\\amoosa\\desktop\\challenge\\'
sentiment_file = 'c:\\users\\amoosa\\desktop\\challenge\\AFINN-96.txt'

#English word sentiment file from http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
# read in text file and create dict
# words need to be stemmed because words from song lyrics are stemmed

sentiment_dict = {}
with open(sentiment_file, 'r') as f:
        for line in f:
            split_line = line.split()
            # ignore phrases
            if len(split_line) > 2:
                continue
            sentiment_dict[stem(split_line[0])] = int(split_line[1])

                        
# read in bag of words from musicxmatch lyric analysis data
f     = open(base_path + 'word_list.txt', 'r')
words  = list(f.read().split(','))
f.close()


# read in song data with bag of words counts for lyrics
# calculate sentiment score for each song
# store results in an array

#song_list = [] 

msd_track_id = []
mxm_track_id = []
sentiment_score = []
num_of_words_in_lyrics = []

with open(base_path+'mxm_data.txt') as f:
    for line in f:
        lines = list(line.split(','))
        del lines[-1]   # couldn't get rid of escape character '\n' so removed, come back to this
        
        if len(lines) >= 2:
            msd_tid = lines.pop(0)
            mxm_tid = lines.pop(0)
        
        song_dict = {}
        for item in lines:
            k,v = item.split(':')
            song_dict[int(k)] = int(v)
            
        num_words = len(song_dict)
        
        score = 0
        for key, freq in song_dict.iteritems():
            word_to_lookup = words[key - 1]
            if word_to_lookup in sentiment_dict.keys():
                score += freq*sentiment_dict[ words[ key - 1]]
            else:
                score += 0
        
        msd_track_id.append(msd_tid)
        mxm_track_id.append(mxm_tid)
        sentiment_score.append(score)
        num_of_words_in_lyrics.append(num_words)
        
all_songs_dict = {'msd_track_id': msd_track_id, 
                    'mxm_track_id':mxm_track_id,
                    'sentiment_score':sentiment_score,
                    'num_of_words_in_lyrics':num_of_words_in_lyrics}




