# curl -i -H "Content-Type: application/json" -X POST -d "{ \"lesson\": [1594663200, 1594666800], \"pupil\": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], \"tutor\": [1594663290, 1594663430, 1594663443, 1594666473] }"  http://localhost:5000/tetrika/api/v1/stat1
# curl -i http://localhost:5000/tetrika/api/v1/stat


from flask import Flask, jsonify, request


def appearance(intervals):
    student = intervals['pupil']
    teacher = intervals['tutor']
    lesson = intervals['lesson']
    summ = 0
    for i in range(0, len(student), 2):
        if student[i] < lesson[0]:
            student[i] = lesson[0]
        if student[i + 1] > lesson[1]:
            student[i + 1] = lesson[1]
        for j in range(0, len(teacher), 2):
            if teacher[j] < lesson[0]:
                teacher[j] = lesson[0]
            if teacher[j + 1] > lesson[1]:
                teacher[j + 1] = lesson[1]
            if student[i] < teacher[j + 1] and student[i + 1] > teacher[j]:
                commontime = min(student[i + 1], teacher[j + 1]) - max(student[i], teacher[j])
                summ += commontime

    return summ


app = Flask(__name__)


@app.route('/tetrika/api/v1/stat', methods=['GET'])
def get_stat():
    testdata = {'lesson': [1594663200, 1594666800],
                'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}

    return jsonify({'Total time': appearance(testdata)})


@app.route('/tetrika/api/v1/stat1', methods=['POST'])
def Help():
    student = request.json['pupil']
    teacher = request.json['tutor']
    lesson = request.json['lesson']
    summ = 0
    for i in range(0, len(student), 2):
        if student[i] < lesson[0]:
            student[i] = lesson[0]
        if student[i + 1] > lesson[1]:
            student[i + 1] = lesson[1]
        for j in range(0, len(teacher), 2):
            if teacher[j] < lesson[0]:
                teacher[j] = lesson[0]
            if teacher[j + 1] > lesson[1]:
                teacher[j + 1] = lesson[1]
            if student[i] < teacher[j + 1] and student[i + 1] > teacher[j]:
                commontime = min(student[i + 1], teacher[j + 1]) - max(student[i], teacher[j])
                summ += commontime
    return jsonify({'Total time': summ})


if __name__ == '__main__':
    app.run(debug=True)
