from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)


@app.route('/')
def career():
    return render_template("career.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      res = result.to_dict(flat=False)
      arr1 = res.values()
      arr = ([value for value in arr1])

      data = np.array(arr)

      data = data.reshape(1,-1)
      #print(data)
      loaded_model = pickle.load(open("career_model_KNN.sav", 'rb'))
      predictions = loaded_model.predict(data)
      #print(predictions)
      jobs_dict = {0: 'Database Developer',
                   1: 'Portal Administrator',
                   2: 'Systems Security Administrator',
                   3: 'Business Systems Analyst',
                   4: 'Software Systems Engineer',
                   5: 'Business Intelligence Analyst',
                   6: 'CRM Technical Developer',
                   7: 'Mobile Applications Developer',
                   8: 'UX Designer',
                   9: 'Quality Assurance Associate',
                   10: 'Web Developer',
                   11: 'Information Security Analyst',
                   12: 'CRM Business Analyst',
                   13: 'Technical Support',
                   14: 'Project Manager',
                   15: 'Information Technology Manager',
                   16: 'Programmer Analyst',
                   17: 'Design & UX',
                   18: 'Solutions Architect',
                   19: 'Systems Analyst',
                   20: 'Network Security Administrator',
                   21: 'Data Architect',
                   22: 'Software Developer',
                   23: 'E-Commerce Analyst',
                   24: 'Technical Services/Help Desk/Tech Support',
                   25: 'Information Technology Auditor',
                   26: 'Database Manager',
                   27: 'Applications Developer',
                   28: 'Database Administrator',
                   29: 'Network Engineer',
                   30: 'Software Engineer',
                   31: 'Technical Engineer',
                   32: 'Network Security Engineer',
                   33: 'Software Quality Assurance (QA) / Testing'}
      print(jobs_dict[predictions[0]])
      job = jobs_dict[predictions[0]]

      return render_template("result.html",result =job)

if __name__ == '__main__':
   app.run(debug = True)