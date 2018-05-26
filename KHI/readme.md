##오픈 소스 기여
### 환경 준비
- WSL
  -[설치 과정 블로그](https://joojy.net/p/20171224581)

### Tools
- Visual Studio Code
- git
```bash
$ sudo apt-get instal git git-core
```
- code Triage
- github
- try git

#3월 9일
conemu
sudo apt-get install git git-core tig

https://www.codetriage.com/
projects.apache.org/projects.html
https://opensource.google.com/

UBUNTU(좋음) vs Windows WSL(i/o가 구림, 설치가 안되는 것들이 있음) vs Docker on windows vs Virtual Machine vs bare-metal linux

1. 프로젝트를 찾기
2. 빌드 방법 찾기, 문서 찾기
3. 빌드 후에 이슈들 확인하기
4. 이슈 해결하기
**처음에 해결할 때는, 재현이 가능한 오류인지 반드시 확인
재현이 힘들면 버리는게 좋습니다.**

git -
add
commit
------- local
push
------- remote

thttps://try.github.io/levels/1/challenges/6 꼭 해보세요
https://learngitbranching.js.org/

1. cd /mnt/c/
2. mkdir prj-001
3. cd prj-001
4. git clone 
5. cd ----


mkdir A
cd A
readme.md
git status
git add 
git config --global user.name "Hyun il Kim"
git config --global user.email "gusdlf93@naver.com"
git commit -m "Initial Commit"
git push origin master

git remote add upstream (URL)
git fetch upstream
git branch -a
//origin/master, upstream/master
git merge upstream/master  //로컬에 반영
git log
git push origin master

컨플릭이 발생하면, 같은 파일을 수정한 사람이 있단 것.
pr취소하고, 

#3월 17일

https://opensource.guide/ko/
https://www.codetriage.com/

효과 주기
#
##
-    .
-    .
```  xxx ```
[]
* xxx *
>
>>
>>>


Language
>C++  - Tensorflow

>Python - ansible

>C# - django

>java - spring


Application
>Android
>Window
>Linux

Server
Engine
>Spring
>WebServer 

System
 >Ansible
 >Jenkis
 >Cloud 

Media
 >ffmpeg
 >GStreamer

Script
> bash

#프로그램 찾을 때 중요한 것 :
>1. Document가 얼마나 깔끔한지
>2. 업데이트가 최근에 (1~2개월 정도) 되었어 야함<지속적인 개발>
>3. 실행이 편해야 함.

#Google Summer Code
>https://summerofcode.withgoogle.com/
여기서 프로젝트 찾아도 좋습니다.

#반드시 지켜야 할 것
>코딩 스타일 
>http://jongwook.kim/google-styleguide/trunk/cppguide.xml

> Line은 80자 안에서
> tap은 설정을 따로해서, 스페이스 2번이나 4번으로 변경되게 해줘야함
> 오픈소스에서 if(&&) 혹은 if(if())뭘 선호하는지, 알고 그대로 적용해줘야함

{
  "workbench.iconTheme" :
  "editor.insertSpaces":
  "editor.tabSize":4,
  "editor.detectIndentation" : 
}

#Trygit & Learning git branch
>언젠가 해보기

#Map 
#Unordered Map
#red-black tree
나중에 한번 찾아보기

>>>GeeksforGeeks 좋은 알고리즘 사이트입니다.