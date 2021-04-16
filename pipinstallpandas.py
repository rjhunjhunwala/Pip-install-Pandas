from pynput.keyboard import Key, Listener
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mutable_st = []


from subprocess import Popen, check_call

def check(mutable_st, key):
    l = len(key)
    return len(mutable_st) >= l and all(mutable_st[i - l] == key[i] for i in range(len(key)))


def open_then_close(url, time_to_sleep = 7):
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(time_to_sleep)

    browser.close()

def on_press(key):
    try:
        mutable_st.append(eval(str(key)))
        print(mutable_st[-1])
    except:
        pass
    do_nothing_function = lambda : None

    def get_random_picture_of(thing):
        adjectives = ["cute", "cuddly", "floofy", "soft",
                      "adorable", "big", "aww", "safe",
                      "happy", "sad", "tame"]
        random.shuffle(adjectives)
        adjectives_to_use = []
        for adjective in adjectives:
            if random.random() < .5:
                adjectives_to_use.append(adjective)
        query_words = adjectives_to_use + [thing]
        query = "+".join(query_words)
        open_then_close("https://www.google.com/search?q={}&source="
                        "lnms&tbm=isch&sa=X&ved=2ahUKEwjFhauqu4HwAhW"
                        "VElkFHcX7CPgQ_AUoAXoECAEQAw&biw=1745&bih=881".format(query))

    quit = lambda : exit(0)
    keywords = {"python": lambda : get_random_picture_of("pythons"),
                "conda": lambda : get_random_picture_of("cartoonish plush snake"),
                "pandas": lambda : get_random_picture_of("pandas"),
                "floof": lambda : get_random_picture_of("floofers"),
                "dog": lambda : get_random_picture_of("dog"),
                "cat": lambda : get_random_picture_of("cat"),
                "fuck": lambda : get_random_picture_of("great alaskan malamute"),
                "shit": lambda : get_random_picture_of("giant flemish rabbit"),
                "sad": lambda : get_random_picture_of("hug"),
                "leavelogger": quit}

    for key, function in keywords.items():
        if check(mutable_st, key):
            function()

with Listener(on_press=on_press) as listener:
    listener.join()