# Bandit Level 13 → Level 14

Level Goal

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

# Solution

Đăng nhập bandit13:

![img](68)

Dùng lệnh ***ls -al***: 

![img](69)

Xem nội dung sshkey.private: 

![img](70)

Xem trang man ssh và tìm được tùy chọn ***-i***: 

![img](71)

Theo mô tả của đề, user bandit14 sẽ chạy trên localhost, sử dụng lệnh ***ssh bandit14@localhost***:

![img](72)

=> Không có quyền đăng nhập. Thử dùng lệnh ***ssh -i sshkey.private -p 2220 bandit14@localhost***, lệnh đã thêm khóa xác thực: 

![img](73)

Đăng nhập thành công bandit14. 

Theo mô tả thử thách, mật khẩu bandit14 nằm ở file /etc/bandit_pass/bandit14: 

![img](74)

=> Tìm được password bandit14: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

