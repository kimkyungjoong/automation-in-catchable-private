import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import os
import sys

# 실행 파일의 경로 설정 (PyInstaller 환경 대응)
def get_script_path():
    if getattr(sys, 'frozen', False):  # .app 또는 .exe 실행 환경
        base_path = sys._MEIPASS  # PyInstaller 환경
    else:  # 일반 Python 실행 환경
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    # PyInstaller 환경에서는 포함된 파일이 _MEIPASS 내부에 위치
    script_path = os.path.join(base_path, "로그인 후 캐치페이 결제.py")

    if not os.path.exists(script_path):
        messagebox.showerror("오류", f"파일을 찾을 수 없습니다: {script_path}")
    
    return script_path

# 자동화 코드 실행 함수
def run_automation():
    script_path = get_script_path()

    if not os.path.exists(script_path):
        return

    try:
        # subprocess 실행 (Python3 사용, 절대 경로 지정)
        subprocess.run(["/usr/bin/python3", script_path], check=True)
        messagebox.showinfo("완료", "자동화 작업이 성공적으로 완료되었습니다!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("오류", f"자동화 작업 중 오류 발생: {e}")

# GUI 생성
def create_gui():
    window = tk.Tk()
    window.title("자동화 프로그램")
    window.geometry("400x300")

    # 안내 텍스트
    label = tk.Label(window, text="캐테 베타 자동화 실행기", font=("Arial", 16))
    label.pack(pady=20)

    # 실행 버튼 (스레드 사용)
    run_button = tk.Button(
        window, text="실행", font=("Arial", 12),
        command=lambda: threading.Thread(target=run_automation).start()
    )
    run_button.pack(pady=10)

    # 종료 버튼
    exit_button = tk.Button(
        window, text="종료", font=("Arial", 12),
        command=window.quit
    )
    exit_button.pack(pady=10)

    window.mainloop()

# GUI 실행
if __name__ == "__main__":
    create_gui()




#  파이썬 코드를 .app 패키지에 포함 시켜서 넣어야 app에서 작동됨