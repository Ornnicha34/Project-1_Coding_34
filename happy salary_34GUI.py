import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณโบนัส
def calculate_bonus():
    try:
        salary = float(entry_salary.get())
        years_worked = int(entry_years.get())

        if years_worked <= 5:
            bonus = salary * 0.05
        elif years_worked <= 10:
            bonus = salary * 0.10
        else:
            bonus = salary * 0.15

        messagebox.showinfo("ผลลัพธ์", f"จำนวนเงินโบนัส: {bonus:.2f} บาท")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณโบนัส")
root.geometry("300x200")

# สร้าง Label และ Entry สำหรับกรอกเงินเดือน
tk.Label(root, text="เงินเดือน:").pack(pady=5)
entry_salary = tk.Entry(root)
entry_salary.pack(pady=5)

# สร้าง Label และ Entry สำหรับกรอกจำนวนปีที่ทำงาน
tk.Label(root, text="จำนวนปีที่ทำงาน:").pack(pady=5)
entry_years = tk.Entry(root)
entry_years.pack(pady=5)

# ปุ่มคำนวณโบนัส
btn_calculate = tk.Button(root, text="คำนวณโบนัส", command=calculate_bonus)
btn_calculate.pack(pady=10)

# เริ่มต้นโปรแกรม
root.mainloop()