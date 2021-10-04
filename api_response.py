import requests
r = requests.get('https://jsonplaceholder.typicode.com/users')
status = r.status_code
print('get ==> '+ str(status))

data = {'Username':'corey','password':'testing'}
r = requests.post('https://httpbin.org/post', data=data)
status = r.status_code
print('post ==> '+ str(status))

r = requests.put('https://httpbin.org/put', data=data)
status = r.status_code
print('put ==> '+ str(status))

r = requests.delete('https://httpbin.org/delete',data=data)
status = r.status_code
print('delete ==> '+ str(status))

j = r.json()
print('Username is: '+j['form']['Username'])
print('Password is: '+j['form']['password'])
