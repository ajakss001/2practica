import sqlite3
from datetime import datetime

class BarApp:
    def __init__(self, db='bar.db'):
        self.conn = sqlite3.connect(db)
        self.conn.executescript('''
            CREATE TABLE IF NOT EXISTS drinks(id INTEGER PRIMARY KEY, name TEXT, type TEXT,
                strength REAL, volume INTEGER, price REAL, stock INTEGER);
            CREATE TABLE IF NOT EXISTS cocktails(id INTEGER PRIMARY KEY, name TEXT, price REAL);
            CREATE TABLE IF NOT EXISTS recipes(cocktail_id INTEGER, drink_id INTEGER, amount INTEGER);
            CREATE TABLE IF NOT EXISTS transactions(type TEXT, item_id INTEGER,
                quantity INTEGER, total REAL, timestamp TEXT);
        ''')

    def add_drink(self, name, type_, strength, volume, price, stock):
        self.conn.execute('INSERT INTO drinks VALUES(NULL,?,?,?,?,?,?)',
            (name, type_, strength, volume, price, stock))
        self.conn.commit()

    def add_cocktail(self, name, price, components):
        cid = self.conn.execute('INSERT INTO cocktails VALUES(NULL,?,?)',
            (name, price)).lastrowid
        for drink_id, amount in components:
            self.conn.execute('INSERT INTO recipes VALUES(?,?,?)',
                (cid, drink_id, amount))
        self.conn.commit()
        return cid

    def get_cocktail_strength(self, cid):
        total_alcohol = sum(strength*amount/100 for strength, amount in
            self.conn.execute('SELECT d.strength, r.amount FROM recipes r '
            'JOIN drinks d ON r.drink_id=d.id WHERE r.cocktail_id=? AND d.type="alcohol"', (cid,))
        )
        total_volume = sum(row[0] for row in self.conn.execute('SELECT amount FROM recipes WHERE cocktail_id=?', (cid,)))



        return round(total_alcohol/total_volume*100, 1) if total_volume else 0

    def sell(self, item_type, item_id, quantity):
        try:
            if item_type == 'cocktail':
                for drink_id, needed in self.conn.execute(
                    'SELECT drink_id, amount*? FROM recipes WHERE cocktail_id=?', (quantity, item_id)):
                    stock = self.conn.execute(
                        'SELECT stock FROM drinks WHERE id=?', (drink_id,)
                    ).fetchone()[0]
                    if stock < needed:
                        return False
                    self.conn.execute(
                        'UPDATE drinks SET stock=stock-? WHERE id=?', (needed, drink_id))
            else:
                stock = self.conn.execute(
                    'SELECT stock FROM drinks WHERE id=?', (item_id,)
                ).fetchone()[0]
                if stock < quantity:
                    return False
                self.conn.execute(
                    'UPDATE drinks SET stock=stock-? WHERE id=?', (quantity, item_id))
            price = self.conn.execute(
                f'SELECT price FROM {"cocktails" if item_type=="cocktail" else "drinks"} WHERE id=?',
                (item_id,)
            ).fetchone()[0]
            self.conn.execute(
                'INSERT INTO transactions VALUES(?,?,?,?,?)',
                (item_type, item_id, quantity, price*quantity,
                 datetime.now().isoformat())
            )
            self.conn.commit()
            return True
        except:
            return False

    def restock(self, drink_id, amount):
        self.conn.execute(
            'UPDATE drinks SET stock=stock+? WHERE id=?', (amount, drink_id)
        )
        self.conn.commit()


if __name__ == '__main__':
    bar = BarApp()

    bar.add_drink('Vodka', 'alcohol', 40.0 , 1000 , 500.0 , 10)
    bar.add_drink('Cola', 'ingredient', 0.0 , 330 , 50.0 , 100)

    cid = bar.add_cocktail('Vodka Cola', 300.0 , [(1 , 50), (2 , 150)])

    print(f'крепкость: {bar.get_cocktail_strength(cid)}%')

    success = bar.sell('cocktail', cid , 2)
    print(f'Продажа успешна: {success}')

    bar.restock(1 , 5)