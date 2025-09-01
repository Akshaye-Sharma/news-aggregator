import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        phone TEXT,
        country TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        publishedAt TEXT,
        description TEXT,
        content TEXT,
        link TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_saved_articles (
        user_id INTEGER,
        article_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (article_id) REFERENCES articles(id),
        PRIMARY KEY (user_id, article_id)
    )
    """)

    conn.commit()
    conn.close()

def save_article(user_id, article):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO articles (title, author, publishedAt, description, content, link)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (article["title"], article.get("author"), article.get("publishedAt"),
          article.get("description"), article.get("content"), article.get("url")))

    cursor.execute("SELECT id FROM articles WHERE link = ?", (article.get("url"),))
    article_id = cursor.fetchone()[0]

    cursor.execute("""
    INSERT OR IGNORE INTO user_saved_articles (user_id, article_id)
    VALUES (?, ?)
    """, (user_id, article_id))

    conn.commit()
    conn.close()

def get_saved_articles(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT a.title, a.author, a.publishedAt, a.description, a.content, a.link
    FROM articles a
    JOIN user_saved_articles usa ON a.id = usa.article_id
    WHERE usa.user_id = ?
    """, (user_id,))
    
    articles = cursor.fetchall()

    conn.close()
    return articles

def remove_saved_article(user_id, article):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM articles WHERE link = ?", (article.get("url"),))
    result = cursor.fetchone()

    if result:
        article_id = result[0]
        cursor.execute("""
        DELETE FROM user_saved_articles 
        WHERE user_id = ? AND article_id = ?
        """, (user_id, article_id))

    conn.commit()
    conn.close()

def is_article_saved(user_id, article):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT a.id FROM articles a
    JOIN user_saved_articles usa ON a.id = usa.article_id
    WHERE usa.user_id = ? AND a.link = ?
    """, (user_id, article.get("url")))

    result = cursor.fetchone()
    conn.close()
    return result is not None

