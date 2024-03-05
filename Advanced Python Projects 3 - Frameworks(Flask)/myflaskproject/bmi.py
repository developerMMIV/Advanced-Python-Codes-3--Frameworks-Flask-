from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def bmi_calculator():
  return render_template("bmi.html")

@app.route("/calculate", methods=["POST"])
def calculate_bmi():
  weight = float(request.form["weight"])
  height = float(request.form["height"])

  if height == 0:
    return "Error: Height cannot be zero"

  bmi = weight / (height * height)
  bmi_category = get_bmi_category(bmi)
  return render_template("result.html", bmi=bmi, bmi_category=bmi_category)

def get_bmi_category(bmi):
  """
  This function defines BMI categories based on the provided value.
  You can customize these ranges and labels as needed.
  """
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

if __name__ == "__main__":
  app.run(debug=True)
