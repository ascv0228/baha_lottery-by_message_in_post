import requests
import collections

def get_requests(messageId,nextPage = 1):
    head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = f'https://wall.gamer.com.tw/app/v1/comment_detail.php?messageId={messageId}&nextPage={nextPage}'
    return requests.get(url, headers = head)

def get_user_list(totalPage,messageId,commentCount):
    user_list = []
    for i in range(totalPage):
        res = get_requests(messageId,i+1)
        for j in range(15):
            if(i*15+j<commentCount):
                user_list += ["%-5d %-20s %-20s"%(i*15+j+1,res.json()['comments'][j]['userid'],res.json()['comments'][j]['name'])]
            else:
                break
    return user_list

def output_screen(user_list):
    for i in user_list:
        print(i)

def output_file(filename,user_list):
    with open(filename, 'w',encoding= 'utf-8') as fo:
        for i in user_list:
            fo.write(str((i+"\n").encode('utf-8').decode('utf-8')))

####################################################################
def get_user_dict(totalPage,messageId,commentCount):
    user_dict = collections.OrderedDict()
    for i in range(totalPage):
        res = get_requests(messageId,i+1)
        for j in range(15):
            if(i*15+j<commentCount):
                user_dict["%-20s"%res.json()['comments'][j]['userid']] = "%-20s"%res.json()['comments'][j]['name']
            else:
                break
    return user_dict

def output_dict_screen(user_dict):
    user_num = 1
    for i in user_dict.keys():
        print("%-5d %-20s %-20s"%(user_num,i,user_dict[i]))
        user_num += 1

def output_dict_file(filename,user_dict):
    user_num = 0
    with open(filename, 'w',encoding= 'utf-8') as fo:
        for i in user_dict:
            user_num += 1
            #fo.write(str(("%-5d %-20s %-20s\n"%(user_num,i,user_dict[i])).encode('utf-8').decode('utf-8')))
            print(str(("%-5d %-20s %-20s\n"%(user_num,i,user_dict[i])).encode('utf-8').decode('utf-8')), file = fo)

if __name__ == "__main__":
    #messageId = int(input('Message ID : '))
    messageId = 16252831
    res = get_requests(messageId)
    totalPage = res.json()['totalPage']
    commentCount = res.json()['commentCount']
    
    isrepeat = input('允許重複 : (Y/N)')
    if (isrepeat in ['Y','y','yes','Yes','YES']):
        user_list = get_user_list(totalPage,messageId,commentCount)
        output_screen(user_list)
        output_file('D:/web crawler/lottery.txt',user_list)
    elif (isrepeat in ['N','n','no','No','NO']):
        user_dict = get_user_dict(totalPage,messageId,commentCount)
        output_dict_screen(user_dict)
        output_dict_file('D:/web crawler/lottery.txt',user_dict)
    else:
        assert 0 , "keyboardError"
