import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)

    if response.ok:
        todos = response.json()
        completed_tasks = []
        total_tasks = len(todos)
        for todo in todos:
            if todo['completed']:
                completed_tasks.append(todo['title'])

        employee_name = todos[0]['userId']
        print("Employee {} is done with tasks({}/{})".format(employee_name, len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task))
    else:
        print("Error: {}".format(response.status_code))

