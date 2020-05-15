import sqlite3
from helpers import classificate_lang
from flask import Flask, render_template, request
conn = sqlite3.connect('library.db') # creates main database or connects
c = conn.cursor() # defines cursor to execute queries on main db

c.execute('CREATE TABLE IF NOT EXISTS library (id integer primary key autoincrement, title text, author text, lang text, year integer, other text)')

app = Flask(__name__) # Configure application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_title", methods=["GET", "POST"])
def search_title():
    if request.method == "GET":
        return render_template("search_title.html")
    else:
        with sqlite3.connect('library.db') as conn:
            title = request.form.get("title")
            c = conn.cursor()
            c.execute("SELECT * FROM library WHERE title LIKE ?", ('%{}%'.format(title),))
            results = c.fetchall()
            count =len(results)
            return render_template("search_title.html", results=results, count=count)

@app.route("/search_author", methods=["GET", "POST"])
def search_author():
    if request.method == "GET":
        return render_template("search_author.html")
    else:
        with sqlite3.connect('library.db') as conn:
            author = request.form.get("author")
            c = conn.cursor()
            c.execute("SELECT * FROM library WHERE author LIKE ?", ('%{}%'.format(author),))
            results = c.fetchall()
            count =len(results)
            return render_template("search_author.html", results=results, count=count)
        
@app.route("/search_lang", methods=["GET", "POST"])
def search_lang():
    if request.method == "GET":
        return render_template("search_lang.html")
    else:
        with sqlite3.connect('library.db') as conn:
            tmp = request.form.get("lang")
            lang = classificate_lang(tmp)
            c = conn.cursor()
            c.execute("SELECT * FROM library WHERE lang LIKE ?", ('%{}%'.format(lang),))
            results = c.fetchall()
            count =len(results)
            return render_template("search_lang.html", results=results, count=count)

@app.route("/search_label", methods=["GET", "POST"])
def search_label():
    if request.method == "GET":
        return render_template("search_other.html")
    else:
        with sqlite3.connect('library.db') as conn:
            label = request.form.get("label")
            c = conn.cursor()
            c.execute("SELECT * FROM library WHERE other LIKE ?", ('%{}%'.format(label),))
            results = c.fetchall()
            count =len(results)
            return render_template("search_other.html", results=results, count=count)

@app.route("/add_book", methods=["GET", "POST"])
def update_add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")
        tmp = request.form.get("lang")
        other = request.form.get("label")
        lang = classificate_lang(tmp)
        with sqlite3.connect('library.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO library (title, author, lang, year, other) VALUES (?,?,?,?,?)', (title, author, lang, year, other))
            return render_template("add_book.html")
            
    else:
        return render_template("add_book.html")

@app.route("/delete_book", methods=["GET", "POST"])
def update_delete():
    if request.method == "POST":
        ident = request.form.get("ident")
        with sqlite3.connect('library.db') as conn:
            c = conn.cursor()
            c.execute('DELETE FROM library WHERE id = :ident',{'ident':ident})
            return render_template("delete_book.html")
            
    else:
        return render_template("delete_book.html")
    
@app.route("/catalogue")
def catalogue():
    with sqlite3.connect('library.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM library")
            results = c.fetchall()
            count =len(results)
            return render_template("catalogue.html", results=results, count=count)



if __name__ == '__main__':
    app.run()
      