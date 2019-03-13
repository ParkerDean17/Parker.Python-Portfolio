# Parker Dean
# Baseball Tracker
# 3/7/19

from tkinter import *
import tkinter.ttk as ttk


class Game(object):
    def __init__(self, name, oteam, atbats, hits, walks, strikeouts, rbis, onbase):
        self.name = name
        self.oteam = oteam
        self.atbats = atbats
        self.hits = hits
        self.walks = walks
        self.strikeouts = strikeouts
        self.rbis = rbis
        self.onbase = onbase

    def __str__(self):
        x = "Player was " + str(self.name)
        return x


class Application(Frame):
    """ Gui application which counts button clicks."""
    def __init__(self,master):
        """ Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.games = []

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # Create instruction label
        self.inst_lbl = Label(self, text="Player Name")
        self.inst_lbl.grid(row=0, column=0, sticky=W)
        # Create entry widget to get name
        self.pname_ent = Entry(self)
        self.pname_ent.grid(row=0, column=1, sticky=W)
        # Create instruction label
        self.team_lbl = Label(self, text="Opposing Team")
        self.team_lbl.grid(row=0, column=2, sticky=W)
        # Create widget for opposing team names
        oteams = ["Hurricane", "Sky View", "Cedar City", "Ben Lohmond", "Bonneville", "Ogden", "Park City", "Stansbury", "Juan Diego"]
        self.teamname_ent = ttk.Combobox(root, values=oteams)
        self.teamname_ent.grid(row=0, column=3, sticky=N)
        # create label for at bats
        self.bats_lbl = Label(self, text="At bats")
        self.bats_lbl.grid(row=1, column=0, sticky=W)
        self.num_bats = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_bats.grid(row=1, column=1, sticky=W)
        # create label for hits
        self.hits_lbl = Label(self, text="Hits")
        self.hits_lbl.grid(row=2, column=0, sticky=W)
        self.num_hits = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_hits.grid(row=2, column=1, sticky=W)
        # create label for walks
        self.walks_lbl = Label(self, text="Walks")
        self.walks_lbl.grid(row=3, column=0, sticky=W)
        self.num_walks = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_walks.grid(row=3, column=1, sticky=W)
        # create label for Strikeouts
        self.strikeouts_lbl = Label(self, text="Strikeouts")
        self.strikeouts_lbl.grid(row=4, column=0, sticky=W)
        self.num_strikeouts = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_strikeouts.grid(row=4, column=1, sticky=W)
        # create label for RBI's
        self.rbis_lbl = Label(self, text="RBI's")
        self.rbis_lbl.grid(row=5, column=0, sticky=W)
        self.num_rbis = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_rbis.grid(row=5, column=1, sticky=W)
        # create label for OBS
        self.ob_lbl = Label(self, text="On Base")
        self.ob_lbl.grid(row=6, column=0, sticky=W)
        self.num_ob = Spinbox(self, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        self.num_ob.grid(row=6, column=1, sticky=W)
        # create button to save stats
        self.bttn1 = Button(self)
        self.bttn1["text"] = "Save game stats"
        self.bttn1["command"] = self.save_game
        self.bttn1.grid(row=7, column=0, sticky=W)

    def save_game(self):
        name = self.pname_ent.get()
        opteam = self.teamname_ent.get()
        atbats = self.num_bats.get()
        num_hits = self.num_hits.get()
        num_walks = self.num_walks.get()
        num_strikeouts = self.num_strikeouts.get()
        num_rbis = self.num_rbis.get()
        num_ob = self.num_ob.get()
        game = Game(name, opteam, atbats, num_hits, num_walks, num_strikeouts, num_rbis, num_ob)
        self.games.append(game)
        print(game)


# main
root = Tk()
root.title("Baseball Tracker")
root.geometry("1000x500")
app = Application(root)
root.mainloop()