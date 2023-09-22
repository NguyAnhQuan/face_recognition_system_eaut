from tkinter import Tk

# Tạo cửa sổ gốc
root = Tk()
root.title("Thay đổi biểu tượng")

# Đường dẫn đến file ảnh .ico mới
new_icon_path = "1face.ico"  # Thay thế bằng đường dẫn tới ảnh .ico mới

# Đặt biểu tượng mới cho cửa sổ gốc
root.iconbitmap(new_icon_path)

# Hiển thị cửa sổ
root.mainloop()
