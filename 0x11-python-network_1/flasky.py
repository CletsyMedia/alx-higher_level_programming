from flask import Flask, request

app = Flask(__name__)

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    print(f"Received email: {email}")  # Add this line for debugging
    return f'Your email is: {email}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
