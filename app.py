# Imports
from flask import (Flask,
                   redirect,
                   url_for,
                   request,
                   render_template)
import mysql.connector
import json

app = Flask(__name__,template_folder="templates")


# Connecting to Sql

@app.route('/')
def version():
  config = {
      'user': 'root',
      'password': 'root',
      'host': 'db',
      'port': '3306',
      'database': 'Employee'
  }
  try:
      connection = mysql.connector.connect(**config)
      cursor = connection.cursor()
      db_Info = connection.get_server_info()
      cursor.close()
      connection.close()
      return "Connected to MySQL Server {}".format(db_Info)+"<br>"+"If you want to insert users to MySQL, access with /insert"
  except:
      return "Oops!! Unable to Connect to MySQL DB"

@app.route("/home", methods=['GET','POST'])
def home():
  config = {
      'user': 'root',
      'password': 'root',
      'host': 'db',
      'port': '3306',
      'database': 'Employee'
  }

  # Post request
  if request.method == "POST":


      # Get Data from Form
      name = request.form['name']
      job = request.form['job']
      salary = request.form['salary']

      # Insert into employee Table
      addEmployee = ("INSERT INTO employee "
            "(name, job, salary) "
            "VALUES (%(name)s, %(job)s, %(salary)s)")

      dataEmployee = {
          'name': name,
          'job': job,
          'salary': salary,
      }
      connection = mysql.connector.connect(**config)
      cursor = connection.cursor()
      cursor.execute(addEmployee,dataEmployee)
      connection.commit()

  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()
  getEmployees = "select * from employee"
  cursor.execute(getEmployees)
  AllEmployees = cursor.fetchall()


  # Render Home Page
  return render_template('home.html',allEmployees=AllEmployees)



# Delete Method
@app.route("/delete", methods=['POST'])
def delete():
  config = {
      'user': 'root',
      'password': 'root',
      'host': 'db',
      'port': '3306',
      'database': 'Employee'
  }

  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()

  # Get ID from form
  id_ = (request.form['id'],)
  # Delete From employee Table
  deleteEmployee = """ Delete from employee where id = %s """
  cursor.execute(deleteEmployee,id_)
  connection.commit()

  # Redirect to Home page
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True)
