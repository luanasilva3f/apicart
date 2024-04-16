from flask import Flask, request, jsonify
import qrcode
import base64
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

@app.route('/api/gerar_qrcode', methods=['GET'])
def gerar_qrcode():
    # Recebe a carteira de criptomoeda dos parâmetros da URL
    carteira = request.args.get('carteira')

    # Verifica se a carteira foi fornecida
    if not carteira:
        return jsonify({'error': 'É necessário fornecer a carteira de criptomoeda'}), 400

    # Gera o QR code
    qr = qrcode.make(carteira)

    # Converte o QR code para base64
    buffer = BytesIO()
    qr.save(buffer, format='JPEG')
    qr_base64 = base64.b64encode(buffer.getvalue())

    # Retorna o resultado em formato JSON com o prefixo data URI
    return jsonify({'base64': f'data:image/jpeg;base64,{qr_base64.decode("ascii")}'})

if __name__ == '__main__':
    app.run(debug=True)
