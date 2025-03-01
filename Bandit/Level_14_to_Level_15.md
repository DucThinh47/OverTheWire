# Bandit Level 14 → Level 15

Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost. 

# Solution

Đăng nhập bandit14: 

![img](75)

Dựa vào mô tả thử thách, cần gửi password bandit14 đến localhost trên cổng 30000. Thử sử dụng nmap để quét dịch vụ nào đang mở trên cổng 30000: 

![img](76)

Thử kết nối đến cổng 30000 trên localhost bằng lệnh ***nc localhost 30000***: 

![img](77)

=> Dịch vụ trên cổng 30000 có thể đang chờ nhận dữ liệu, cung cấp mật khẩu bandit14 như mô tả của thử thách và nhận được mật khẩu của bandit15: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo


