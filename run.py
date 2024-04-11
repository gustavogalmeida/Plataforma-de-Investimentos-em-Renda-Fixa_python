from app import app

app.config['SECRET_KEY'] = '123'

if __name__ == "__main__":
    app.run(debug=True)