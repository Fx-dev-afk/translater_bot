import pymysql

TOKEN = '5359023166:AAEIiGztL2jSgCqAGTcYKt35cko4HneeMLI'
STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /choose"
CHOSEMSG = "Choose lang"
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'ru': 'English',
    'en': 'Russian'
}

mydb = pymysql.connect(
    host="",
    user="",
    passwd="F",
    database=""
)
