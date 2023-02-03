CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(30),
    drink VARCHAR(3),
    extras VARCHAR(50),
    price INTEGER
);


-- # extras[]
-- # def nameInput("hello whats your name?")
-- # return name

-- # def drinkInput():
-- # order = input("what drink you want")
-- # return order

-- # def sizeInput():
-- # size = input("what size drink would you like (sml/med/large")
-- # size = size.lower()
-- # return size

-- # def extrasInput():
-- # yes = input("would you like any extras?")
-- # yes = yes.lower()
-- # while yes == "yes":
-- #     yes = input("would you like any extras")
-- #     extra = input("what extra would you like")
-- #     extras.append(extra)


