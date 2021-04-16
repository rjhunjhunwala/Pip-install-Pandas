<h2>pip install pandas</h2>


Pandas is a leading library in the field of data science, when you utter the magic words:
    <pre>
        pip install pandas
</pre>

You get a powerful library to explore, analyze, and transform massive data sets using expressive syntax.
<br/><br/><br/>
You even get chills as you type the commands into your terminal:

<pre>
    <figcaption>Magical application</figcaption>
    <pre><code contenteditable="false" tabindex="0" spellcheck="false">python my_magic_app.py
    </pre>

Your app runs, it does the big data, but still... somethings missing... you can't put your finger on it....
<br/><br/><br/>
You are missing ACTUAL pandas!! Wouldn't it be great if these magic spells also summon the animals whose name you invoke?

Introducing: pipinstallpandas.py! Whenever you invoke the name (or even mention it in any context of an animal to do your magical programming work, this script
will also show you some pictures of the cuties to help you properly express your gratitude some example commands to try in your terminal. Typing other words will show you a surprise.

<pre>
python pipinstallpandas.py # start the logger
conda install tensorflow
pip install pandas
python my_amazing_app.py >> output_log.txt
cat output_log.txt
</pre>

Without further ado: here is the script:

    <pre>
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


def open_then_close(url, time_to_sleep = 3):
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
                "conda": lambda : get_random_picture_of("cartoonish plush snake")
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
   </pre>


<a href = "../pipinstallpandas.py">Download</a> the script here.
<a href = "https://codepen.io/daemondevin/pen/pNqpQE">Code Pen for how to include source</a>
