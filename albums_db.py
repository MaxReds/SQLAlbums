import sqlite3

class Album:
    def __init__(self, title, artist, release_year, genre):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre

class AlbumsDB:
    def __init__(self, db_name="albums.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            release_year INTEGER,
            genre TEXT
        );
        '''
        try:
            self.cursor.executescript(create_table_sql)
            self.connection.commit()
            print("Таблица 'albums' успешно создана или уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")

    def add_album(self, album):
        try:
            self.cursor.execute('''
                INSERT INTO albums (title, artist, release_year, genre) 
                VALUES (?, ?, ?, ?)
            ''', (album.title, album.artist, album.release_year, album.genre))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении альбома: {e}")

    def get_albums(self):
        try:
            self.cursor.execute('SELECT * FROM albums')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении альбомов: {e}")
            return []

    def update_album(self, album_id, **kwargs):
        try:
            for key, value in kwargs.items():
                self.cursor.execute(f'''
                    UPDATE albums
                    SET {key} = ?
                    WHERE id = ?
                ''', (value, album_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении альбома: {e}")

    def delete_album(self, album_id):
        try:
            self.cursor.execute('DELETE FROM albums WHERE id = ?', (album_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при удалении альбома: {e}")

    def close(self):
        self.connection.close()
