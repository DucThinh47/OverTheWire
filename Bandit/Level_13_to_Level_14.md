# Bandit Level 13 → Level 14

Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

# Solution

Đăng nhập bandit13:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image68.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image69.png?raw=true)

Xem nội dung sshkey.private: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image70.png?raw=true)

Xem trang man ssh và tìm được tùy chọn ***-i***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image71.png?raw=true)

Theo mô tả của đề, user bandit14 sẽ chạy trên localhost, sử dụng lệnh ***ssh bandit14@localhost***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image72.png?raw=true)

=> Không có quyền đăng nhập. Thử dùng lệnh ***ssh -i sshkey.private -p 2220 bandit14@localhost***, lệnh đã thêm khóa xác thực: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image73.png?raw=true)

Đăng nhập thành công bandit14. 

Theo mô tả thử thách, mật khẩu bandit14 nằm ở file /etc/bandit_pass/bandit14: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image74.png?raw=true)

=> Tìm được password bandit14: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

