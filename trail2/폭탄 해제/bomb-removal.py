unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class co:
    def __init__(self, uc, wc, s):
        self.uc = uc
        self.wc = wc
        self.s = s

comm = co(unlock_code, wire_color, seconds)
print(f"""code : {comm.uc}
color : {comm.wc}
second : {comm.s}""")