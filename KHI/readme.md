
- Schedule -

#5.5  - 커널 컨트리뷰션
#5.12 - 휴강
#5.19 - 외식 (장소는 정자역, 강남 양자 택일)
#5.26 - linux - next

#정적 분석툴 2개
- cppcheck
- clang

정적분석툴로 살펴볼것들
- unused variable
- memory leek : malloc free

### keras 분석 정리 하세요
Contributting 분석 정리에 따라서 error를 발견할 확률이 높아짐.

1. 잘못된 api 사용에 의한 경고나코멘트
2. 정적 분석툴로 나온 데이터에 대해서 해결 해보기
- 브랜치 만들어서 거기다가 적용

#documentation에 어떤 조합으로 쓰면 문제가 발생하는지
code의 사용법을 이런 조합으로 사용해야 한다라는 것을 만들어서 보내면 좋겠습니다.
사용하면 안되는 조합들을 올려줘도 좋을 거 같습니다.

# linux - kernel 
1) 글자가 한줄에 xx자 이상일 때, 
2) 초기화가 안되어있으면 return시에 garbage가 리턴되서 문제가 발생합니다.

절대 git push origin 쓰지마세요
git fetch origin입니다 push쓰면 한세월걸려요

HW.현재 어떤 방향으로 진행중인지하고, 포커싱 결과들에 대해서 전체적으로 플로우 차트 하나 만들어서 올리기

###naver smtp 서버 사용법 알아오세욥###
pop3