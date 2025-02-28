# Bandit Level 3 → Level 4

Level Goal

The password for the next level is stored in a hidden file in the inhere directory.

Đăng nhập bandit3: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image9.png?raw=true)

Dùng lệnh ***ls***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image10.png?raw=true)

=> Không tìm được gì. Thử dùng lệnh ***ls -al*** để liệt kê đầy đủ hơn: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image11.png?raw=true)

=> Tìm được file ..Hiding_From_You. Thử xem nội dung file này bằng lệnh ***cat '...Hiding_From_You'***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image12.png?raw=true)

=> Tìm được password cho bandit4: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
