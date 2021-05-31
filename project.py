import time 
import difflib
import random


def main():
    quotes = ["Stop! You have violated the Law! Pay the court a fine or serve your sentence. Your stolen goods are now forfeit",
    "Hey you, you're finally awake. You were trying to cross the border? Walked right into that imperial ambush, like us and that thief over there.",
    "There is no greater sorrow than to recall happiness in times of misery.",
    "What can you do, thought Winston, against the lunatic who is more intelligent than yourself; who gives your arguments a fair hearing and simply persists in his lunacy?"]

    begin = str(input("Do you want to start? Yes/No "))

    while begin == "Yes":

        ind = random.randint(0,len(quotes)-1)

        print(quotes[ind])

        start = time.time()
        text = str(input("Please type the quote above: "))
        stop= time.time()

        count = stop - start
        words_p_m = "{:.2f}".format(wpm(text,count))
        acc = "{:.2f}".format(difflib.SequenceMatcher(None,quotes[ind],text).ratio()*100)


        print("Your words per minute were "+str(words_p_m))
        print("Your accuracy was "+str(acc))

        new_qt = input("Do you want to add a new quote? Yes/No ")

        if new_qt == "Yes":
            new = input("Type your quote: ")
            quotes.append(new)
        
        begin = str(input("Do you want to start again? Yes/No "))


def wpm(text,count):
    word_list = text.split()
    num_words = len(word_list)
    minutes = count/60
    return num_words/minutes

if __name__ == '__main__':
    main()