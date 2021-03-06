class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x, y):
        self.x = x
        self.y = y
        
        return x * y
    
    def backword(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        
        return dx, dy

if __name__ == '__main__':
    apple = 100
    apple_num = 2
    tax = 1.1

    # layer
    mul_apple_layer = MulLayer()
    mul_tax_layer = MulLayer()
    
    # forward
    apple_price = mul_apple_layer.forward(apple, apple_num)
    price = mul_tax_layer.forward(apple_price, tax)
    
    print(price)

    # backward
    dprice = 1
    dapple_price, dtax = mul_tax_layer.backword(dprice)
    dapple, dapple_num = mul_apple_layer.backword(dapple_price)
    
    print(dapple, dapple_num, dapple_price)
    