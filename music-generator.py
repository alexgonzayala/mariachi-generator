import music21
import numpy
import pandas
import tensorflow as tf
import sklearn as sk
import matplotlib.pyplot as plt


# i want to design a music generator. i want it to generate music by the end!
# Steps to take to make this happen:
# 1. Gather a large dataset of music files! (midi would be best maybe) 
## Finished with this step.
# 2. Preprocess music files into a format suitable for training a model using music21.
## This involves turning the music files into a format that can be fed into a neural network
## What format should that be? Piano rolls seem like they've worked before.
## This depends on the music files I gather though. For piano music, piano rolls seem to be a good fit
## But, for music with more instruments, something similar to piano rolls but with more channels might be better.

# 3. Design several neural network architectures to experiment with.
## Some ideas for this:
## I want to start off with something I know, so I will start with a simple feedforward network and see what I get.
## Then, I want to learn more about RNNs and LSTMs, so I will look to implement those.
## Additionally, maybe CNNs could be used? They're good at pattern recognition, and I'd like to 
## include them in my analysis.
## Finally, transformers are all the rage right now, so I will look to make one as well.