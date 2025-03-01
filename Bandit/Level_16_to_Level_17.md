# Bandit Level 16 → Level 17

Level Goal

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

# Solution

Đăng nhập bandit16: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image85.png?raw=true)

Theo mô tả thử thách, sử dụng lệnh ***nmap localhost -p31000-32000*** để quét dịch vụ đang chạy trên những cổng mở từ 31000 đến 32000: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image86.png?raw=true)

=> Những cổng đang mở là: 31046,31518,31790,31960

Tiếp theo cần tìm cổng nào lắng nghe kết nối SSL/TLS. Thử cổng 31046: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image87.png?raw=true)

=> Không phải. Tiếp theo thử cổng 31518: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image88.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image89.png?raw=true)

=> Không trả lại gì khi cung cấp password bandit315. Tiếp theo, thử cổng 31790: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image90.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image91.png?raw=true)

=> Không trả về password bandit17. Tiếp theo, thử cổng 31960: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image92.png?raw=true)

=> Việc sử dụng openssl để tạo kết nối SSL/TLS không được. Thử sử dụng netcat bằng lệnh ***ncat --ssl localhost 31790**, ncat là một bản nâng cấp của nc, cho phép kết nối đến cổng 31790 bằng SSL/TLS: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image93.png?raw=true)

=> Nhập password bandit16 và nhận được ssh private key để kết nối đến bandit17. 

    -----BEGIN RSA PRIVATE KEY-----
    MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
    imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
    Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
    DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
    JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
    x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
    KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
    J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
    d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
    YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
    vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
    +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
    8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
    SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
    HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
    SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
    R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
    Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
    R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
    L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
    blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
    YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
    77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
    dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
    vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
    -----END RSA PRIVATE KEY-----

Lưu khóa này vào file /tmp/sshkey_bandit17. Sau đó cấp quyền cho file này bằng lệnh ***chmod 600 /tmp/sshkey_bandit17*** vì SSH yêu cầu quyền file chỉ chủ sở hữu mới được đọc/ghi. Nếu không, bị từ chối truy cập.

Sau đó dùng lệnh ***ssh -i /tmp/sshkey_bandit17 -p 2220 bandit17@localhost*** để kết nối đến bandit17: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image94.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image95.png?raw=true)

=> Kết nối thành công đến bandit17. 

Thử thách này phải kết nối đến bandit17 bằng private key chứ không có password. 
