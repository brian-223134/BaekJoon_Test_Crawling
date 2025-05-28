import requests
from bs4 import BeautifulSoup
import re
import os
import tkinter as tk
from tkinter import messagebox

def fetch_examples_gui(url, status_label):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        res = requests.get(url, headers=headers)
    except Exception as e:
        messagebox.showerror("에러", f"요청 실패: {e}")
        return

    if res.status_code != 200:
        messagebox.showerror("에러", f"요청 실패: 상태코드 {res.status_code}")
        return

    soup = BeautifulSoup(res.text, 'html.parser')

    problem_id_match = re.search(r'/(\d+)', url)
    problem_id = problem_id_match.group(1) if problem_id_match else "unknown"

    inputs = soup.find_all('pre', id=re.compile(r'^sample-input-\d+'))
    outputs = soup.find_all('pre', id=re.compile(r'^sample-output-\d+'))

    if not inputs or not outputs:
        messagebox.showwarning("경고", "예제를 찾을 수 없습니다.")
        return

    os.makedirs(f"problem_{problem_id}", exist_ok=True)

    for i, (input_tag, output_tag) in enumerate(zip(inputs, outputs), start=1):
        input_text = input_tag.get_text().strip()
        output_text = output_tag.get_text().strip()

        with open(f"problem_{problem_id}/input{i}.txt", 'w', encoding='utf-8') as f:
            f.write(input_text)
        with open(f"problem_{problem_id}/output{i}.txt", 'w', encoding='utf-8') as f:
            f.write(output_text)

    status_label.config(text=f"✓ 저장 완료: problem_{problem_id}/")
    messagebox.showinfo("완료", f"예제가 저장되었습니다.\n[problem_{problem_id}] 폴더 확인")

def create_gui():
    root = tk.Tk()
    root.title("Baekjoon 예제 크롤러")
    root.geometry("500x180")
    root.resizable(False, False)

    tk.Label(root, text="문제 URL 입력 (예: https://www.acmicpc.net/problem/1000):").pack(pady=10)

    url_entry = tk.Entry(root, width=60)
    url_entry.pack()

    status_label = tk.Label(root, text="", fg="green")
    status_label.pack(pady=10)

    def on_crawl():
        url = url_entry.get().strip()
        if not url.startswith("http"):
            messagebox.showwarning("입력 오류", "올바른 URL을 입력하세요.")
            return
        status_label.config(text="크롤링 중...")
        root.update()
        fetch_examples_gui(url, status_label)

    tk.Button(root, text="크롤링 시작", command=on_crawl).pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    create_gui()