import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from os import chdir, listdir, path
from tkinter import messagebox as msg, filedialog as fd

from pygame import mixer, display as pydp

pydp.init()


class MusicStore():
    def __init__(self):
        self.conn = sqlite3.connect(path.expanduser("~/Music/hey.db"))
        self.curs = self.conn.cursor()
        self.curs.execute("create table if not exists path (id INTEGER PRIMARY_KEY AUTO_INCREMENT,name TEXT NULL)")
        self.curs.execute("insert into path (id,name) values('1',?)", (path.expanduser("~/Music/"),))

    def getPath(self):
        self.curs.execute("select name from path where id = 1")
        res = self.curs.fetchone()
        return res[0]

    def setPath(self, path):
        self.curs.execute("DELETE FROM path")
        self.curs.execute("insert into path (id,name) VALUES(?,?)", ('1', path))
        self.conn.commit()
        self.conn.close()


class Player(tk.Tk):
    def __init__(self, width=400, height=300, app="MP3"):
        super().__init__()
        self.geometry("{}x{}".format(width, height))
        self.resizable(0, 0)
        self.iconphoto(True, tk.PhotoImage(file="player.png"))
        self.title(app)
        self.configure(cursor="diamond_cross", background="darkgrey")

        mixer.init()
        self.db_data = MusicStore()
        self.drawInterface()
        self.bind("<space>", self.pausePlayMusic)

    def startVisualiser(self, ind=0):
        try:
            img = self.frames[ind]
        except:
            ind = 0
            img = self.frames[ind]
        ind += 1
        self.lbl_img.configure(image=img)
        self.lbl_img.image = img
        self.visualiser_loop = self.lbl_img.after(150, self.startVisualiser, ind)

    def startTimer(self):
        times = mixer.music.get_pos()
        seconds = divmod(times, 1000)
        minutes = 0 if seconds[0] < 60 else seconds[0] // 60
        sec = seconds[0] if seconds[0] < 60 else seconds[0] % 60
        if sec < 0: sec = 0
        sec = sec if sec > 9 else "0" + str(sec)
        minutes = minutes if minutes > 9 else "0" + str(minutes)
        milli = seconds[1] // 10
        milli = milli if milli < 98 else "00"
        timed = f"{minutes}:{sec:2}:{milli:2}"
        self.lbl_time.configure(text=timed)
        self.timer_loop = self.after(10, self.startTimer)

    def stopMusic(self):
        mixer.music.fadeout(1000)
        mixer.music.unload()
        self.btn_play["fg"] = "#fff"
        self.stopTimer()
        self.stopVisualiser()

    def playAll(self):
        self.stopMusic()
        playlist = self.songs.copy()
        self.playMusic(playlist.index(self.currentSong))
        mixer.music.set_endevent(89)
        mixer.music.play()

    def initDir(self, music_path):
        chdir(music_path)
        self.songs = [x for x in listdir() if x.endswith((".mp3", ".wav"))]
        if not len(self.songs):
            msg.showinfo("Songs not found", "No MP3 or WAV file found")
        self.mylist.delete(0, tk.END)
        for num, item in enumerate(self.songs):
            lst = f"{num + 1:>4} -- {item}"
            self.mylist.insert(tk.END, lst)

    def chooseDir(self):
        music_path = fd.askdirectory(title="@Nyeya - Choose a directory", initialdir=path.expanduser("~/Music/"))
        if music_path:
            self.db_data.setPath(music_path)
            self.initDir(music_path)

    def stopTimer(self):
        try:
            self.timer_loop
        except:
            return
        self.after_cancel(self.timer_loop)

    def stopVisualiser(self):
        try:
            self.visualiser_loop
        except:
            return
        self.lbl_img.after_cancel(self.visualiser_loop)

    def playMusic(self, position=None, loop=0):
        self.isPaused = False
        self.btn_play["fg"] = "#c00"

        self.marqueeCount = 5

        def startMarquee():
            if self.marqueeCount >= len(song):
                self.marqueeCount = 5
                self.current_playing["text"] = song[:5]
            self.current_playing["text"] += song[self.marqueeCount]
            self.marqueeCount += 1
            self.marqueeStart = self.current_playing.after(150, startMarquee)

        try:
            mixer.music.stop()
            mixer.music.unload()
            self.stopVisualiser()
        except:
            pass
        try:
            self.current_playing.after_cancel(self.marqueeStart)
        except:
            pass
        if position == None:
            try:
                song_name = self.mylist.get(tk.ACTIVE)
                song = song_name.split(" -- ", 1)
                song = song[1]
            except:
                return
            position = self.songs.index(song)
        else:
            song = self.songs[position]
        self.mylist.selection_clear(0, tk.END)
        self.mylist.select_set(position)
        self.mylist.activate(position)
        self.mylist.see(tk.ACTIVE)
        self.currentSong = song
        try:
            mixer.music.load(song)
        except:
            msg.showinfo("Unsuccessful - @Nyeya [Limitless]", "Cannot load music, file maybe corrupted")
            return
        if len(song) > 8:
            self.current_playing["text"] = song[:5]
            startMarquee()
        self.current_playing["text"] = song
        self.lbl_play_state["text"] = "Now Playing"
        self.lbl_play_state.pack()
        self.lbl_play_state.after(3000, self.lbl_play_state.pack_forget)
        self.startTimer()
        self.startVisualiser(1)
        mixer.music.play(loops=loop, fade_ms=2000)

    def pausePlayMusic(self, event=None):
        try:
            self.isPaused
        except:
            return
        if mixer.music.get_busy() and not self.isPaused:
            mixer.music.pause()
            self.isPaused = True
            self.btn_play["fg"] = "#fff"
            self.stopTimer()
            self.stopVisualiser()
        elif self.isPaused:
            mixer.music.unpause()
            self.startTimer()
            self.startVisualiser()
            self.btn_play["fg"] = "#c00"
            self.isPaused = False
        else:
            return

    def nextMusic(self):
        try:
            index = self.songs.index(self.currentSong)
        except:
            return
        if index >= len(self.songs) - 1:
            currentIndex = 0
        else:
            currentIndex = index + 1
        self.playMusic(currentIndex)

    def prevMusic(self):
        try:
            index = self.songs.index(self.currentSong)
        except:
            return
        if index < 1:
            currentIndex = len(self.songs) - 1
        else:
            currentIndex = index - 1
        self.playMusic(currentIndex)

    def loopOne(self):
        self.playMusic(loop=-1)

    def drawInterface(self):
        outerFrame = tk.Frame(self, bg="#666")
        outerFrame.pack(fill="both", expand=True, padx=5, pady=5)

        playPanel = tk.Frame(outerFrame, bg="#333")
        playPanel.place(relx=2 / 100, rely=2 / 100, relwidth=96 / 100, relheight=30 / 100)

        # *********** PLAY PANEL *********
        timerPane = tk.Frame(playPanel, relief=tk.SUNKEN, bd=4, bg="#333")
        timerPane.place(relx=2 / 100, rely=5 / 100, relwidth=28 / 100, relheight=90 / 100)

        self.lbl_time = tk.Label(timerPane, font="consolas 18", text="00:00:00", bg="#333", fg="white")
        self.lbl_time.pack(fill='x', pady=5)
        self.lbl_play_state = tk.Label(timerPane, justify=tk.LEFT, font="verdana 6", text="", bg="#333", fg="yellow")
        self.lbl_play_state.pack(pady=0)

        self.current_playing = tk.Label(timerPane, font="verdana 10", text="", bg="#333", fg="white")
        self.current_playing.pack(fill='x', pady=5)

        visualPane = tk.Frame(playPanel, relief=tk.GROOVE, bd=4)
        visualPane.place(relx=32 / 100, rely=5 / 100, relwidth=40 / 100, relheight=90 / 100)

        self.frames = [tk.PhotoImage(file="visual.gif", format="gif -index %i" % (i)) for i in range(40)]

        self.lbl_img = tk.Button(visualPane, image=self.frames[0], bg="#F8F8F8")
        self.lbl_img.pack(fill=tk.BOTH, expand=True)

        othersPane = tk.Frame(playPanel, bd=5, background="#666")
        othersPane.place(relx=74 / 100, rely=5 / 100, relheight=90 / 100, relwidth=24 / 100)
        othersPane.columnconfigure([0, 1], weight=1)
        othersPane.rowconfigure([0, 1], weight=1)
        btn_loop_one = tk.Button(othersPane, text="LOOP CURRENT", bg='red', fg="white", command=self.loopOne)
        btn_loop_one.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        # ******************* CONTROL PANEL *******************#
        controlPane = tk.Frame(outerFrame, bg="#333")
        controlPane.place(relx=2 / 100, rely=32 / 100, relwidth=96 / 100, relheight=10 / 100)
        set_btn = {
            "fg": "white",
            "bg": "#333",
            "font": "Roboto 10"
        }
        btn_prev = tk.Button(controlPane, **set_btn, text="PREV", command=self.prevMusic)
        btn_prev.place(relx=1 / 100, rely=15 / 100, relheight=70 / 100, relwidth=8 / 100)

        btn_pause = tk.Button(controlPane, text="||", **set_btn, command=self.pausePlayMusic)
        btn_pause.place(relx=10 / 100, rely=15 / 100, relheight=70 / 100, relwidth=8 / 100)

        self.btn_play = tk.Button(controlPane, text="PLAY", **set_btn, command=self.playMusic)
        self.btn_play.place(relx=19 / 100, rely=15 / 100, relheight=70 / 100, relwidth=8 / 100)

        btn_next = tk.Button(controlPane, **set_btn, text="NEXT", command=self.nextMusic)
        btn_next.place(relx=28 / 100, rely=15 / 100, relheight=70 / 100, relwidth=8 / 100)

        btn_stop = tk.Button(controlPane, **set_btn, text="STOP", command=self.stopMusic)
        btn_stop.place(relx=37 / 100, rely=15 / 100, relheight=70 / 100, relwidth=8 / 100)

        # ********* SCALES *************
        frm_scale_bg = "#333"
        frm_scale = tk.Frame(controlPane, bg=frm_scale_bg)
        frm_scale.place(relx=48 / 100, rely=5 / 100, relwidth=50 / 100, relheight=90 / 100)

        style = ttk.Style()
        style.configure("TScale", background=frm_scale_bg)

        seek_lbl = tk.Label(frm_scale, text="Volume", font="verdana 8", bg=frm_scale_bg, fg="white")
        seek_lbl.pack(side=tk.LEFT)

        self.seek_scale = ttk.Scale(frm_scale, style="TScale", from_=.00001, to=1.0, orient=tk.HORIZONTAL,
                                    command=self.changeVolume)
        self.seek_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.seek_scale.set(mixer.music.get_volume())

        self.lbl_vol_count = tk.Label(frm_scale, text=int(mixer.music.get_volume() * 100), bg=frm_scale_bg, fg="white")
        self.lbl_vol_count.pack(side=tk.LEFT)

        # ******* -------------- PLAY LIST AREA --------------- **********
        playlistArea = tk.Frame(outerFrame, bg="#555", bd=3, relief=tk.SUNKEN)
        playlistArea.place(relx=2 / 100, rely=44 / 100, relheight=54 / 100, relwidth=96 / 100)

        # ** The Playlist headers
        lbl_playlist = tk.Label(playlistArea, text="Your playlist items", fg="white", bg="#955", bd=5, relief=tk.GROOVE)
        lbl_playlist.place(relx=10 / 100, rely=0 / 100, relwidth=50 / 100, relheight=9 / 100)

        btn_playlist = ttk.Button(playlistArea, text="Browse Music", command=self.chooseDir)
        btn_playlist.place(relx=65 / 100, rely=0 / 100, relwidth=25 / 100, relheight=9 / 100)
        # ** The play list box
        playlistPanel = tk.Frame(playlistArea, background="#555")
        playlistPanel.place(relx=10 / 100, rely=10 / 100, relwidth=80 / 100, relheight=90 / 100)

        self.mylist = tk.Listbox(playlistPanel, activestyle="dotbox", selectmode=tk.SINGLE, bg="#000", fg="yellow",
                                 font="Arial 12", bd=0, selectbackground="yellow", selectforeground="black",
                                 relief=tk.FLAT, exportselection=0, cursor="hand2")

        list_scroll_y = ttk.Scrollbar(playlistPanel, command=self.mylist.yview, cursor="dot")

        self.mylist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        list_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.mylist.configure(yscrollcommand=list_scroll_y.set)
        self.initDir(self.db_data.getPath())

    def changeVolume(self, vol):
        new_vol = float(f"{vol:.6}")
        mixer.music.set_volume(new_vol)
        self.lbl_vol_count.configure(text=int(new_vol * 100))


if __name__ == '__main__':
    player = Player(width=550, height=600, app="Nyeya Music Player")
    player.mainloop()
