import pandas as pd
import random
import os
from faker import Faker

fake = Faker('de_DE')

# ============================================
# RESTAURANTS
# ============================================
def generate_restaurants():
    restaurants_data = [
        {
            "restaurant_id": "REST-BER-001",
            "name": "Zur Goldenen Gabel Downtown",
            "city": "Berlin",
            "country": "Germany",
            "address": "Unter den Linden 12, Berlin",
            "opening_date": "2023-01-15",
            "phone": "+49-30-123-4567"
        },
        {
            "restaurant_id": "REST-BER-002",
            "name": "Zur Goldenen Gabel Mitte",
            "city": "Berlin",
            "country": "Germany",
            "address": "Alexanderplatz 5, Berlin",
            "opening_date": "2023-06-20",
            "phone": "+49-30-234-5678"
        },
        {
            "restaurant_id": "REST-MUC-001",
            "name": "Zur Goldenen Gabel Marienplatz",
            "city": "Munich",
            "country": "Germany",
            "address": "Marienplatz 8, Munich",
            "opening_date": "2023-03-10",
            "phone": "+49-89-345-6789"
        },
        {
            "restaurant_id": "REST-MUC-002",
            "name": "Zur Goldenen Gabel Schwabing",
            "city": "Munich",
            "country": "Germany",
            "address": "Leopoldstrasse 45, Munich",
            "opening_date": "2023-09-05",
            "phone": "+49-89-456-7890"
        },
        {
            "restaurant_id": "REST-HAM-001",
            "name": "Zur Goldenen Gabel Hafencity",
            "city": "Hamburg",
            "country": "Germany",
            "address": "Speicherstadt 3, Hamburg",
            "opening_date": "2024-02-14",
            "phone": "+49-40-567-8901"
        }
    ]

    df_restaurants = pd.DataFrame(restaurants_data)
    return df_restaurants

# ============================================
# MENU ITEMS (Master List)
# ============================================
def generate_menu_items():
    master_menu = [
        # Starters (Vorspeisen)
        {"item_id": "ITEM-101", "name": "Leberknödelsuppe", "category": "Starter", "price": 9.50, "ingredients": "Liver Dumplings, Beef Broth, Chives", "is_vegetarian": False, "spice_level": "Mild"},
        {"item_id": "ITEM-102", "name": "Obatzda mit Brezn", "category": "Starter", "price": 8.00, "ingredients": "Camembert, Butter, Paprika, Pretzel", "is_vegetarian": True, "spice_level": "Mild"},
        {"item_id": "ITEM-103", "name": "Currywurst Snack", "category": "Starter", "price": 7.50, "ingredients": "Pork Sausage, Curry Ketchup, Paprika", "is_vegetarian": False, "spice_level": "Medium"},
        {"item_id": "ITEM-104", "name": "Kartoffelsuppe", "category": "Starter", "price": 8.50, "ingredients": "Potato, Leek, Bacon, Cream", "is_vegetarian": False, "spice_level": "None"},
        {"item_id": "ITEM-105", "name": "Flammkuchen", "category": "Starter", "price": 11.00, "ingredients": "Thin Dough, Crème Fraîche, Onion, Bacon", "is_vegetarian": False, "spice_level": "None"},

        # Main Course - Vegetarian (Hauptgericht - Vegetarisch)
        {"item_id": "ITEM-201", "name": "Käsespätzle", "category": "Main Course", "price": 14.50, "ingredients": "Egg Noodles, Emmental Cheese, Fried Onions", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-202", "name": "Gemüseschnitzel", "category": "Main Course", "price": 13.00, "ingredients": "Breaded Vegetables, Lemon, Potato Salad", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-203", "name": "Kartoffelknödel mit Pilzrahmsoße", "category": "Main Course", "price": 15.00, "ingredients": "Potato Dumplings, Mushroom Cream Sauce, Herbs", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-204", "name": "Laugenbrezel mit Obatzda & Salat", "category": "Main Course", "price": 12.00, "ingredients": "Pretzel, Camembert Spread, Mixed Salad", "is_vegetarian": True, "spice_level": "Mild"},
        {"item_id": "ITEM-205", "name": "Reibekuchen mit Apfelmus", "category": "Main Course", "price": 11.50, "ingredients": "Potato Pancakes, Apple Sauce, Sour Cream", "is_vegetarian": True, "spice_level": "None"},

        # Main Course - Non-Vegetarian (Hauptgericht - Fleisch)
        {"item_id": "ITEM-301", "name": "Schweinshaxe", "category": "Main Course", "price": 22.50, "ingredients": "Pork Knuckle, Dark Beer Sauce, Sauerkraut, Dumplings", "is_vegetarian": False, "spice_level": "Mild"},
        {"item_id": "ITEM-302", "name": "Wiener Schnitzel", "category": "Main Course", "price": 20.00, "ingredients": "Veal, Breadcrumbs, Lemon, Parsley Potatoes", "is_vegetarian": False, "spice_level": "None"},
        {"item_id": "ITEM-303", "name": "Sauerbraten", "category": "Main Course", "price": 21.00, "ingredients": "Marinated Beef, Gingersnap Gravy, Red Cabbage, Dumplings", "is_vegetarian": False, "spice_level": "Mild"},
        {"item_id": "ITEM-304", "name": "Bratwurst mit Sauerkraut", "category": "Main Course", "price": 14.50, "ingredients": "Grilled Sausage, Sauerkraut, Mustard, Bread", "is_vegetarian": False, "spice_level": "Mild"},
        {"item_id": "ITEM-305", "name": "Rinderroulade", "category": "Main Course", "price": 23.00, "ingredients": "Beef Roll, Bacon, Pickles, Mustard, Red Wine Gravy", "is_vegetarian": False, "spice_level": "None"},

        # Sides (Beilagen)
        {"item_id": "ITEM-401", "name": "Kartoffelsalat", "category": "Side", "price": 5.50, "ingredients": "Potato, Vinegar, Mustard, Herbs", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-402", "name": "Rotkohl", "category": "Side", "price": 4.50, "ingredients": "Red Cabbage, Apple, Vinegar, Cloves", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-403", "name": "Semmelknödel", "category": "Side", "price": 5.00, "ingredients": "Bread Dumplings, Egg, Milk, Parsley", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-404", "name": "Bratkartoffeln", "category": "Side", "price": 6.00, "ingredients": "Pan-Fried Potatoes, Onion, Bacon", "is_vegetarian": False, "spice_level": "None"},
        {"item_id": "ITEM-405", "name": "Spätzle Butter", "category": "Side", "price": 5.50, "ingredients": "Egg Noodles, Butter, Parsley", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-406", "name": "Sauerkraut", "category": "Side", "price": 4.00, "ingredients": "Fermented Cabbage, Caraway Seeds, White Wine", "is_vegetarian": True, "spice_level": "None"},

        # Desserts (Nachspeisen)
        {"item_id": "ITEM-501", "name": "Schwarzwälder Kirschtorte", "category": "Dessert", "price": 7.50, "ingredients": "Chocolate Sponge, Cherries, Whipped Cream, Kirsch", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-502", "name": "Apfelstrudel mit Vanillesoße", "category": "Dessert", "price": 7.00, "ingredients": "Puff Pastry, Apple, Raisins, Cinnamon, Vanilla Sauce", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-503", "name": "Rote Grütze mit Sahne", "category": "Dessert", "price": 6.50, "ingredients": "Mixed Red Berries, Starch, Sugar, Cream", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-504", "name": "Dampfnudel mit Vanillesoße", "category": "Dessert", "price": 8.00, "ingredients": "Steamed Dough Dumpling, Vanilla Sauce, Poppy Seeds", "is_vegetarian": True, "spice_level": "None"},

        # Beverages (Getränke)
        {"item_id": "ITEM-601", "name": "Hefeweizen (0.5L)", "category": "Beverage", "price": 5.50, "ingredients": "Wheat Beer", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-602", "name": "Märzen (0.5L)", "category": "Beverage", "price": 5.50, "ingredients": "Lager Beer", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-603", "name": "Apfelschorle", "category": "Beverage", "price": 3.50, "ingredients": "Apple Juice, Sparkling Water", "is_vegetarian": True, "spice_level": "None"},
        {"item_id": "ITEM-604", "name": "Spezi", "category": "Beverage", "price": 3.50, "ingredients": "Cola, Orange Soda", "is_vegetarian": True, "spice_level": "None"},
    ]

    # ============================================
    # RESTAURANT MENU ITEMS
    # ============================================
    menu_items_data = []
    restaurants_data = generate_restaurants().to_dict('records')

    df_menu_items = pd.DataFrame(menu_items_data)
    for restaurant in restaurants_data:
        rest_id = restaurant["restaurant_id"]

        for item in master_menu:
            price_multiplier = random.uniform(0.95, 1.05)

            menu_items_data.append({
                "restaurant_id": rest_id,
                "item_id": item["item_id"],
                "name": item["name"],
                "category": item["category"],
                "price": round(item["price"] * price_multiplier, 2),
                "ingredients": item["ingredients"],
                "is_vegetarian": item["is_vegetarian"],
                "spice_level": item["spice_level"]
            })

    df_menu_items = pd.DataFrame(menu_items_data)
    return df_menu_items

# ============================================
# CUSTOMERS
# ============================================
def generate_customers(n=500):
    customers = []

    for i in range(n):
        join_date = fake.date_between(start_date='-2y', end_date='today')

        customer = {
            "customer_id": f"CUST-{10000 + i}",
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "city": random.choice(["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"]),
            "join_date": join_date.strftime("%Y-%m-%d"),
        }
        customers.append(customer)

    return pd.DataFrame(customers)


def generate_data_for_sql_db():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    df_restaurants = generate_restaurants()
    df_menu_items = generate_menu_items()
    df_customers = generate_customers(500)

    df_restaurants.to_csv(os.path.join( "data","restaurants.csv"), index=False)
    df_menu_items.to_csv(os.path.join("data", "menu_items.csv"), index=False)
    df_customers.to_csv(os.path.join( "data", "customers.csv"), index=False)

    print(f"Generated {len(df_restaurants)} restaurants")
    print(f"Generated {len(df_menu_items)} menu items")
    print(f"Generated {len(df_customers)} customers")


if __name__ == "__main__":
    generate_data_for_sql_db()