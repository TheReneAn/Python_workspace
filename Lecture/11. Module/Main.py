''' Way 1 '''
import theater_module

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

''' Way 2 '''
import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

''' Way 3 '''
from theater_module import *

price(3)
price_morning(4)
price_soldier(5)

''' Way 4 '''
from theater_module import price, price_morning
price(3)
price_morning(4)
# price_soldier(5)      => Can not use it

''' Way 5 '''
from theater_module import price_soldier as price
price(5)





