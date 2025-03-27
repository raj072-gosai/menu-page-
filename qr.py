import qrcode

redirect_url = "http://192.168.58.25/menu.php?table_number=4"

# Combine Wi-Fi details and redirect URL
qr_data =  redirect_url

# Generate the QR code
qr = qrcode.make(qr_data)
qr.save("menu_qr_4.png")
