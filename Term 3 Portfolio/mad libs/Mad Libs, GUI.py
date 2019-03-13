# Parker Dean
# 3/11/19

from tkinter import *


class Application(Frame):
    def __init__(self,master):
        """ Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # Create instruction label
        self.noun_ent = Label(self, text="Enter a noun: ")
        self.noun_ent.grid(row=1, column=0, sticky=W)
        # Create entry widget to accept password
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=1, column=1, sticky=W)
        # Create entry widget to accept password

        self.num_ent = Label(self, text="Enter a Number: ")
        self.num_ent.grid(row=2, column=0, sticky=W)

        self.num_ent = Entry(self)
        self.num_ent.grid(row=2, column=1, sticky=W)

        self.rel_ent = Label(self, text="Enter a Relative: ")
        self.rel_ent.grid(row=3, column=0, sticky=W)

        self.rel_ent = Entry(self)
        self.rel_ent.grid(row=3, column=1, sticky=W)

        Label(self,
              text = "Adjectives(s): "
              ).grid(row=4, column=0, sticky=W)

        self.hit = BooleanVar()
        Checkbutton(self,
                    text="Hit",
                    variable=self.hit,
                    ).grid(row=4, column=1, sticky=W)

        self.ignore = BooleanVar()
        Checkbutton(self,
                    text="ignore",
                    variable=self.ignore,
                    ).grid(row=4, column=2, sticky=W)

        self.destroy = BooleanVar()
        Checkbutton(self,
                    text="Destroy",
                    variable=self.destroy,
                    ).grid(row=4, column=3, sticky=W)

        self.second_adj = StringVar()
        self.second_adj.set(None)

        second_adj = ["kill", "love", "screw"]
        column = 1
        for adj in second_adj:
            Radiobutton(self,
                        text=adj,
                        variable=self.second_adj,
                        value=adj
                        ).grid(row=5, column=column, sticky=W)
            column += 1

        # create submit button
        Button(self,
               text = "Click for story",
               command = self.tell_story,
               ).grid(row=6, column=0, sticky=W)

        # display the story
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=5)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        noun = self.noun_ent.get()
        number = self.num_ent.get()
        relative = self.rel_ent.get()
        adjectives = ""
        if self.hit.get():
            adjectives += "hit, "
        if self.ignore.get():
            adjectives += "ignore, "
        if self.destroy.get():
            adjectives += "destroy, "
        second_adj = self.second_adj.get()

        #create the story
        story = "Yesterday I got wicked pissed when a snowplow hit my"
        story += noun
        story += " for the"
        story += number
        story += "-th time. I told the driver that he could go"
        story += second_adj
        story += " himself and I was going to"
        story += adjectives
        story += " his"
        story += relative
        story += "Long story short, I need bail money."

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
# main
root = Tk()
root.title("Mad Libs")
root.geometry("750x500")
app = Application(root)
root.mainloop()