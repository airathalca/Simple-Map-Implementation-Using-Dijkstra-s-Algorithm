from tkinter import *
from tkinter import filedialog as fd
from dijkstra import *
from time import perf_counter

def solve():
    global iterationnumber
    global D
    global window
    tStart = perf_counter()
    text.delete("1.0","end")
    path, dist, iter = D.dijkstra(src_node.get(), dest_node.get())
    if (dist < INT_MAX):
        tStop = perf_counter()
        text.insert("2.0", "Iterations = " + str(iter) + "\nWaktu Eksekusi = " + str("{:.6f}".format(tStop-tStart)) + " sekon\n")
        text.insert("3.0", "Shortest path = {0}\n".format(print_path(list(path))))
        text.insert("4.0", "Distance = " + str(dist))
        text.tag_add("tag_name", "1.0", "end")
    else:
        text.insert("5.0", "Path tidak ditemukan")
        text.tag_add("tag_name", "1.0", "end")

def select_file():
    global D
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    D = Graph(filename)
    options = [node for node in D.nodes]
    src_drop = OptionMenu(window, src_node, *options)
    src_drop.place(x=300, y = 144)
    src_drop.config(width = 17)
    dest_drop = OptionMenu(window, dest_node, *options)
    dest_drop.place(x=300, y = 202)
    dest_drop.config(width = 17)

#create window
window = Tk()
window.title("Dijkstra Application")
window.geometry("600x400")
window.configure(background='dark slate gray')

#create label for title
Label(text="Dijkstra Geming",bg = 'dark slate gray', fg = 'white', font = ("Comic Sans MS", "24")).pack()

#create button for open file
open_button = Button(text='Open a File',fg = 'white', bg = 'slate gray', command=select_file)
open_button.place(x=300, y = 95)
open_button.config(width = 20)

src_node = StringVar()
dest_node = StringVar()
src_node.set("source node")
dest_node.set("destination node")
src_text = Label(text="Source: ",bg = 'dark slate gray', fg = 'white', font = ("Comic Sans MS", "9"))
src_text.place(x=300, y = 122)
src_drop = OptionMenu(window, src_node, "Source Node")
src_drop.place(x=300, y = 144)
src_drop.config(width = 17)
dest_text = Label(text="Destination: ",bg = 'dark slate gray', fg = 'white', font = ("Comic Sans MS", "9"))
dest_text.place(x=300, y = 180)
dest_drop = OptionMenu(window, dest_node, "Destination Node")
dest_drop.place(x=300, y = 202)
dest_drop.config(width = 17)

#create solve button to solve 15 puzzle
solvebutton = Button(text = 'Solve\nUsing\nDijkstra', fg = 'white', bg = 'slate gray', font = ("Comic Sans MS", "13"), command = solve)
solvebutton.config(width = 10, height = 5)
solvebutton.place(x=460, y = 95)

#create text for constraint etc.
text=Text(bg = 'dark slate gray', font = ("Comic Sans MS", "10"))
text.tag_configure("tag_name", justify='left')
text.config(width = 33, height = 7)
text.place(x=300, y = 240)

window.mainloop()