# BaekJoon_Test_Crawling
# 📄 Baekjoon Example Crawler

백준(BOJ, [https://www.acmicpc.net](https://www.acmicpc.net)) 문제 페이지에서 입력/출력 예제를 자동으로 크롤링하여  
`input{i}.txt`, `output{i}.txt` 형식으로 저장하는 Python 프로그램입니다.

---

## ✅ 기능 설명

- 백준 문제 URL을 입력받아 해당 문제의 예제 입력/출력을 파싱
- `problem_<문제번호>/` 디렉토리를 생성하고 예제들을 `input1.txt`, `output1.txt`, ... 형태로 저장
- BeautifulSoup을 이용한 HTML 정적 크롤링

---

## 📦 요구 사항

- Python 3.6 이상
- 아래 패키지 설치 필요

```bash
pip install requests beautifulsoup4 pyinstaller
```
---

## 🛠 `.exe` 직접 생성하기 (PyInstaller 사용)

이 프로젝트는 `.exe` 실행 파일을 Git에 포함하지 않으며, 사용자가 직접 빌드해야 합니다.  
아래의 안내에 따라 `dist/` 폴더를 생성하고 실행 파일을 만들 수 있습니다.

### 🚀 .exe 빌드 명령
- 아래의 명령을 terminal에 입력하면 GUI 용 exe 파일이 생성됩니다.
```bash
pyinstaller --onefile --windowed crawl_UI.py
```
---

## 🚀사용 방법

- .exe 빌드 명령 실행 후 아래와 같은 디렉토리 구조로 파일이 생성됩니다:
```bash
project_root/
├── dist/
│   └── crawl_UI.exe     ← 여기서 실행 가능
├── build/
├── crawl_UI.spec
```
- 이후 dist directory에서 .exe 파일을 직접 실행하면 프로그램이 실행됩니다.
- ![image](https://github.com/user-attachments/assets/a3ad4594-496d-49e0-aa2b-6e267e07922d)
- 참고: test case도 exe 파일과 동일한 directory에 생성됩니다.

## 동작 방식
- requests로 HTML을 받아올 때 User-Agent를 설정하여 접근 차단 방지
- BeautifulSoup으로 `<pre id="sample-input-1">`, `<pre id="sample-output-1">` 태그를 추출
- 정규표현식으로 sample-input-\d+, sample-output-\d+을 매칭
- 파일 이름은 문제 번호를 기준으로 problem_<문제번호>/input{i}.txt, output{i}.txt로 저장

## 참고사항
- 문제 구조가 변경되면 정규표현식 부분을 수정해야 할 수 있습니다.
- 예제 개수가 일치하지 않는 경우 (inputN, outputM의 N ≠ M)는 짝이 맞는 개수만 저장됩니다.
- 백준 서버 구조나 robots.txt 정책이 변경되면 작동하지 않을 수 있습니다.
- crawl.py는 non-UI 버전의 crawling 실행 프로그램입니다. (terminal에서 python crawl.py [문제 url] 입력시 동일하게 동작)
