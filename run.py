from app import create_app
import os

app = create_app()

print('Current working directory:', os.getcwd())
print('Templates dir exists:', os.path.exists('templates/form.html'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 