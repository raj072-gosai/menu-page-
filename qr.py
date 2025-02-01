import qrcode

wifi_details = "WIFI:T:WPA;S:Raj;P:12345678;;"
redirect_url = "http://192.168.144.50:5500/menu.html"

# Combine Wi-Fi details and redirect URL
qr_data = wifi_details + "URL:" + redirect_url

# Generate the QR code
qr = qrcode.make(qr_data)
qr.save("wifi_menu_qr.png")
