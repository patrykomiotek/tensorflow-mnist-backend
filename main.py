from flask import Flask, jsonify, render_template, request

# webapp
app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    app.run()
