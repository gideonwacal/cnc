from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# ======= Mail Configuration =======
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gideonwacal33@gmail.com'       # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'fdkf dcnj kbnk dqkd'          # Replace with your App Password

mail = Mail(app)

# ======= Routes =======
@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if not name or not email or not subject or not message:
        flash("All fields are required. Please fill in everything.")
        return redirect('/')

    # Send Email
    try:
        msg = Message(subject=f"New Contact: {subject}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['gideonwacal33@gmail.com'])  # where the message will be sent

        msg.body = f"""A new client has sent you a message:

        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        """

        mail.send(msg)
        flash("Your message has been sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        flash("Failed to send email. Please try again later.")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
