from flask import Flask, request, render_template_string

app = Flask(__name__)

# Insecure template rendering (XSS)
@app.route("/")
def home():
    name = request.args.get("name", "")
    html = f"<h1>Welcome {name}</h1>"  # XSS vulnerability
    return render_template_string(html)

# Insecure headers (ZAP will detect)
@app.after_request
def remove_security_headers(response):
    response.headers.pop('X-Frame-Options', None)
    response.headers.pop('X-Content-Type-Options', None)
    response.headers.pop('Content-Security-Policy', None)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

