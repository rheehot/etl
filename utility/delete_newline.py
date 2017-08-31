'''
delete_newline.py ‘데이터파일명’ ‘줄 별 구분자 개수’ ‘구분자’ > 출력파일명
※ SOH 구분자로 입력하려면 커맨드라인에서 [Ctrl]+[v]+[a] 입력
'''

import sys
reload(sys)

f = open(sys.argv[1], 'r')
delimiter_count = int(sys.argv[2])
delimiter = sys.argv[3] # command line에서 입력
# delimiter = '\x01' # 구분자: SOH 문자
count = 0
temp_string = ''

while True:
    line = f.readline()

    count = 0

    if not line:
        break
    else:
        # print line
        for letter in line:
            if letter == delimiter:
                count += 1
        if count == delimiter_count:
            if temp_string != '':
                print temp_string
                temp_string = ''

            line = line.replace('\n', '')
            print line
        else:
            line = line.replace('\r\n', '')
            line = line.replace('\n', '')
            temp_string += line
#while

f.close()
