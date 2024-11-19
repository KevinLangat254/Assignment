def calculate_discount(price,discount_percent):
   if discount_percent>=20:
      discount=(discount_percent*price)/100
      newPrice=price-discount
      print(f'The new price for the item is: {newPrice}')
   else:
      print(f'The price for the item is still: {price} ')
price=float(input('Enter the original price of an item:'))
discount_percent=float(input('Enter the disount percentage: ')) 
calculate_discount(price,discount_percent)     