import qrcode


# -------------- FUNCTION/CLASS -------------- #
name = "qrcode-nubank-youtube"
language = "pt-br"
baptism_of_fire = name + "-" + language + ".png"

# -------------- ORIGINAL LINK -------------- #
original_link = "00020126950014BR.GOV.BCB.PIX0136df533973-ccbd-45c6-ba03-8fd43ccfe06f0233Muito obrigado pela contribuição!5204000053039865802BR5925ANDERSON MARCOS DIAS CANT6009SAO PAULO61080540900062070503***6304253E"

# -------------- bitly LINK -------------- #
bitly_link = original_link

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
