from flask import Flask, request
from fpdf import FPDF
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Route to handle form data from frontend
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Received data:", data)

    name = data['name']
    email = data['email']
    phone = data['phone']
    business = data['business']

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Business Booster Kit", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"Business: {business}", ln=True)

    pdf_path = f"{name.replace(' ', '_')}_booster_kit.pdf"
    pdf.output(pdf_path)

    # Email setup
    sender_email = "your_email@gmail.com"         # ✅ Your Gmail address
    sender_password = "your_app_password_here"    # ✅ App password (not your Gmail password)

    try:
        msg = EmailMessage()
        msg['Subject'] = "Your Business Booster Kit"
        msg['From'] = sender_email
        msg['To'] = email
        msg.set_content("Attached is your Business Booster Kit.")

        with open(pdf_path, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=pdf_path)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('balamanibalamani452@gmail.com', 'nnrpmjczkhimirtg')
            smtp.send_message(msg)

        print("Email sent successfully to", email)
        return "Booster Kit sent successfully!"

    except Exception as e:
        print("Failed to send email:", e)
        return "Failed to send email.", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
