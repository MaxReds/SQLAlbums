from albums_db import Album, AlbumsDB


def main():
    db = AlbumsDB()

    while True:
        print("\nМузыкальные Альбомы")
        print("1. Добавить альбом")
        print("2. Показать все альбомы")
        print("3. Обновить альбом")
        print("4. Удалить альбом")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Название: ")
            artist = input("Исполнитель: ")
            release_year = input("Год выпуска: ")
            genre = input("Жанр: ")
            album = Album(title, artist, release_year, genre)
            db.add_album(album)
            print("Альбом добавлен.")
        elif choice == '2':
            albums = db.get_albums()
            for album in albums:
                print(f"{album[0]}. {album[1]} - {album[2]} ({album[3]}, {album[4]})")
        elif choice == '3':
            album_id = input("ID альбома для обновления: ")
            field = input("Поле для обновления (title, artist, release_year, genre): ")
            new_value = input("Новое значение: ")
            db.update_album(album_id, **{field: new_value})
            print("Альбом обновлен.")
        elif choice == '4':
            album_id = input("ID альбома для удаления: ")
            db.delete_album(album_id)
            print("Альбом удален.")
        elif choice == '5':
            db.close()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()