#-*- coding: utf-8 -*-
import Levenshtein as lev

# import easyocr
# import numpy as np
# import cv2
# import random
# import matplotlib.pyplot as plt
# import os
# from PIL import ImageFont, ImageDraw, Image
# import natsort
# beforeResult=[]
# textResult=[]
# textAfterResult=[]
#
# tmpResult=[]
#
#
# img = cv2.imread("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")
# im=Image.open("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")
#
# w,h=im.size
# tmph=(int)(h*0.75)
# dst=img[tmph:h,0:w].copy()
#
#
# reader = easyocr.Reader(['ko', 'en'], gpu=False)
# result = reader.readtext("C:/Users/iwsl1/CNN_Contents_Analytics/tesa.JPG")
#
# # for i in range(0,len(result)):
# #     if result[i]
#
# for i in range(0,len(result)):
#     beforeResult.append(str(result[i][1]))
# for i in range(0,len(result)):
#     if not ((result[i][0][0][0]>0 and result[i][0][0][0]<w) and (result[i][0][0][1]) > tmph and (result[i][0][0][1] < h)
#     and (result[i][0][1][0]>0 and result[i][0][1][0]<w) and (result[i][0][1][1]) > tmph and (result[i][0][1][1] < h)
#     and (result[i][0][2][0]>0 and result[i][0][2][0]<w) and (result[i][0][2][1]) > tmph and (result[i][0][2][1] < h)
#     and (result[i][0][3][0]>0 and result[i][0][3][0]<w) and (result[i][0][3][1]) > tmph and (result[i][0][3][1] < h)):
#         continue
#     print(result[i][1])
#     textResult.append(str(result[i][1]))
#
# #원본
# print(beforeResult)
#
# #자막 부분만 자른부분
# print(textResult)
#
# before=""
# for i in range(0,len(textResult)):
#     before+=textResult[i]
# print(before)

tmptest=[]
print("whiy")
# test=[' ', ' 경기 고양시의 커피전문점_', ' 경기 고양시의 커피전문점', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' ', ' 몇몇은 마스크틀 턱에 걸쳐습니다.', ' 몇몇은 마스크v 턱에 걸젊습니다.', ' ', ' 카페 주인이 4명까지만 이용할 수 있다며나가라고 하자 언성이 높아집니다.', ' 카페 주인이 4명까지만 이용할 수 있다며나가라고 하자 언성이 높아집니다.', ' 카페 주인이 4명까지만 이용할 수 있다며나가라고 하자 언성이 높아집니다.', ' 카페 주인이 4명까지만 이용할 수 있다며나가라고 하자 언성이 높아집니다.', ' 카페 주인이 4명까지만 이용할 수 있다며나가라고 하자 언성이 높아집니다.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' 포개서 앉켓다는 것도 거부당하자 한 남성이 욕설올 내뱉습니다.', ' 조개서 앉켓다는 것도 거부당하자 한 남성이 욕설올 내뱉습니다.', ' 조개서 완켓다는 것도 거부당하자 한 남성이 욕설올 내뱉습니다.', ' 조개서 완켓다는 것도 거부당하자 한 남성이 욕설올 내뿌습니다.', ' 포개서 앉켓다는 것도 거부당하자 한 남성이 욕설올 내백습니다.', ' ', ' ', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' ', ' 업주와 말다툼올 벌인 일행은 곧 카페름 떠낫습니다.', ' 업주와 말다툼올 벌인 일행은 곧 카페름 떠낫습니다.', ' 업주와 말다툼올 벌인 일행은 곧 카페름 떠낫습니다.', ' 업주와 말다툼올 벌인 일행은 곧 카페름 떠낫습니다:', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 앉젯다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 앉켓다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 안켓다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 안젯다고 해 실랑이름 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주논 3주 전에도 비슷한 일행이 찾아와여럿이 안젯다고 해 실랑이름 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주논 3주 전에도 비슷한 일행이 찾아와여럿이 안젯다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 앉켓다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' 남성들올 경찰에 신고한 업주는 3주 전에도 비슷한 일행이 찾아와여럿이 앉켓다고 해 실랑이틀 벌인 적이 있다고 주장햇습니다.', ' ', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것뿐인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요밥식 요료때냐', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것뿐인데 왜저한E 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요합선대화음식 으로때냐', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것뿐인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요합썹대화음실 :류때냐', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것뿐인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요합썹대화음실 하류때냐', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것분인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것분인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것분인데 왜저한데 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요', ' 제가 틀린 말을 한 것도 아니고 방역수칙올 지키고자 한 것분인데 왜저한테 그렇게 말을 하시논지 도무지 이해가 안 돼서 제보하게 뒷어요', ' 남성들이 입고 있던 조끼에는 민주노총 건설노조라고 적혀 있없습니다.  ', ' 남성들이 입고 잇당 조끼에눈 민주노총 건설노조라고 적혀 있엇습니다.', ' 남성들이 입고 있던 조끼에는 민주노총 건설노조라고 적혀 있없습니다.', ' 남성들이 입고 있당 조끼에는 민주노총건설소조라고 적혀 있/습니다 .', ' 남성들이 입고 있도 조끼에눈 민주노총건설소조라고 적혀 있어습니다 .', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지는확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다:', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만, 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 이에 대해 건설노조 혹은 CCTV 속 손님들이 실제 노조원인지논확실하지 않지만 자체적으로 진상을 파악하켓다고 밝혀습니다.', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침을 교육하도록 논의하켓다고 약속햇습니다', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침을 교육하도록 논의하켓다고 약속햇습니다.', ' 또 대신 업주에계 사과한다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침하 교육하도록 논의하켓다고 약속햇습니다.', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침을 교육하도록 논의하켓다고 약속햇습니다.', ' 또 대신 업주에계 사과한다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침을 교육하도록 논의하켓다고 약속햇습니다.', ' 또 대신 업주에게 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침하 교육하도록 논의하켓다고\'약속해습나다: "', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침흘교육하도록 논의하켓다고 약속해습니다-"', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침올교육하도록 논의하켓다고 약속해습나다. "', ' 또 대신 업주에계 사과하다면서 노조원들로 확인되면 다중이용시설에서지켜야 할 방역 지침을 교육하도록 논의하켓다고 약속햇습니다.', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거듭 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거듭 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거듭 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거논 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거듭 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거논 논의하고 있어요', ' 저희 나름으로는 방역 수칙은 꼭 지켜야켓다는 지침 내리고교육하는 거논 논의하고 있어요', ' ', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반켓논지와모욕 형의름 적용할 수 있는지 조사한다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반켓논지와모욕 형의름 적용할 수 있는지 조사한다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반켓논지와모욕 형의름 적용할 수 있는지 조사하다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반해는지와모욕 형의름 적용할 수 있는지 조사한다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반쾌논지와모욕 형의름 적용할 수 있는지 조사한다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반쾌논지와모욕 형의름 적용할 수 있는지 조사한다는 방침입니다.', ' 경찰은 남성들의 신원올 파악해 방역 수칙올 위반쾌논지와모욕 현의름 적용할 수 있는지 조사한다는 방침입니다.', ' YTN 박희재입니다.', ' YTN 박희재입니다.', ' ', ' 자막뉴스 제작 | 이 선 에디터', ' 자막뉴스 제작 | 이 선 에디터', ' ']
result=[]
test=[' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.', ' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.',' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.',' 남색 조끼름 입은 남성 9명이 카페로 들어갑니다.',' 몇몇은 마스크틀 턱에 걸쳐습니다.', ' 몇몇은 마스크v 턱에 걸젊습니다.']


visited=[False]*len(test)

for i in range(0,len(test)-1):
    for j in range(i+1,len(test)-1):
        if(lev.ratio(test[i],test[j])<0.8):
            break
        else:
            if(lev.ratio(test[i],test[j])>0.8 ):
                visited[j] = True

print(visited)


