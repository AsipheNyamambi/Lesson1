status_code = 400

match status_code:
      case 200:
          print('success')
          print('This is a success message. Happy:')
      case 400:
          print('Not Found')
      case 500:
          print('server error')
      case _:
          print('Unknown status')     #The wildcard _" acts as the 'default' case
