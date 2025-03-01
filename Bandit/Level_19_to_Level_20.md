# Bandit Level 19 → Level 20

Level Goal

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

# Solution

Đăng nhập bandit19:

![img](101)

Dùng lệnh **ls**: 

![img](103)

=> bandit20-do là một tệp thực thi ELF 32-bit. Đồng thời, nó có setuid (SUID) – có nghĩa là khi chạy chương trình này, nó thực thi với quyền của chủ sở hữu file, thay vì người chạy.

Thử thực thi file bằng lệnh ***./bandit20-do***: 

![img](104)

=> Chương trình cho phép chạy một lệnh dưới quyền của user khác.

Thử chạy lệnh id: 

![img](105)

=> euid=11020(bandit20), nghĩa là chương trình thực thi với quyền của bandit20

Theo mô tả thử thách, mật khẩu bandit20 nằm ở /etc/bandit_pass: 

![img](106)

=> Password bandit20: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO


