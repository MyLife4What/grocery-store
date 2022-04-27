from utils.grocery_store import GroceryStore

grocery_store = GroceryStore()

print(grocery_store.product().get_all_product())
print(grocery_store.product().get_product_by_id(5))
print(grocery_store.product().get_product_by_name("Frozen foods"))
print(grocery_store.product().get_product_by_sort_price())
print(grocery_store.product().get_product_by_sort_quantity())
print(grocery_store.customer().get_all_customer())
print(grocery_store.customer().get_customer_by_id(10))
print(grocery_store.customer().get_customer_by_name("Melanie"))
print(grocery_store.customer().get_customer_by_gender("Male"))
print(grocery_store.customer().get_customer_by_member_rank("Platinum"))