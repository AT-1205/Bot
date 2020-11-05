import telebot
from telebot import types

bot = telebot.TeleBot("1248875561:AAHJtgjHyRdXF4z9ABfiQLfLOue_OYkHn-I")

name = ''


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello. What is your name?")
    bot.register_next_step_handler(message, reg_name)


@bot.message_handler(func=lambda m: True)
def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Nice to meet you  " + name)
    bot.send_message(message.from_user.id, '''I am English Study Bot.
I hope to help you with your English.''')
    bot.send_message(message.from_user.id, '''There are many ways to improve you English.
It is depends on what skill you want to increase:
Vocabulary - learn more words and phrases.
Speaking - practice your pronunciation and the way you express yourself.
Grammar - study a way we arrange words to make proper sentences,
grammar rules and time tenses.''')
    bot.send_message(message.from_user.id, '''If you ready to start,
please type 'Start'.''')
    bot.register_next_step_handler(message, skill)


@bot.message_handler(func=lambda m: True)
def skill(message):
    if message.text == 'Start' or 'Back':
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Vocabulary', callback_data='B')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Speaking', callback_data='T')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Grammar', callback_data='C')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text='Not sure', callback_data='H')
        keyboard.add(key4)
        s = 'Please choose what skill you want to improve'
        bot.send_message(message.from_user.id, text=s, reply_markup=keyboard)
    elif message.text == 'TOEFL':
        bot.send_message(message.from_user.id, '''TOEFL - The world's premier English-language test
for university study, work and immigration.
You can find more and register to the test in: https://www.ets.org/toefl''')
        bot.send_message(message.from_user.id, '''If you want to go back
please type: 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'IELTS':
        bot.send_message(message.from_user.id, '''IELTS is the high-stakes English test for study, migration or work
Find out more about IELTS in: https://www.ielts.org/
You can register for the test in Bishkek here:
https://ielts.kg/''')
        bot.send_message(message.from_user.id, '''If you want to go back
please type: 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Read':
        bot.send_message(message.from_user.id, '''This is the list of Literature, for English practise and
self-development:
1. The Adventures of Tom Sawyer by Mark Twain (1876)
2. Little women by Louisa May Alcott (1868-1869)
3. A Journey to the Centre of the Earth by Jules Verne (1871)
4. The Automobile Girls At Washington by Laura Dent Crane (1913)
5. A Ghost of a Chance by Cherie Claire (2017)
6. The Man in the Brown Suit by Agatha Christie (1924)
7. Around the World in 80 Days by Jules Verne (1873)
You can find all of them and more there: https://manybooks.net/''')
        bot.send_message(message.from_user.id, '''If you want to go back
please type: 'Back'.''')
        bot.register_next_step_handler(message, skill)
    else:
        bot.send_message(message.from_user.id, '''Unknown command,
please try again''')
        bot.register_next_step_handler(message, skill)


@bot.callback_query_handler(func=lambda m: True)
def callback(call):
    if call.data == 'B':
        bot.send_message(call.message.chat.id, 'Very well, ' + name + '''. The best and most
interesting way to improve your vocabulary skills is by watching
films and reading books''')
        bot.send_message(call.message.chat.id, '''If you don't know where you can find them, please write:
TV - to see list of the recommended resources where
you watch free movies and TV-shows
Books - to see list of the recommended resources where
you can read books on English.''')
        bot.register_next_step_handler(call.message, sources)
    elif call.data == 'T':
        bot.send_message(call.message.chat.id, "Ok, " + name + '''. If you want to speak English well,
you must practice with other people.
Also ypu can find a native speaker from social media or app tandem
and chat or call them from skype and zoom.
https://www.tandem.net/ru''')
        bot.send_message(call.message.chat.id, '''You can visit talking clubs in your City.
Type 'Talking clubs' to see the list of the good talking clubs in Bishkek.''')
        bot.register_next_step_handler(call.message, sources)
    elif call.data == 'C':
        bot.send_message(call.message.chat.id, '''Grammar - is very important, especially
if you are going to take some tests, like TOEFL and IELTS.''')
        bot.send_message(call.message.chat.id, '''The best way to study grammar and prepare
for test like this, is going to courses and studying with someone,
who has an experience in in this''')
        bot.send_message(call.message.chat.id, '''Please write:
Courses - to see list of the best courses in Bishkek;
Online courses - to see list of the websites where you can study online;
Textbook - to see the list of the books for grammar study.''')
        bot.register_next_step_handler(call.message, sources)
    elif call.data == 'H':
        bot.send_message(call.message.chat.id, "It is ok, " + name + '''. If you confused or not sure
what you need learn, you can write 'Help'.''')
        bot.register_next_step_handler(call.message, help1)


@bot.message_handler(func=lambda m: True)
def sources(message):
    if message.text == 'TV':
        bot.send_message(message.from_user.id, '''These are websites where you can watch Movies, TVshows:
1. https://www.netflix.com/kg/
2. https://www.filmdoo.com/
3. https://tinyzonetv.to/
4. https://www.linkedfilm.com/
5. https://www.freemoviescinema.com/''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu,
please write 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Books':
        bot.send_message(message.from_user.id, '''These are websites where you can read books in English:
1. https://english-e-reader.net/
2. https://madbook.org/books
3. https://manybooks.net/
4. https://www.bookrix.com/books.html''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu, please write 'Back'.
If you want to see a list of recommended literature type 'Read'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Talking clubs':
        bot.send_message(message.from_user.id, '''These are talking clubs in Bishkek I recommend you to visit:
1. English Zone, 42/1 Isanov St.
2. American Information Resource center, Bayalinov library, 242 Ogonbaev St.
3. Speaking club in American school, 134 Ahunbaev St.
4. Oxford International school, 9.11 T.Okeeva St.''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu,
please write 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Courses':
        bot.send_message(message.from_user.id, '''These are English schools in Bishkek that i recommend you to visit:
1. Logos school, 109/1 Turusbekov St.
2. American school, 52 Toktogul St.
3. Lingua school, 204 Sovetskaya St.
4. WOE language courses, 197/1 Tynystanov St.
5. IELTS, 173/4 Yunusaliev St.''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu,
please write 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == "Online courses":
        bot.send_message(message.from_user.id, '''If you don't have time or chance to go to courses,
these are online courses for you:
1. https://perfectlyspoken.com/ - free courses for begginers.
2. https://learnenglish.britishcouncil.org/ - Self-access English courses for
professionals who want to take their career to the next level.
3. https://www.coursera.org/ - professional courses with native speakers
and certificates.
4. https://www.futurelearn.com/ - online English courses designed to improve
your English speaking and writing skills.''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu,
please write 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Textbook':
        bot.send_message(message.from_user.id, '''This is the list of books for English language study:
1. Oxford business result books - is a six-level business English course
that gives students the communication skills they need for immediate use
at work.
2. Cambridge Academic English books - there are books from A1 to C2 levels.
3. English Grammar in Use: A Self-Study Reference and Practice Book for
Intermediate Students of English - with Answers.
4. Focus - five-level English course book.
5. High-Level Everyday English - book for Advanced and + level students
for everyday practice.''')
        bot.send_message(message.from_user.id, '''If you want to go back to the menu,
please write 'Back'.''')
        bot.register_next_step_handler(message, skill)
    else:
        bot.send_message(message.from_user.id, '''Unknown command, please try
again.''')
        bot.register_next_step_handler(message, sources)


@bot.message_handler(func=lambda m: True)
def help1(message):
    if message.text == 'Help':
        bot.send_message(message.from_user.id, '''First, I need to know your English level.
Please type your level:
A1 - If you are Begginer
A2 - If you have Elementary level
B1 - If you have Intermediate level
B2 - If you have Upper Intermediate level
C1 - If you have Advanced level
C2 - If you have Mastery level
Or type: 'Find out', if you don't know your level.''')
        bot.register_next_step_handler(message, level)


@bot.message_handler(func=lambda m: True)
def level(message):
    if message.text == 'A1' or message.text == 'A2':
        bot.send_message(message.from_user.id, 'Ok, ' + name + '''.I see you need more
practice.''')
        bot.send_message(message.from_user.id, '''There are many ways to improve your English.
        But since you only started. These are some sources for begginers:
        https://lingualeo.com/ru
        https://perfectlyspoken.com/
        https://puzzle-english.com/
        https://www.esolcourses.com/''')
        bot.send_message(message.from_user.id, '''If you want to go back please
type: 'Back'.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'B1' or message.text == 'B2':
        bot.send_message(message.from_user.id, "Very well, " + name + '''. But you
can do better.''')
        bot.send_message(message.from_user.id, '''If you already know basics, you should focus on
speaking and expressing yourself.
So I would recommend you to start watching movies and reading book in English.
Or you can also improve your grammar skills.
It is depends on your goals. If you are going to take tests like IELTS
and TOEFl you need to work on all of the skills.
Please type:
Back - if you want to go back and choose one of the skills, where you
can find sources for books, movies and grammar.
TOEFl - if you want to know more about it.
IELTS - if you want to know more about it.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'C1' or message.text == 'C2':
        bot.send_message(message.from_user.id, "Wonderful, " + name + '''! I see you are already
a professional.''')
        bot.send_message(message.from_user.id, '''If you are confident in your English, you should
try yourself in official language tests, like TOEFL or IELTS.
Or if you not sure, you can practise a bit more.
Also i recommend you to practise everyday, because you can forget things easily
without repeating them.
Since you have a high level in English, I advice you to read books in English.
Please type:
Read - to see the list of Literature in English for you.
Back - to go back to menu.
TOEFL - if you want to know more about it.
IELTS - if you want to know more about it.''')
        bot.register_next_step_handler(message, skill)
    elif message.text == 'Find out':
        bot.send_message(message.from_user.id, '''You can learn about find out more about language level
and pass your test here: https://www.cambridgeenglish.org/''')
        bot.send_message(message.from_user.id, '''If you want to go back
please type: 'Back'.''')
        bot.register_next_step_handler(message, skill)
    else:
        bot.send_message(message.from_user.id, '''Unknown command,
please try again''')
        bot.register_next_step_handler(message, level)


bot.polling()

