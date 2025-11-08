from win10toast_click import ToastNotifier
import webbrowser
#pip install win10toast-click
#notify.py
def on_click(url):
    print("Thông báo đã được nhấp!")
    webbrowser.open(url)  # Mở trình duyệt tới URL

toaster = ToastNotifier()

def show_notification(msg,url):
    toaster.show_toast(
        "Thông báo từ Python",
        "Nhấn vào đây để mở trang web\n" + msg,
        icon_path=None,  # Có thể dùng icon .ico nếu muốn
        duration=10,
        threaded=True,
        callback_on_click=lambda: on_click(url)

    )

# Giữ chương trình chạy cho đến khi thông báo biến mất
import time
while toaster.notification_active():
    time.sleep(0.1)
