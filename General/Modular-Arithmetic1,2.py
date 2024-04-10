# def find_b(a, m):
#     b = a % m 
#     return b
# a, m = map(int, input("Enter a and m: ").split())
# result = find_b(a, m)
# print(result)
def find_b_Fermat(a, m):
    b = pow(a, m-1, m) #base**exponent % modulus
    return b
'''
Hàm `find_b_Fermat(a, m)` sử dụng định lý nhỏ Fermat trong số học.
Định lý này nói rằng nếu `p` là một số nguyên tố, 
và `a` là một số nguyên bất kỳ không chia hết cho `p`, 
thì `a^(p-1) ≡ 1 (mod p)`. 

Trong hàm này, `a` là cơ sở và `m` là module. 
Hàm `pow(a, m-1, m)` tính `a^(m-1) mod m`.
Kết quả của phép toán này được gán cho `b` và sau đó được trả về.
Vì vậy, hàm này tìm `b` sao cho `b ≡ a^(m-1) (mod m)`'''

a, m = map(int, input("Enter a and m: ").split())
result = find_b_Fermat(a, m)
print(result)