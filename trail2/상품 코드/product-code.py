product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class co:
    def __init__(self, pn='codetree', pc=50):
        self.pn = pn
        self.pc = pc
comm1 = co()
comm2 = co(product_name, product_code)
print(f"""product {comm1.pc} is {comm1.pn}
product {comm2.pc} is {comm2.pn}""")