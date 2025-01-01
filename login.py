import sqlite3
from getpass import getpass

def login(username, password):
    
    try:
        conn = sqlite3.connect(':memory:')
        db = conn.cursor()

        db.execute('''
        CREATE TABLE IF NOT EXISTS `customers` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `conversations` TEXT NOT NULL,
        `created_at` TIMESTAMP DEFAULT NULL,
        `updated_at` TIMESTAMP DEFAULT NULL
        );
        ''')

        db.execute('''
        CREATE TABLE IF NOT EXISTS `menus` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `name` TEXT NOT NULL,
        `desc` TEXT NOT NULL,
        `buy_price` INTEGER NOT NULL,
        `sell_price` INTEGER NOT NULL,
        `unlock_xp_at` INTEGER NOT NULL,
        `menu_type` INTEGER NOT NULL,
        `created_at` TIMESTAMP NOT NULL,
        `updated_at` TIMESTAMP NOT NULL
        );
        ''')

        db.execute('''
        CREATE TABLE IF NOT EXISTS `stocks` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `user_id` INTEGER NOT NULL,
        `menu_id` INTEGER NOT NULL,
        `quantity` INTEGER DEFAULT 0,
        `created_at` TIMESTAMP NOT NULL,
        `updated_at` TIMESTAMP NOT NULL,
        FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
        FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`) ON UPDATE CASCADE
        );
        ''')

        db.execute('''
        CREATE TABLE IF NOT EXISTS `hints` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `desc` TEXT NOT NULL,
        `menu_type` INTEGER NOT NULL,
        `created_at` TIMESTAMP NOT NULL,
        `updated_at` TIMESTAMP NOT NULL
        );
        ''')

        db.execute('''
        CREATE TABLE IF NOT EXISTS `users` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `username` TEXT NOT NULL,
        `password` TEXT NOT NULL,
        `xp` INTEGER NOT NULL DEFAULT 0,
        `credits` INTEGER NOT NULL DEFAULT 0,
        `created_at` TIMESTAMP NOT NULL,
        `updated_at` TIMESTAMP NOT NULL
        );
        ''')

        db.execute('''
        INSERT INTO `users` (`username`, `password`, `xp`, `credits`, `created_at`, `updated_at`) VALUES
        ('user1', 'password123', 50, 1000, '2024-01-01 06:00:00', '2024-01-01 06:00:00'),
        ('user2', 'password456', 30, 500, '2024-01-02 06:00:00', '2024-01-02 06:00:00'),
        ('user3','1234', 60, 1500, '2025-01-02 05:25:57', '2025-01-02 05:25:59');
        ''')

        conn.commit()

        db.execute('SELECT * FROM `users` WHERE `username` = ? AND `password` = ?', (username, password))
        user = db.fetchone()

        if user:
            print("\nLogin successful!\n")
            print(f"\nWelcome, {user[1]}! Your XP: {user[3]}, Credits: {user[4]}\n")
        else:
            print("username atau password salah.")

    except sqlite3.Error as e:
        print(f"error: {e}")

    finally:
        if conn:
            conn.close()


print("\nLogin untuk masuk ke dalam game!\n")
username_input = input("username: ")
password_input = getpass("password: ")
login(username_input, password_input)


