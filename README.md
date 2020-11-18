# Speech-Recognition-with-python-and-Goolgle-cloud-api
Speech Recognition From Bengali to English

# Speech Recognition 
Speech recognition is an interdisciplinary subfield of software engineering and computational semantics that develops methodologies and technologies that enable the recognition and translation of spoken language into text by computers. It is also known as automatic speech recognition (ASR), computer speech recognition, or speech to text (STT).[1]

# Download Data

We use asr_bengali audio dataset for testing our audio. link:
https://bengali.ai/datasets/

 # In speech_rec_1.py we use two function

 # Functions:

In function get_file_path we use os.walk to get the path of the audio file from our directory.Then append all audio file individually in a file_paths list.
In process file, function we use speech recognizer class of python to recognize audio and write it into text format.
In the main function we take the list of all audio from file_paths list. Then call the process_file function with each audio. process_file function returns us a string.
Then we write the string in output file.   
  
# Accuracy Check

In this we check the accuracy with Sequencemeter. We use read() method to take all string line by line and character by character. 
 
 # class difflib.SequenceMatcher

This is a flexible class for comparing pairs of sequences of any type, so long as the sequence elements are hashable. The basic algorithm predates, and is a little fancier than,  an algorithm published in the late 1980’s by Ratcliff and Obershelp under the hyperbolic name “gestalt pattern matching.” The idea is to find the longest contiguous matching   subsequence that contains no “junk” elements (the Ratcliff and Obershelp algorithm doesn’t address junk). The same idea is then applied recursively to the pieces of the sequences to the left and to the right of the matching subsequence. This does not yield minimal edit sequences, but does tend to yield matches that “look right” to people.[2]

# real_quick_ratio() 

Return an upper bound on ratio() very quickly. The three methods that return the ratio of matching to total characters can give different results due to differing levels of approximation, although quick_ratio() and real_quick_ratio() are always at least as large as ratio() [2] 

# Reference: 
1. https://en.wikipedia.org/wiki/Speech_recognition
2. https://docs.python.org/2/library/difflib.html

# Another account:
Link: https://github.com/Ibtesum-Sakibmd
