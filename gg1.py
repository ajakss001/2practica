import sqlite3
from datetime import datetime


class DrinkApp:
    def __init__(self, db_file="drinks.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS alcohol (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                strength REAL NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS cocktails (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY,
                cocktail_id INTEGER NOT NULL,
                alcohol_id INTEGER,
                ingredient_id INTEGER,
                amount INTEGER NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                item_type TEXT NOT NULL,
                item_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total REAL NOT NULL,
                date TEXT NOT NULL)"""
        ]
        for table in tables:
            self.conn.execute(table)
        self.conn.commit()

    def add_drink(self, name, strength, quantity, price):
        self.conn.execute("INSERT INTO alcohol VALUES (NULL,?,?,?,?)",
                          (name, strength, quantity, price))
        self.conn.commit()

    def add_ingredient(self, name, quantity):
        self.conn.execute("INSERT INTO ingredients VALUES (NULL,?,?)", (name, quantity))
        self.conn.commit()

    def add_cocktail(self, name, price):
        self.conn.execute("INSERT INTO cocktails VALUES (NULL,?,?)", (name, price))
        self.conn.commit()
        return self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    def add_component(self, cocktail_id, alcohol_id=None, ingredient_id=None, amount=0):
        self.conn.execute("INSERT INTO components VALUES (NULL,?,?,?,?)",
                          (cocktail_id, alcohol_id, ingredient_id, amount))
        self.conn.commit()

    def sell(self, item_type, item_id, quantity):
        if item_type == 'alcohol':
            item = self.conn.execute("SELECT price,quantity FROM alcohol WHERE id=?",
                                     (item_id,)).fetchone()
        else:
            item = self.conn.execute("SELECT price,1 FROM cocktails WHERE id=?",
                                     (item_id,)).fetchone()
            for comp in self.conn.execute("SELECT alcohol_id,ingredient_id,amount FROM components WHERE cocktail_id=?",
                                          (item_id,)):
                alc, ing, amt = comp
                if alc:
                    stock = self.conn.execute("SELECT quantity FROM alcohol WHERE id=?",
                                              (alc,)).fetchone()[0]
                    if stock < amt * quantity:
                        raise ValueError("Not enough stock")
                if ing:
                    stock = self.conn.execute("SELECT quantity FROM ingredients WHERE id=?",
                                              (ing,)).fetchone()[0]
                    if stock < amt * quantity:
                        raise ValueError("Not enough stock")

        if item[1] < quantity and item_type == 'alcohol':
            raise ValueError("Not enough stock")

        total = item[0] * quantity
        self.conn.execute("INSERT INTO sales VALUES (NULL,?,?,?,?,?)",
                          (item_type, item_id, quantity, total, datetime.now().isoformat()))

        if item_type == 'alcohol':
            self.conn.execute("UPDATE alcohol SET quantity=quantity-? WHERE id=?",
                              (quantity, item_id))
        else:
            for comp in self.conn.execute("SELECT alcohol_id,ingredient_id,amount FROM components WHERE cocktail_id=?",
                                          (item_id,)):
                alc, ing, amt = comp
                if alc:
                    self.conn.execute("UPDATE alcohol SET quantity=quantity-? WHERE id=?",
                                      (amt * quantity, alc))
                if ing:
                    self.conn.execute("UPDATE ingredients SET quantity=quantity-? WHERE id=?",
                                      (amt * quantity, ing))
        self.conn.commit()

    def restock(self, item_type, item_id, amount):
        table = 'alcohol' if item_type == 'alcohol' else 'ingredients'
        self.conn.execute(f"UPDATE {table} SET quantity=quantity+? WHERE id=?",
                          (amount, item_id))
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = DrinkApp()

    db.add_drink("Whiskey", 40, 10, 700)
    db.add_drink("Tequila", 38, 8, 650)
    db.add_ingredient("Cola", 20)
    db.add_ingredient("Lemon", 15)

    cid = db.add_cocktail("Whiskey Cola", 300)
    db.add_component(cid, alcohol_id=1, amount=50)
    db.add_component(cid, ingredient_id=1, amount=150)

    db.sell('cocktail', 1, 2)
    db.sell('alcohol', 1, 1)
    db.restock('alcohol', 1, 5)

    db.close()