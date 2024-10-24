import qrcode


def gerar_qrcode(conteudo, main):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(conteudo)
        qr.make(fit=True)


        img = qr.make_image(fill='black', back_color='white')

        img.save(f"{main}.png")
        print(f"QRcode salvo como {main}.png")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o QR code {e}")


url_ou_texto = input("Digite a url ou texto para geraro QRcode: ")
nome_arquivo= input("Digite o nome do arquivo para salvar o QRCode:  ")
gerar_qrcode(url_ou_texto, nome_arquivo )