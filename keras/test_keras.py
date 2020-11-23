'''

sentiment analysis or text mining

'''



# %% [markdown]
## the imports
#import tensorflow
import time
print('start... \n\n')

t_0 = time.time()

# this throws some GPU error messages
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
t_1 = time.time()

print('keras imports complete', '\n')
print('imports time', round(t_1 - t_0, 1), 'seconds', '\n\n')

# %% [markdown]

sentance = [
    'This is a standard sentance',
    'here is another sentance',
    'and this is a very very very long sentance'
    ]

# keras model
model = Tokenizer(num_words=100, oov_token='one_time_use')

model.fit_on_texts(sentance)

words = model.word_index
print(words, '\n')

sequence = model.texts_to_sequences(sentance)

test_text = [
    'This is a youtube channel',
    'here are some things to do and this was mentioned alot'
    ]
sequence_2 = model.texts_to_sequences(test_text)

print(sequence_2, '\n')

padding = pad_sequences(sequence, padding='post', maxlen=8, truncating='post')

print(padding)


