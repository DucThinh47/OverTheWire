# Bandit Level 21 → Level 22

Level Goal

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

# Solution

Đăng nhập bandit21: 

![img](116)

Theo mô tả thử thách, truy cập /etc/cron.d và tìm hiểu: 

![img](117)

=> Nội dung của file cronjob_bandit22 cho thấy đây là là một tệp cron job, dùng để thiết lập các tác vụ tự động chạy theo lịch trình. 

- ***@reboot bandit22 /usr/bin/cronjob_bandit22.sh***: Khi hệ thống khởi động lại, bandit22 sẽ chạy script /usr/bin/cronjob_bandit22.sh.

-  ***** bandit22 /usr/bin/cronjob_bandit22.sh: Mỗi phút, user bandit22 sẽ chạy script /usr/bin/cronjob_bandit22.sh.

Truy cập /usr/bin để tìm hiểu file cronjob_bandit22.sh:

![img](118)

=> Tệp cronjob_bandit22.sh là một script Bash (ASCII text executable) chạy theo lịch trình do cronjob_bandit22 đặt trước đó

Trong nội dung file này có: 

- ***cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv***: Ghi nội dung mật khẩu của bandit22 vào tệp /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv.
Do script này được cron chạy mỗi phút, nên tệp /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv sẽ luôn chứa mật khẩu của bandit22.

=> Xem nội dung /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv:

![img](119)

=> Password bandit22: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q