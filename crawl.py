import requests
from bs4 import BeautifulSoup
import os
import sys
import re

def fetch_examples(problem_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    res = requests.get(problem_url, headers=headers)
    if res.status_code != 200:
        print("페이지를 불러올 수 없습니다.")
        return

    soup = BeautifulSoup(res.text, 'html.parser')

    problem_id_match = re.search(r'/(\d+)', problem_url)
    problem_id = problem_id_match.group(1) if problem_id_match else "unknown"

    # 🔥 여기서 raw string 사용
    inputs = soup.find_all('pre', id=re.compile(r'^sample-input-\d+'))
    outputs = soup.find_all('pre', id=re.compile(r'^sample-output-\d+'))

    os.makedirs(f"problem_{problem_id}", exist_ok=True)

    for i, (input_tag, output_tag) in enumerate(zip(inputs, outputs), start=1):
        input_text = input_tag.get_text().strip()
        output_text = output_tag.get_text().strip()

        with open(f"problem_{problem_id}/input{i}.txt", 'w', encoding='utf-8') as f:
            f.write(input_text)
        with open(f"problem_{problem_id}/output{i}.txt", 'w', encoding='utf-8') as f:
            f.write(output_text)

        print(f"✓ input{i}.txt / output{i}.txt 저장 완료")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("사용법: python crawl.py <문제 URL>")
    else:
        fetch_examples(sys.argv[1])
