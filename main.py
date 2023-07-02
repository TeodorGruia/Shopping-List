"""
Program name: Shopping list
Date of first writing: 7/2/2023
Author: Sam Goldberg
"""
import ShoppingCartLibrary 

def main():
  print("Welcome to the Shopping cart application!")
  num_items = input("How many items are you buying? ")
  print("Please add your items below")
  t = ShoppingCartLibrary.add_items_to_cart(num_items)
  
  sv_yn = input("Save Cart? [y] or [n]: ")
  if sv_yn == "y":
    ShoppingCartLibrary.save_cart(t)
  else:
    print("Your cart is not saved, want to build another cart? ")
    bc_yn = input("[y] or [n]: ")
    if bc_yn == "y":
      main()
    

if __name__ == "__main__": main()


