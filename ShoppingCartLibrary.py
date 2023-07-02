"""
Library/Module name: Shopping Cart Library

Author: Sam Goldberg
"""
import os
import io

#Make a cart, check if there is a carts folder before just blindly making one
cart = []
if os.path.exists("Carts") == False:
  os.mkdir("Carts")

def add_items_to_cart(num):
  """
  Adds items to cart. Based on num variable
  """
  
  for item in range(int(num)):
    print("Enter item: ")
    cItem = input(":> ")
    cart.append(cItem)
  return cart 


def print_items():
  """
    Prints all items in cart
  """
  print("Your Cart")
  for item in cart:
    print("Item: ", item)

def save_cart(cart):
  if os.path.exists("Carts") == True:
    cName = input("Please name your cart: ")
    if cName == "":
      while cName == "":
        cName = input("Please name your cart: ")
    scart = io.open(rf"Carts\{cName}", "w+")
    scart.writelines(cart)
    scart.close()



