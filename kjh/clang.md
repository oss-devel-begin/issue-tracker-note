# Clang 설치 실패 기록

## 공통사항
 1. Clang 공식 사이트에서 Clang 다운로드
 2. Clang 실행 결과 각각의 파일에 대해서는 정적분석 가능 확인
 3. godot의 경우 c와 cpp, py 가 모두 있는 프로그램을 SCons로 패키징.
 4. 다양한 파일들을 동시에 확인하고 싶을 경우 scan-build 명령어를 사용해야함.

## Windows
 1. Clang 공식 사이트에서 미리 컴파일된 실행파일로 설치(Pre-Built Binaries)
 2. 설치 후 scan-build 실행 결과 perl 추가 설치 필요 확인
 3. Strawberry Perl 설치
 4. scan-build가 정상적으로 움직임을 확인하였으나 scan-build는 make 파일에 대해서는 작동하지만 SConstruct에는 작동하지 않는 것 같음.

## Ubuntu 1차
 1. Clang 공식 사이트에서 LLVM 압축파일 설치
 2. 압축 해제 이후 진행방식을 알 수가 없음.

## Ubuntu 2차
 1. sudo apt install 커맨드를 통해 Clang, LLVM 등 설치
 2. scan-build 작동하지 않음

## Ubuntu 2차
 1. [Clang 공식 사이트의 지시사항](http://clang.llvm.org/get_started.html)에 따라 설치
 2. scan-build가 작동하지 않음
