from flask import Flask, request, jsonify
from math import gcd
from functools import reduce
import google.generativeai as genai

app = Flask(__name__)

# CONFIGURATION - Put your API Key between the quotes below
genai.configure(api_key="AIzaSyBLYtfy9pNL6IZYwlw6yRRrj1tH65wy1wo")
model = genai.GenerativeModel('gemini-1.5-flash')
MY_EMAIL = "l1881.be23@chitkara.edu.in"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"is_success": True, "official_email": MY_EMAIL}), 200

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json
        res = None
        if 'fibonacci' in data:
            n, a, b = data['fibonacci'], 0, 1
            res = []
            for _ in range(n): res.append(a); a, b = b, a + b
        elif 'prime' in data:
            res = [x for x in data['prime'] if x > 1 and all(x % i for i in range(2, int(x**0.5) + 1))]
        elif 'lcm' in data:
            res = reduce(lambda a, b: abs(a*b) // gcd(a, b), data['lcm'])
        elif 'hcf' in data:
            res = reduce(gcd, data['hcf'])
        elif 'AI' in data:
            response = model.generate_content(data['AI'] + " One word only.")
            res = response.text.strip()
        return jsonify({"is_success": True, "official_email": MY_EMAIL, "data": res}), 200
    except:
        return jsonify({"is_success": False}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
