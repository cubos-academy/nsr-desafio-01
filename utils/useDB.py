import sqlite3, os

PATH = str(os.path.dirname(__file__))


class Sqlite:
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect(PATH + '/apod.db')
        self.cur = self.conn.cursor()
        self._create_table()
        
    
    def _create_table(self) -> None:
        try:
            sql = """
            CREATE TABLE IF NOT EXISTS subscribers (
                id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                chat_id     VARCHAR(20) NOT NULL UNIQUE
            )
            """
            
            self.cur.execute(sql)
            self.conn.commit()
            
        except TypeError:
            print('Erro ao criar tabela')
        
    
    def insert_sub(self, chat_id: str) -> None:
        
        try:
            sql = f'''
                INSERT INTO subscribers (chat_id)
                VALUES (?)
            '''
            self.cur.execute(sql, (chat_id,))
            self.conn.commit()
            
            self._close_db()
            
        except TypeError:
            print(TypeError)
            
    
    def read_subs(self) -> list:
        sql = f'''
            SELECT chat_id FROM subscribers
        '''
        self.cur.execute(sql)
        
        return [linha for linha in self.cur.fetchall()]
    
    
    def _close_db(self) -> None:
        self.conn.close()
        