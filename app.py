from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Engineer',
        'location': 'Los Angeles, CA',
        'salary': '$100000'
    },
    {
        'id': 2,
        'title': 'S/W Engineer',
        'location': 'SF, CA',
        # 'salary': '$200000'
    },
    {
        'id': 3,
        'title': 'Cybersec Engineer',
        'location': 'New York, NY',
        'salary': '$50000'
    },
    {
        'id': 4,
        'title': 'Data Analyst',
        'location': 'Ohio',
        'salary': '$100000'
    },
    {
        'id': 5,
        'title': 'SWE Engineer',
        'location': 'Portland, OR',
        # 'salary': '$300000'
    }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='M&M careers')


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
