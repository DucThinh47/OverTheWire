# Natas Level 3 → Level 4

Username: natas4

URL: http://natas4.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image19.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image20.png?raw=true)

Xem source page: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image21.png?raw=true)

Xem file wechall.js: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image22.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image23.png?raw=true)

Không tìm được gì. Mở Burp Suite và Intercept refresh page request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image24.png?raw=true)

Dựa vào nội dung được hiển thị trên page: *Access disallowed. You are visiting from "http://natas5.natas.labs.overthewire.org/index.php" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"*, thử sửa Referer header thành *http://natas5.natas.labs.overthewire.org/*: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image25.png?raw=true)

Send request và xem response:  

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image26.png?raw=true)

=> Password natas5: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK


