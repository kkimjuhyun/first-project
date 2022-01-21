def price(people):
    print("{0}명 가격은 {1}원입니다.".format(people, people * 10000))

def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다. ".format(people, people * 6000))

def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))


# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(4)
# mv.price_morning(4)
# mv.price_soldier(3)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning  #솔져 제외
# price(4)
# price_morning(5)
# price_soldier(3) #오류 발생

from theater_module import price_soldier as price
price(3)