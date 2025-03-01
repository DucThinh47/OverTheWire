# Bandit Level 20 → Level 21

Level Goal

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

# Solution

Đăng nhập bandit20: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image107.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image108.png?raw=true)

Kiểm tra định dạng file suconnect: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image109.png?raw=true)

=> Là một tệp thực thi ELF 32-bit

Thử thực thi file này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image110.png?raw=true)

=> Khi thực thi, file sẽ kết nối đến localhost trên cổng chỉ định. Theo mô tả thử thách, cần cung cấp password bandit20 cho dịch vụ đang chạy trên cổng này và nếu hợp lệ sẽ trả về mật khẩu bandit21. 

=> Cần tạo một server lắng nghe bằng netcat để nhận kết nối và gửi lại mật khẩu bandit21. Mở terminal mới và đăng nhập bandit20:  

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image111.png?raw=true)

Bên terminal còn lại, thực thi file suconnect trên cổng 12345: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image112.png?raw=true)

Bên server lắng nghe đã nhận được kết nối: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image113.png?raw=true)

=> Nhập mật khẩu của bandit20 và nhận về mật khẩu của bandit21: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image114.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image115.png?raw=true)

=> Password bandit21: EeoULMCra2q0dSkYj561DX7s1CpBuOBt