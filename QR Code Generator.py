import qrcode
import urllib.parse

upi_id = input("Enter your UPI ID = ")
name = input("Enter your Name = ")
amount = input("Enter Amount = ")
message = input("Enter Message = ")

# Encode text properly (IMPORTANT)
name = urllib.parse.quote(name)
message = urllib.parse.quote(message)

# Correct UPI URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={message}"

print("Generated UPI URL:", upi_url)  # Debug

# Generate QR
qr = qrcode.make(upi_url)

# Save & show
qr.save("upi_qr.png")
qr.show()

print("✅ QR Code Generated Successfully!")