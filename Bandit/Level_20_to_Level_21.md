# Bandit Level 20 → Level 21

Level Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

# Solution

Đăng nhập bandit20: 

![img](107)

Dùng lệnh ***ls -al***: 

![img](108)

Kiểm tra định dạng file suconnect: 

![img](109)

=> Là một tệp thực thi ELF 32-bit

Thử thực thi file này: 

![img](110)

=> Khi thực thi, file sẽ kết nối đến localhost trên cổng chỉ định. Theo mô tả thử thách, cần cung cấp password bandit20 cho dịch vụ đang chạy trên cổng này và nếu hợp lệ sẽ trả về mật khẩu bandit21. 

=> Cần tạo một server lắng nghe bằng netcat để nhận kết nối và gửi lại mật khẩu bandit21. Mở terminal mới và đăng nhập bandit20:  

![img](111)

Bên terminal còn lại, thực thi file suconnect trên cổng 12345: 

![img](112)

Bên server lắng nghe đã nhận được kết nối: 

![img](113)

=> Nhập mật khẩu của bandit20 và nhận về mật khẩu của bandit21: 

![img](114)

![img](115)

=> Password bandit21: EeoULMCra2q0dSkYj561DX7s1CpBuOBt