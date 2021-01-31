from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def default():
  return render_template('default.html')
 
@app.route('/example1')
def example1():
  return render_template('example1.html')

@app.route('/example2')
def example2():
  return render_template('example2.html')

@app.route('/example3')
def example3():
  return render_template('example3.html')

if __name__ == "__main__":
    app.run()