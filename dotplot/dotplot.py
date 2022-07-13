import qrcode


# -------------- FUNCTION/CLASS -------------- #
name = "dotplot"
language = "pt-br"
baptism_of_fire = name + "-" + language + ".png"

# -------------- ORIGINAL LINK -------------- #
original_link = "https://colab.research.google.com/drive/1X-GOVrOwP5tN3-c9yyfmiin0K-BvcywB?usp=sharing"

# -------------- bitly LINK -------------- #
bitly_link = "https://bit.ly/dot_plot"

# -------------- Creating inbstance for qrcode -------------- #
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# -------------- Adding the link -------------- #
qr.add_data(bitly_link)

# -------------- Making the qrcode -------------- #
qr.make(fit=True)

# -------------- Exporting the qrcode -------------- #
img = qr.make_image(fill_color="black", back_color="white")
img.save(baptism_of_fire)
