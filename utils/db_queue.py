import queue

chat_id_queue = queue.Queue()

def add_chat_id(chat_id):
    chat_id_queue.put(chat_id)

def get_chat_id():
    try:
        return chat_id_queue.get(timeout=1)
    except queue.Empty:
        return None