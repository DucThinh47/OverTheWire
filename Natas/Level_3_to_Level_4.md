# Natas Level 3 → Level 4

Username: natas4

URL: http://natas4.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](19)

![img](20)

Xem source page: 

![img](21)

Xem file wechall.js: 

![img](22)

![img](23)

Không tìm được gì. Mở Burp Suite và Intercept refresh page request: 

![img](24)

Dựa vào nội dung được hiển thị trên page: *Access disallowed. You are visiting from "http://natas5.natas.labs.overthewire.org/index.php" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"*, thử sửa Referer header thành *http://natas5.natas.labs.overthewire.org/*: 

![img](25)

Send request và xem response:  

![img](26)

=> Password natas5: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK


