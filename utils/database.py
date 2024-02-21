import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Work with categories
    def get_categories(self):
        categories = self.cursor.execute("SELECT id, category_name FROM categories;")
        return categories

    def add_category(self, new_cat):
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()
        print(categories)
        if not categories:
            try:
                self.cursor.execute(
                    "INSERT INTO categories (category_name) VALUES(?);",
                    (new_cat,)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully added'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def upd_category(self, new_cat, old_cat):
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()

        if not categories:
            try:
                self.cursor.execute(
                    "UPDATE categories SET category_name=? WHERE category_name=?;",
                    (new_cat, old_cat)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully updated'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def edit_category(self, new_name, id):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE id=?",
                (new_name, id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def del_category(self, name, id):
        try:
            self.cursor.execute(
                "DELETE FROM categories WHERE id=?, product_name=?",
                (name, id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def get_product(self):
        products = self.cursor.execute("SELECT id, product_name FROM categories;")
        return products

    def add_product(self, new_cat):
        products = self.cursor.execute(
            "SELECT id, product_name FROM products WHERE product_name=?;",
            (new_cat,)
        ).fetchone()
        print(products)
        if not products:
            try:
                self.cursor.execute(
                    "INSERT INTO products (product_name) VALUES(?);",
                    (new_cat,)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully added'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def upd_product(self, new_cat, old_cat):
        products = self.cursor.execute(
            "SELECT id, product_name FROM products WHERE product_name=?;",
            (new_cat,)
        ).fetchone()

        if not products:
            try:
                self.cursor.execute(
                    "UPDATE products SET product_name=? WHERE product_name=?;",
                    (new_cat, old_cat)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully updated'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def edit_product(self, new_name, id):
        try:
            self.cursor.execute(
                "UPDATE products SET product_name=? WHERE id=?",
                (new_name, id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def del_product(self, name, id):
        try:
            self.cursor.execute(
                "DELETE FROM products WHERE id=?, product_name=?",
                (name, id)
            )
            self.conn.commit()
            return True
        except:
            return False
