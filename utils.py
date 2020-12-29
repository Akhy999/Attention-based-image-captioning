#!/usr/bin/env python
# coding: utf-8

# In[144]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.preprocessing.image import load_img
from collections import Counter


# In[1]:


def load_document(document_name):
    document = open(document_name, 'r')
    buffer = document.read()
    document.close()
    return buffer


# In[12]:





# In[22]:


def make_dataframe(buffer):
    df = []
    for line in buffer.split('\n'):
        line_split = line.split('\t')
        if len(line_split) == 1:
#            print(line_split)
            continue
        head = line_split[0].split('#')
        df.append(head + [line_split[1].lower()])
    return df


# In[75]:





# In[76]:





# In[77]:





# In[78]:


def add_tags(df):
    df.caption = df.caption.apply(lambda x: '<go> ' + str(x) + ' <end>'  )
#     for caption in df.caption:
#         caption = '<go>' + str(caption) + '<end>'
    return


# In[79]:





# In[116]:


def data_plot(df):
    target_size = (256,256,3)
    count = 1
    fig = plt.figure(figsize=(10,12))
    img_baseaddress = ""
    
    for i in df.file_name.unique()[100:103]:
        file_name = img_baseaddress + i
        captions = list(df.caption.loc[df.file_name == i].values)
        img = load_img(file_name,target_size=target_size)

        ax = fig.add_subplot(3,2,count,xticks = [],yticks = [])
        ax.imshow(img)
        count += 1

        ax = fig.add_subplot(3,2,count)
        plt.axis('off')
        ax.plot()
        ax.set_xlim(0,1)
        ax.set_ylim(0,len(captions))
        for i,caption in enumerate(captions):
            ax.text(0,i,caption,fontsize = 20)
        count += 1
    plt.show()
#     print(file_name)
#     image = load_img("./flicker 8k/Flickr8k_Dataset/Flicker8k_Dataset/" + file_name,target_size)
#     plt.subplot(1,2,2).imshow(image)
#     plt.subplot(1,2,1).text(df['caption'].loc[df.file_name==file_name].values)


# In[117]:





# In[138]:


def word_count(df):
    complete_string = ''
    for i in df.caption:
        complete_string = complete_string+' '+i
    vocabulary = complete_string.split(' ')
    ct = Counter(vocabulary)
    appen_1 = []
    appen_2 = []
    for i in ct.keys():
        appen_1.append(i)
    for j in ct.values():
        appen_2.append(j)
    data = {"word" : appen_1, "count" : appen_2}
    dfword = pd.DataFrame(data)
    dfword = dfword.sort_values(by = 'count', ascending=False)
    dfword = dfword.reset_index()[["word","count"]]
    return dfword


# In[141]:





# In[146]:


def tokenize_caption(top_k, train_captions):
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=top_k,oov_token="<unk>",filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')
    tokenizer.fit_on_texts(train_captions)
    train_seqs = tokenizer.texts_to_sequences(train_captions)

    tokenizer.word_index['<pad>'] = 0
    tokenizer.index_word[0] = '<pad>'

    # Create the tokenized vectors
    train_seqs = tokenizer.texts_to_sequences(train_captions)
    return train_seqs, tokenizer 


# In[147]:






# In[150]:


# In[154]:





# In[157]:


# maxi = 0
# for i in df.caption:
#     if len(i.split(' ')) > maxi:
#         maxi = len(i.split(' '))
#         cap = i
# print(cap)


# In[158]:


def padd_train_seq(train_seqs, max_length):
    cap_vector = tf.keras.preprocessing.sequence.pad_sequences(train_seqs, padding='post',maxlen=max_length)
    return cap_vector

def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, (224, 224))
    img = tf.keras.applications.vgg16.preprocess_input(img)
    return img, image_path

def map_func(img_name, cap):
    img_tensor = np.load(img_name.decode('utf-8')+'.npy')
    return img_tensor, cap