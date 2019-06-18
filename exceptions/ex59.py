import sys
import os
import random
import traceback


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]    ## Python way of copying a list
        
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results



if __name__ == "__main__":
    WORD_FILE_NAME = "words.txt"
    WORDS = []
    PHRASES = {
        "class %%%(%%%):"                               : "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)"      : "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()"                                   : "Set *** to an instance of class %%%.",
        "***.***(@@@)"                                  : "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'"                               : "From *** get the *** attribute and set it to '***'."
    }

    # do they want to drill phrases first
    PHRASE_FIRST = False
    if len(sys.argv) == 2 and sys.argv[1] == "english":
        PHRASE_FIRST = True

    # load up the words from the website
    word_file_path = os.path.dirname(__file__) + os.sep + WORD_FILE_NAME
    word_file = open(word_file_path)
    for word in word_file.readlines():
        WORDS.append(word.strip())

    # keep going until they hit CTRL- D
    try:
        while True:
            snippets = [*PHRASES.keys()]
            random.shuffle(snippets)
            for snippet in snippets:
                phrase = PHRASES[snippet]
                question, answer = convert(snippet, phrase)
                if PHRASE_FIRST:
                    question, answer = answer, question
        
                    print(question)
                    
                    input("> ")
                    
                    print("ANSWER: {}\n\n".format(answer))
    except KeyboardInterrupt:
        traceback.print_exc()
        print("\nBye")
    except EOFError:
        print("\nBye")
    