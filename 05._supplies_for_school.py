number_of_pens = int(input())
number_of_markers = int(input())
cleaning_detergent = int(input())
discount = float (input())

pens_price = number_of_pens * 5.80
marker_price = number_of_markers * 7.2
detergent_price = cleaning_detergent * 1.20

total_price = pens_price + marker_price + detergent_price
discount_all = total_price * discount / 100
price_after_discount = total_price - discount_all

print (price_after_discount)