# Bandit Level 15 → Level 16

Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

# Solution

Đăng nhập bandit15:

![img](78)

Dùng lệnh ***ls -al***: 

![img](79)

Dựa vào mô tả thử thách, cần sử dụng mã hóa SSL/TLS để gửi mật khẩu bandit15 đến dịch vụ cổng 30001 trên localhost. Thử đọc trang man của ***openssl***: 

![img](80)

Tìm được một số tùy chọn có thể hữu ích: 

![img](81)

Khi chạy lệnh ***openssl s_client***, OpenSSL hoạt động như một client SSL/TLS, tức là nó giả lập hành vi của một trình duyệt web hoặc ứng dụng khi kết nối đến một server sử dụng giao thức SSL/TLS.

SSL (Secure Sockets Layer) và TLS (Transport Layer Security) là giao thức bảo mật dùng để mã hóa dữ liệu truyền qua mạng (HTTPS, SMTP, IMAP, v.v.).

Khi một client (trình duyệt, email client) kết nối đến một server qua HTTPS, chúng thực hiện bắt tay TLS (TLS handshake) để thiết lập kết nối an toàn.

OpenSSL s_client giúp kiểm tra và debug quá trình này bằng cách mô phỏng một client kết nối SSL/TLS đến server.

Xem các tùy chọn với s_client bằng lệnh ***openssl s_client -help***: 

![img](82)

=> Sử dụng lệnh ***openssl s_client -connect localhost:30001*** để kết nối đến localhost trên cổng 30001 bằng giao thức SSL/TLS: 

![img](83)

=> Kết nối thành công.

Theo mô tả thử thách, tiếp tục phải gửi password bandit15 để nhận được password bandit16: 

![img](84)

=> Password bandit16: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx