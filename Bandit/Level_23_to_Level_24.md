# Bandit Level 23 → Level 24

Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

# Solution: 

Đăng nhập bandit23: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image126.png?raw=true)

Theo mô tả thử thách, truy cập /etc/cron.d: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image127.png?raw=true)

Đọc nội dung file cronjob_bandit24: 

![img](128)

Dựa vào nội dung file, truy cập và đọc nội dung shell /usr/bin/cronjob_bandit24.sh:

![img](129)

Phân tích: 

- Script di chuyển vào thư mục /var/spool/bandit24/foo.
- Thực thi mọi file trong đó nếu file thuộc về bandit23.
- Sau khi chạy, file sẽ bị xóa

Do bandit23 có quyền ghi vào /var/spool/bandit24/foo, nên có thể:

- Tạo một shell script, đặt tên là myscript.sh để đọc mật khẩu bandit24

- Đặt script vào /var/spool/bandit24/foo

- Chờ cronjob chạy và thực thi script

![img](130)

=> Password bandit24: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8


