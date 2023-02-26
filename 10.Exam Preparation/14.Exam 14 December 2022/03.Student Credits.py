def students_credits(*args):
    courses = {}
    output = []
    for info in args:
        info = info.split('-')
        course_name = info[0]
        credits = int(info[1])
        max_test_points = int(info[2])
        diyans_points = int(info[3])

        diyans_percentage = diyans_points / max_test_points * 100
        diyans_credits = credits * diyans_percentage / 100
        courses[course_name] = diyans_credits

    total_credits = 0

    for course, scores in courses.items():
        total_credits += scores

    if total_credits >= 240:
        output.append(f'Diyan gets a diploma with {total_credits:.1f} credits.')
    else:
        output.append(f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.')
    sorted_result = sorted(courses.items(), key=lambda kvpt: -kvpt[1])
    for course, points in sorted_result:
        output.append(f"{course} - {points:.1f}")
    return '\n'.join(data for data in output)
