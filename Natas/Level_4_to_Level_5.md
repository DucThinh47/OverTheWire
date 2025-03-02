# Natas Level 4 → Level 5

Username: natas5

URL: http://natas5.natas.labs.overthewire.org

# Solution

Truy cập URL:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image27.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image28.png?raw=true)

Xem source page: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image29.png?raw=true)

Xem file wechall.js: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image30.png?raw=true)

Không tìm được gì. Dựa vào nội dung trên page *Access Disallowed. You are not logged in*, có thể liên quan đến cookies. 

Mở Inspect, truy cập phần cookie: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image31.png?raw=true)

Tìm được cookie có tên loggedin đang có value là 0, thử thay value thành 1 và refresh page: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image32.png?raw=true)

=> Pasword natas6: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned

