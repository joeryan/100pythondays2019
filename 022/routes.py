from app import app


@app.route('/')
@app.index('/index')
def index():
    return "Hello world!"