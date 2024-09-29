# utils/qrcode_generator.py
import qrcode
from io import BytesIO
import base64

def generate_qr_code(data: str) -> str:
    """
    주어진 데이터를 QR 코드로 변환하고 Base64로 인코딩된 이미지를 반환합니다.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 데이터를 메모리 버퍼에 저장
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return img_str
