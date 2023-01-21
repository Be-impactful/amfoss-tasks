import os
import telebot
import requests
import csv

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv("API_KEY")
bot_id = os.getenv("BOT_ID")

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\nSee /help to see the commands.')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    movie_name = message.text[7:]
    if movie_name:
        # TODO: 1.2 Get movie information from the API
        movie_details = requests.get("http://www.omdbapi.com/?apikey="+yourkey+"&t="+movie_name).json()
        title = movie_details['Title']
        year = movie_details['Year']
        rating = movie_details['imdbRating']
        
        # TODO: 1.3 Show the movie information in the chat window
        bot.reply_to(message, 
        "Title: "+ title + "\nYear of Release: "+ year + "\nIMDB Rating: " + rating)
        
        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open("Movie details.csv", 'a') as file:
            heading = ["Title", "Year of Release", "IMDB Rating"]
            f_writer = csv.writer(file, delimiter=',')
            if file.tell() == 0:
                f_writer.writerow(heading)
                f_writer.writerow([title, year, rating])
            else:
                f_writer.writerow([title, year, rating])
    else:
        bot.reply_to(message, 'I did not understand '+'\N{confused face}')

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    bot.send_document(message.chat.id, open("Movie details.csv"))


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
