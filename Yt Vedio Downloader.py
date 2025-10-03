import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import Vedio_downloader_cmd as vdc
import threading

# Create the main application window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("800x600")
root.configure(bg="lightblue")
root.resizable(False, False)

# Add a label to the window
app_name_label = tk.Label(root, text="YouTube Video Downloader", font=("Helvetica", 24) , bg="lightblue")
app_name_label.pack(pady=20)

#Add URL Entry
lable_url = tk.Label(root, text="Enter YouTube Video URL:", font=("Helvetica", 16), bg="lightblue")
url = tk.Entry(root, width=50, font=("Helvetica", 14))
url.pack(pady=20)
lable_url.pack(pady=5)

# Add path Entry
def select_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, selected_path)


path_entry = tk.Entry(root, width=50, font=("Helvetica", 14))
path_entry.pack(pady=20)

label_path = tk.Label(root, text="Select Download Folder:", font=("Helvetica", 16), bg="lightblue")
label_path.pack(pady=1)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 14), command=select_path)
browse_button.pack(pady=5)

# Add a download button
download_button = tk.Button(root, text="Download", font=("Helvetica", 16), bg="green", fg="white")
download_button.pack(pady=20)

#progress bar hook
def progress_hook(d):
    if d['status'] == 'downloading':
        if d.get('total_bytes'):
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            progress_var.set(percent)
            root.update_idletasks()
        elif d.get('total_bytes_estimate'):
            percent = d['downloaded_bytes'] / d['total_bytes_estimate'] * 100
            progress_var.set(percent)
            root.update_idletasks()
    elif d['status'] == 'finished':
        progress_var.set(100)
        root.update_idletasks()

# Download command function 
def download_video():
    video_url = url.get()
    download_path = path_entry.get()
    progress_var.set(0) # Reset progress bar to 0
    if video_url and download_path:
        lable_process = tk.Label(root,text=f"Downloading video from {video_url} to {download_path}")
        lable_process.pack()
        vdc.download_video(video_url, download_path,progress_hook)

    else:
        lable_process = tk.Label(root,text="Please enter a valid URL and select a download folder.")
        lable_process.pack()

# Run download in a separate thread to avoid blocking the GUI
def start_download():
    threading.Thread(target=download_video).start()

download_button.config(command=start_download)

# Add a status bar(To be implemented)
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=400)
progress_bar.pack(pady=10)

lable_progress_bar = tk.Label(root,text="Progress Bar",bg='lightblue')
lable_progress_bar.pack()

# Start the Tkinter event loop
root.mainloop()