from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView

class SuperEditApp(App):
    def build(self):
        return self.root

    def save(self):
        #print("saving")
        #print(self.root.ids)
        data = self.root.ids['tiMain'].text
        #print(data)
        fname = self.root.ids['tiFName'].text
        with open(fname, 'w') as plik:
            plik.write(data)
    
    def load(self):
        print("loading")
        self.fc = FileChooserIconView(path='.')
        self.root.add_widget(self.fc)
        self.fc.bind(on_submit=self.load_tekst)
    

    def load_tekst(self, *positionals):
        #print(positionals)
        fc, fname, *dontcare = positionals
        print(fname[0])
        fname = fname[0]
        # fname = self.root.ids['tiFName'].text
        with open(fname, 'r') as plik:
            data = plik.read()
        
        self.root.ids['tiMain'].text = data
        self.root.remove_widget(self.fc)

    def save_chooser(self):
        print("saving 2")
        self.fc = FileChooserIconView(path='.')
        self.root.add_widget(self.fc)
        self.fc.bind(on_submit=self.save_tekst)

    def save_tekst(self, *positionals):
        fc, fname, *dontcare = positionals
        data = self.root.ids['tiMain'].text
        with open(fname[0], 'w') as plik:
            plik.write(data)
        self.root.ids['tiFName'].text = fname[0]
        self.root.remove_widget(self.fc)




app = SuperEditApp()
app.run()