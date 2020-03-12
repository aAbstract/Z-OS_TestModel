

'''
All the callbacks will be implemented in the future version
'''

def onconnect(connection_obj):
	print('[ID]: ' + ' %s '%(connection_obj.id) +  str(connection_obj.address) + ' => ' + 'Applied on Connection Call back done')

def onread(connection_obj,data,sock_list):
	print('Data recived from object ' + connection_obj.id)

def ondisconnect(connection_obj):
	print('client ' + connection_obj.id + ' disconnected')

def onerror(connection_obj):
	print('client ' + connection_obj.id + ' have error occured')
