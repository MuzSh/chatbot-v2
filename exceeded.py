values = {
    'error': {
        'message': 'You exceeded your current quota, please check your plan and billing details.',
        'type': 'insufficient_quota',
        'param': None,
        'code': None
    }
}
# response =  'You exceeded your current quota, please check your plan and billing details.'

keyWords = ['exceeded', 'quota']
response = values["error"]["message"]
if any(word in str(response) for word in keyWords):
    print("No More. Please contact your administrator for more information!")