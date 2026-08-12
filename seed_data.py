from database.connection import SessionLocal
from database.models import Store, ReorderLevel

db = SessionLocal()

# One line per store — copy this pattern for all your stores
stores = [
    Store(store_code="1123", name="GK2", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1245", name="Okhla", city="NCR", type="Factory", active=True),
    Store(store_code="1342", name="CP", city="NCR", type="retail_partner", active=True),
    Store(store_code="1854", name="Model Town", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1912", name="Vasant Kunj", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1763", name="Sector 50", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1189", name="Udyog Vihar", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1174", name="Satyaniketan", city="NCR", type="dark kitchen", active=True),
    Store(store_code="1291", name="Sec 44 Noida", city="NCR", type="dark kitchen", active=True),
    Store(store_code="2378", name="Andheri", city="Mumabi", type="dark kitchen", active=True),
    Store(store_code="2165", name="Lower Parel", city="Mumbai", type="dark kitchen", active=True),
    Store(store_code="2956", name="Mahim (Khar)", city="Mumbai", type="dark kitchen", active=True),
    Store(store_code="3021", name="Dehradun", city="Dehradun", type="dark kitchen", active=True),
    Store(store_code="4823", name="Anna Nagar", city="Chennai", type="dark kitchen", active=True),
    Store(store_code="4721", name="Adyar (Kottupuram)", city="Chennai", type="dark kitchen", active=True),
    Store(store_code="4907", name="OMR (Okkiyampet)", city="Chennai", type="dark kitchen", active=True),
    Store(store_code="4238", name="Royapuram (Washermenpet)", city="Chennai", type="dark kitchen", active=True),
    Store(store_code="5013", name="Whitefield", city="Bangalore", type="dark kitchen", active=True),
    Store(store_code="5825", name="Kalyan Nagar (HBR)", city="Bengalore", type="dark kitchen", active=True),
    Store(store_code="5174", name="Indira Nagar", city="Bangalore", type="dark kitchen", active=True),
    Store(store_code="5692", name="Sarjapur", city="Bangalore", type="dark kitchen", active=True),
    Store(store_code="6321", name="Manikonda", city="Hyderabad", type="dark kitchen", active=True),
    Store(store_code="6943", name="Gowchibowli", city="Hyderabad", type="dark kitchen", active=True)
    # add the rest of your stores here, same pattern
]
for store in stores:
    db.merge(store)

# One line per SKU — copy this pattern for every flavor/size you sell
reorder_items = [
    ReorderLevel(sku_name="Amarena Cherry (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Berry Berry Cheesy (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Biscoff (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Coffee Dunked Brownie (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Epic Indian Butterscotch (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="La La Lavender (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Rose n Cinnamon (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Strawberry Cheesecake (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Triple Berry Bomb (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Kesar Almond Pista No Sugar (125ml)", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Yes Choco Hazelnut No Sugar (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Yes Filter Coffee No Sugar (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Yes Mocha Almond No Sugar (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Yes Vanilla No Sugar (125ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Matcha Latte No Sugar (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Vegan Filter Coffee (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Vegan Mango (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Vegan Triple Berry (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Vegan Matcha Strawberry (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Dot Cake Red Velvet (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Dot Cake Strawberry CK (125ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Brownie Fudge Choco Hazelnut (180ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Chocolate 4x (180ml)", reorder_level=3, moq=6),
    ReorderLevel(sku_name="Ghana Dark Chocolate (180ml)", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Jags n Crunch (180ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Nutty Jags (180ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="Rose n Cinnamon (180ml)", reorder_level=2, moq=4),
    ReorderLevel(sku_name="South Indian Filter Coffee (180ml)", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Biscoff (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Brownie Fudge Choco Hazelnut (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Coffee Dunked Brownie (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Chocolate 4X (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Epic Indian Butterscotch (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Ghana Dark Chocolate (500ml)", reorder_level=2, moq=3),
    ReorderLevel(sku_name="South Indian Filter Coffee (500ml)", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Strawberry Cheesecake (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Kesar Almond Pista No Sugar (500ml)", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Yes Choco Hazelnut No Sugar (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Yes Filter Coffee No Sugar (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Yes Mocha Almond No Sugar (500ml)", reorder_level=1, moq=2),
    ReorderLevel(sku_name="Yes Vanilla No Sugar (500ml)", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Chocolate Fudge Sauce", reorder_level=2, moq=5),
    ReorderLevel(sku_name="SF Chocolate Sauce", reorder_level=2, moq=5),
    ReorderLevel(sku_name="Bonnies Vanilla", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Bonnies Coffee", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Bonnies Mint", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Cassata Bites", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Tiramisu Sandwich", reorder_level=2, moq=5),
    ReorderLevel(sku_name="Brownie Sandwich Vanilla", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Brownie Sandwich Filter Coffee", reorder_level=2, moq=3),
    ReorderLevel(sku_name="Mini ChocoBar Coffee Brownie", reorder_level=2, moq=5),
    ReorderLevel(sku_name="Mini ChocoBar Biscoff", reorder_level=2, moq=5),
    ReorderLevel(sku_name="Frostreats Banana", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Frostreats Blueberry", reorder_level=5, moq=9),
    ReorderLevel(sku_name="Frostreats Cookies", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Frostreats Mango", reorder_level=4, moq=9),
    ReorderLevel(sku_name="Frostreats Peanut Butter", reorder_level=5, moq=9),
    ReorderLevel(sku_name="Frostreats Vanilla", reorder_level=5, moq=9),
    ReorderLevel(sku_name="Frostreats Waffles", reorder_level=4, moq=9)
    # add the rest of your SKUs here, same pattern
]
for item in reorder_items:
    db.merge(item)

db.commit()
db.close()
print("Data added.")