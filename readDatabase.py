import json
import watson_developer_cloud
import pandas
import codecs

D = pandas.read_excel('file.xls')

for i in range(0,len(D)):
    conversation = watson_developer_cloud.ConversationV1(
        username= D['user'][i],
        password=D['password'][i],
        version=''
    )

    response = conversation.get_workspace(
        workspace_id=D['workspace_id'][i],
        export=True,
    )

    company = D['company'][i]
    path = D['path'][i] + '/' + company + '.json'
    F = codecs.open(path,'w','utf-8')
    F.write(json.dumps(response, indent=2))
    F.close()

