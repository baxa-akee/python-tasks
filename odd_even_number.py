# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/baxa_akee_2602



# release the even and odd numbers

def s():
    a = []
    s = []
    d = int(input('A ni kiriting: \n'))
    b = int(input('B ni kiriting: \n'))
    for i in range (d,b):
        if i % 2 == 0:
            a.append(f"Even: {i}")
        else:
            s.append(f"Odd: {i}")
    print(a)
    print(s)
s()
