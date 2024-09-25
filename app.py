from flask import Flask
import redis

app = Flask(__name__)

# Configure Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def hello_world():
    redis_client.set('hello', 'world')

    message = redis_client.get('hello').decode('utf-8')

    return f'Hello, {message}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

