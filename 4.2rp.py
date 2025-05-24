import sqlite3

conn = sqlite3.connect('ilovedrink.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS Drinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    alcohol_content REAL NOT NULL,
    volume_ml REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    alcohol_content REAL NOT NULL,
    volume_ml REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS Stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_id INTEGER,
    ingredient_id INTEGER,
    quantity_ml REAL NOT NULL,
    FOREIGN KEY (drink_id) REFERENCES Drinks(id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(id)
);
CREATE TABLE IF NOT EXISTS Cocktails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS CocktailIngredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cocktail_id INTEGER,
    ingredient_id INTEGER,
    amount_ml REAL NOT NULL,
    FOREIGN KEY (cocktail_id) REFERENCES Cocktails(id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(id)
);
''')
conn.commit()


def add_entry(table, data):
    placeholders = ', '.join(['?'] * len(data))
    cursor.execute(f"INSERT INTO {table} VALUES (NULL, {placeholders})", data)
    conn.commit()
    return cursor.lastrowid


def update_stock(ingredient_id=None, drink_id=None, amount=0):
    if ingredient_id:
        cursor.execute("SELECT quantity_ml FROM Stock WHERE ingredient_id=?", (ingredient_id,))
        row = cursor.fetchone()
        qty = row[0] if row else 0
        new_qty = qty + amount
        if row:
            cursor.execute("UPDATE Stock SET quantity_ml=? WHERE ingredient_id=?", (new_qty, ingredient_id))
        else:
            cursor.execute("INSERT INTO Stock (ingredient_id, quantity_ml) VALUES (?, ?)", (ingredient_id, amount))
        conn.commit()
        return
    if drink_id:
        cursor.execute("SELECT quantity_ml FROM Stock WHERE drink_id=?", (drink_id,))
        row = cursor.fetchone()
        qty = row[0] if row else 0
        new_qty = qty + amount
        if row:
            cursor.execute("UPDATE Stock SET quantity_ml=? WHERE drink_id=?", (new_qty, drink_id))
        else:
            cursor.execute("INSERT INTO Stock (drink_id, quantity_ml) VALUES (?, ?)", (drink_id, amount))
        conn.commit()


def get_stock(ingredient_id=None, drink_id=None):
    if ingredient_id:
        cursor.execute("SELECT quantity_ml FROM Stock WHERE ingredient_id=?", (ingredient_id,))
        row = cursor.fetchone()
        return row[0] if row else 0
    if drink_id:
        cursor.execute("SELECT quantity_ml FROM Stock WHERE drink_id=?", (drink_id,))
        row = cursor.fetchone()
        return row[0] if row else 0
    return 0


def create_cocktail(name, price, ingredients):
    cid = add_entry('Cocktails', [name, price])
    for ing_id, amount in ingredients:
        add_entry('CocktailIngredients', [cid, ing_id, amount])
    return cid


def calculate_strength(cocktail_id):
    cursor.execute('''
        SELECT ci.amount_ml, i.alcohol_content 
        FROM CocktailIngredients ci JOIN Ingredients i ON ci.ingredient_id=i.id 
        WHERE ci.cocktail_id=?
    ''', (cocktail_id,))

    total_volume = total_alcohol = 0
    for amount_ml, alc in cursor.fetchall():
        total_volume += amount_ml
        total_alcohol += amount_ml * alc / 100

    return (total_alcohol / total_volume) * 100 if total_volume else 0


def sell_cocktail(cocktail_id):
    cursor.execute('SELECT ingredient_id, amount_ml FROM CocktailIngredients WHERE cocktail_id=?', (cocktail_id,))
    ingredients_list = cursor.fetchall()

    for ing_idx, req_amount in ingredients_list:
        if get_stock(ingredient_id=ing_idx) < req_amount:
            print("Недостаточно ингредиентов.")
            return False

    for ing_idx, req_amount in ingredients_list:
        update_stock(ingredient_id=ing_idx, amount=-req_amount)

    print("Коктейль продан!")
    return True


if __name__ == "__main__":
    lemon_juice_ingredients = add_entry('Ingredients', ['Лимонный сок', 0.0, 1000])
    triple_sec_ingredients = add_entry('Ingredients', ['Трипл сек', 30.0, 1000])

    vodka_drink = add_entry('Drinks', ['Водка', 40.0, 500])

update_stock(ingredient_id=lemon_juice_ingredients, amount=2000)
update_stock(ingredient_id=triple_sec_ingredients, amount=1500)

martinez_ingredients = [
    (lemon_juice_ingredients, 50),
    (triple_sec_ingredients, 30)
]
martinez_price = 10.0

martinez_cocktail_ID = create_cocktail("Мартинез", martinez_price, martinez_ingredients)

strength_percent = calculate_strength(martinez_cocktail_ID)
print(f"Крепость коктейля 'Мартинез' составляет {strength_percent:.2f}%.")

sell_cocktail(martinez_cocktail_ID)

conn.close()