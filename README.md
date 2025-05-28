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
pip install requests beautifulsoup4
```
---

## 🚀사용 방법

```bash
python crawl.py https://www.acmicpc.net/problem/1000
```

- 실행 후 아래와 같은 디렉토리 구조로 파일이 생성됩니다:
```bash
problem_1000/
├── input1.txt
└── output1.txt
```

- test case가 여러개인 경우
```bash
problem_1000/
├── input1.txt
├── output1.txt
├── input2.txt
└── output2.txt
```

## 동작 방식
- requests로 HTML을 받아올 때 User-Agent를 설정하여 접근 차단 방지
- BeautifulSoup으로 `<pre id="sample-input-1">`, `<pre id="sample-output-1">` 태그를 추출
- 정규표현식으로 sample-input-\d+, sample-output-\d+을 매칭
- 파일 이름은 문제 번호를 기준으로 problem_<문제번호>/input{i}.txt, output{i}.txt로 저장

## 참고사항
- 문제 구조가 변경되면 정규표현식 부분을 수정해야 할 수 있습니다.
- 예제 개수가 일치하지 않는 경우 (inputN, outputM의 N ≠ M)는 짝이 맞는 개수만 저장됩니다.
- 백준 서버 구조나 robots.txt 정책이 변경되면 작동하지 않을 수 있습니다.
