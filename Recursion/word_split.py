# will be given a string of words without spaces and a list containing strings (invidual words)
#checking both the string and list check whether what words from the list are present in the string.


def word_split(phrase,list_of_words,output):

    if output is None:
        output=[]

    for words in list_of_words:

        if phrase.startswith(words):

            output.append(words)

            return word_split(phrase[len(words):],list_of_words,output)

    return output




