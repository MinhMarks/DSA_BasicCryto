from sympy import *
from Crypto.Util.number import long_to_bytes
N = 0xb8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d
e = 0x9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3
c = 0x3f984ff5244f1836ed69361f29905ca1ae6b3dcf249133c398d7762f5e277919174694293989144c9d25e940d2f66058b2289c75d1b8d0729f9a7c4564404a5fd4313675f85f31b47156068878e236c5635156b0fa21e24346c2041ae42423078577a1413f41375a4d49296ab17910ae214b45155c4570f95ca874ccae9fa80433a1ab453cbb28d780c2f1f4dc7071c93aff3924d76c5b4068a0371dff82531313f281a8acadaa2bd5078d3ddcefcb981f37ff9b8b14c7d9bf1accffe7857160982a2c7d9ee01d3e82265eec9c7401ecc7f02581fd0d912684f42d1b71df87a1ca51515aab4e58fab4da96e154ea6cdfb573a71d81b2ea4a080a1066e1bc3474
print("flag:",long_to_bytes(pow(c,[d for k,d in [(i.p,i.q) for i in continued_fraction_convergents(continued_fraction_iterator(Rational(e,N)))] if k!=0 and not ((e*d-1)%k) and d!=1][0]
,N)).decode(),end="")
'''
Trong đoạn mã này, chúng ta có một số biến và phép tính được thực hiện:
1. Biến `c` là một số nguyên lớn được biểu diễn dưới dạng số hexa.
Đây là thông điệp đã được mã hóa.
2. Hàm `long_to_bytes()` được sử dụng để chuyển đổi số nguyên lớn thành một chuỗi bytes.
Kết quả của hàm này sẽ là thông điệp đã được giải mã.
3. Hàm `pow()` được sử dụng để tính toán phép lũy thừa. 
Trong trường hợp này, nó được sử dụng để giải mã thông điệp đã được mã hóa. 
Cụ thể, nó nhận vào hai đối số: 
`c` là thông điệp đã được mã hóa và `N` là một số nguyên lớn khác.
4. Trong phần cuối cùng của đoạn mã, 
chúng ta có một biểu thức danh sách 
được sử dụng để tính toán giá trị `d` trong phép tính giải mã. 
Đoạn mã này sử dụng các phân số liên tục và phân số hội tụ để tính toán giá trị `d`.
Sau khi giải mã thông điệp, kết quả được chuyển đổi thành chuỗi và in ra màn hình '''