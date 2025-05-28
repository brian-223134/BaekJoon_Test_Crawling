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
