# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/baxa_akee_2602


# word to deciaml system 

def to_decimal(string):
    decimal_list = []
    for char in string:
        decimal_list.append(ord(char))
    return decimal_list

a = input('Enter the word: ')
decimal_code = to_decimal(a)
print(decimal_code)
