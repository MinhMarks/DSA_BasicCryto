# a^(p-2) % p = a^(-1)  
from Crypto.Util.number import inverse
print(inverse(3, 13)) 
'''Hàm `inverse(a, n)` trong thư viện `Crypto.Util.number` 
của Python được sử dụng để tính **nghịch đảo modulo. 
Cụ thể, inverse(a, n) sẽ trả về số nguyên b 
sao cho (a * b) mod n = 1.
Nói cách khác, b là nghịch đảo của a theo modulo n 
inverse(3, 13) sẽ trả về nghịch đảo của 3 theo modulo 13
nghĩa là nó sẽ tìm số `b` sao cho (3 * b) mod 13 = 1 
Lưu ý rằng nếu `a` và `n` không nguyên tố cùng nhau
(nghĩa là gcd(a, n) != 1), 
thì không tồn tại nghịch đảo modulo và hàm inverse(a, n) sẽ trả về lỗi
'''
# def mod_inv(x, y):
#     for i in range(y):
#         if x*i % y == 1:
#             return i
# print(mod_inv(3, 13))