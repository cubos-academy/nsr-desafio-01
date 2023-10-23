import schedule
from apis.telegram_bot import run_bot
from utils.db_queue import get_chat_id
from utils.useDB import Sqlite
from apis.telegram_bot import  send_daily_photo

db = Sqlite()

def send_for_subscribers():
    subs = db.read_subs()
    
    for sub in subs:
        send_daily_photo(sub)
        

def scheduler():
    schedule.every().day.at("08:00").do(
        send_for_subscribers()
    )    


if __name__ == '__main__':
    run_bot() 
    scheduler()