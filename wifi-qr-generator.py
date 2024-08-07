import wifi_qrcode_generator as qr

def generate_wifi_qr(ssid, password, auth_type):
    """
    Generate a QR code for WiFi access.
    :param ssid: SSID of the WiFi network
    :param password: Password of the WiFi network
    :param auth_type: Authentication type (WPA, WPA2, WEP, or nopass)
    """
    qr_code = qr.wifi_qrcode(ssid, hidden=False, authentication_type=auth_type, password=password)
    img = qr_code.make_image(fill='black', back_color='white')
    file_name = f"wifi_qr_{ssid}.png"
    img.save(file_name)
    print(f"WiFi QR code generated and saved as '{file_name}'.")

if __name__ == "__main__":
    ssid = "***"
    password = "***"
    auth_type = "WPA"
    generate_wifi_qr(ssid, password, auth_type)