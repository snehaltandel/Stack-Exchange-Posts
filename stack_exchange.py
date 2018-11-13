import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('./data/Stack-Exchange-Posts.xml').getroot()
data = []

for child in e:
    row = child.attrib

    '''Id'''
    try:
        Id = row['Id']
        # print(Id)
    except:
        pass

    '''PostTypeId'''
    try:
        PostTypeId = row['PostTypeId']
        # print(PostTypeId)
    except:
        if 'PostTypeId' not in row:
            PostTypeId = 'NULL'
        pass

    '''ParentId'''
    try:
        ParentId = row['ParentId']
        # print(ParentId)
    except:
        if 'ParentId' not in row:
            ParentId = 'NULL'
        pass

    '''AcceptedAnswerId'''
    try:
        AcceptedAnswerId = row['AcceptedAnswerId']
        # print(AcceptedAnswerId)
    except:
        if 'AcceptedAnswerId' not in row:
            AcceptedAnswerId = 'NULL'
        pass

    '''CreationDate'''
    try:
        CreationDate = row['CreationDate']
        # print(CreationDate)
    except:
        pass

    '''Score'''
    try:
        Score = row['Score']
        # print(Score)
    except:
        pass

    '''ViewCount'''
    try:
        ViewCount = row['ViewCount']
        # print(ViewCount)
    except:
        pass

    '''Body'''
    try:
        Body = row['Body']
        # print(Body)
    except:
        pass

    '''OwnerUserId'''
    try:
        OwnerUserId = row['OwnerUserId']
        # print(OwnerUserId)
    except:
        pass

    '''LastActivityDate'''
    try:
        LastActivityDate = row['LastActivityDate']
        # print(LastActivityDate)
    except:
        pass

    '''Title'''
    try:
        Title = row['Title']
        # print(Title)
    except:
        pass

    '''Tags'''
    try:
        Tags = row['Tags']
        # print(Tags)
    except:
        pass

    '''AnswerCount'''
    try:
        AnswerCount = row['AnswerCount']
        # print(AnswerCount)
    except:
        pass

    '''CommentCount'''
    try:
        CommentCount = row['CommentCount']
        # print(CommentCount)
    except:
        pass

    '''FavoriteCount'''
    try:
        FavoriteCount = row['FavoriteCount']
        # print(FavoriteCount)
    except:
        pass

    '''ClosedDate'''
    try:
        ClosedDate = row['ClosedDate']
        # print(ClosedDate)
    except:
        pass
data.append([Id, PostTypeId, ParentId, AcceptedAnswerId, CreationDate, Score, ViewCount, Body, OwnerUserId, LastActivityDate, Title, Tags, AnswerCount, CommentCount, FavoriteCount, ClosedDate])
print(data)



