# Bandit Level 22 → Level 23

Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

# Solution

Đăng nhập bandit22: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image120.png?raw=true)

Dựa vào mô tả thử thách, truy cập /etc/cron.d: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image121.png?raw=true)

Đọc nội dung file cronjob_bandit23:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image122.png?raw=true)

=>Một cron job chạy mỗi phút (* * * * *) dưới quyền bandit23, thực thi script /usr/bin/cronjob_bandit23.sh. 

Truy cập và đọc shell /usr/bin/cronjob_bandit23.sh: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image123.png?raw=true)

- *whoami*: lấy tên user hiện tại (trong trường hợp này là bandit23).

- *echo I am user bandit23 | md5sum | cut -d ' ' -f 1*: Tạo một hash MD5 dựa trên chuỗi "I am user bandit23", chỉ lấy phần hash.

- Sao chép mật khẩu từ /etc/bandit_pass/bandit23 vào tệp /tmp/<md5_hash>.

Thử tìm tên tệp chứa mật khẩu: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image124.png?raw=true)

=> Tên tệp chứa mật khẩu: /tmp/8ca319486bfbbc3663ea0fbe81326349

Đọc nội dung tệp này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image125.png?raw=true)

=> Mỗi phút, script của bandit23 chạy và lưu mật khẩu vào một file trong /tmp/ với tên là MD5 của chuỗi "I am user bandit23".
Có thể tính toán MD5 này, rồi đọc file tương ứng để lấy mật khẩu.

=> Password bandit23: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga




