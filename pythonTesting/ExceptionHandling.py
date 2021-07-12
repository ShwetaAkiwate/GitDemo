
ItemsInCart = 0

# 2 items will be added to cart

if ItemsInCart != 2:  #raise Exception("Product cart count not match")  # raise is keyword
    pass

assert(ItemsInCart == 0)
#assert(ItemsInCart == 0) execution will fail

# try,  catch

try:
    with open('filelog.txt', 'r') as reader:   # filelog file is not exist so it will throw error
        # with open('test.txt', 'r') as reader:  # test file is exist
        reader.read()

except Exception as e:       # in python we will use except keyword for Catch
    print(e)

finally:
    print("Cleaning up resources")
