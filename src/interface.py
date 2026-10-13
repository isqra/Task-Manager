import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

collection = ["task_1 | create menu", "task_2 | add main", "task_3 | update main", "task_4 | delete main"]


frame_menu = None
frame_tasks = None
tasks = None

def main():
    global frame_menu, frame_tasks, tasks
    frame_menu = tk.Frame(root, background="grey", width=500, height=500)
    frame_tasks = tk.Frame(root, background="green", width=500, height=500)
    frame_menu.pack_propagate(False)
    frame_tasks.pack_propagate(False)

    button_show_tasks = tk.Button(frame_menu, text="Все задачи", command=show_all_tasks)
    button_show_tasks.pack()

    button_exit = tk.Button(frame_menu, text="Exit", command=create_menu)
    button_exit.pack()
    tasks = tk.Listbox(frame_tasks)
    tasks.pack()

    return frame_menu, frame_tasks

def show_all_tasks():
    frame_menu.pack_forget()
    frame_tasks.pack()

    tasks.delete(0, tk.END)

    for number, content in enumerate(collection):
        word = ''
        for symbol in content:
            if symbol != '|':
                word = f"{word}{symbol}"
            else:
                break
        tasks.insert(tk.END, word)

def create_menu():
    frame_tasks.pack_forget()
    frame_menu.pack()

main()
create_menu()
root.mainloop()
