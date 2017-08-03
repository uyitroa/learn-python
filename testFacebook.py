import facebook

at = <my access token>
pid = <my page id>
api = facebook.GraphAPI( at )
args = {'fields' : 'message'}  #requested fields
conv = api.get_object( 'me/conversations')
msg = api.get_object( conv['data'][0]['id']+'/messages')
for el in msg['data']:
    content = api.get_object( el['id'], **args)   #adding the field request
    print content