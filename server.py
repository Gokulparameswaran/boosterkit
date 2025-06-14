from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import base64

app = Flask(__name__)
CORS(app)

@app.route('/send-pdf', methods=['POST'])
def send_pdf():
    data = request.get_json()
    pdf_base64 = data['pdf']
    email_to = data['email']

    # Decode the PDF
    pdf_data = base64.b64decode(pdf_base64.split(',')[1])

    # Prepare email
    msg = EmailMessage()
    msg['Subject'] = 'Your Business Booster Kit'
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = email_to
    msg.set_content('Hello,\n\nHere is your Business Booster Kit report.\n\nBest,\nBooster Team')

    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='booster-kit.pdf')

    # Send email using Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('balamanibalamani452@gmail.com', 'nnrpmjczkhimirtg')
            smtp.send_message(msg)
        return jsonify({'status': 'sent'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
