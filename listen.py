import asyncio
import websockets
import json
import tkinter as tk
from tkinter import simpledialog
import pandas as pd

class ActionDialog(simpledialog.Dialog):
    def __init__(self, parent, actions):
        self.actions = actions
        super().__init__(parent)
        
    def body(self, master):
        tk.Label(master, text="Select or create an action:" ).grid(row=0, column=0, sticky=tk.W)
        font = ('Helvetica', 12)
        
        self.listbox = tk.Listbox(master, font=font, height=5, width=50)
        self.listbox.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)
        for action in self.actions:
            self.listbox.insert(tk.END, action)
        
        self.entry = tk.Entry(master, font = font, width=50)
        self.entry.grid(row=2, column=0, sticky=tk.W+tk.E)
        
        return self.listbox
    
    def apply(self):
        selection = self.listbox.curselection()
        if selection:
            self.result = self.actions[selection[0]]
        else:
            self.result = self.entry.get()
            if self.result:
                self.actions.append(self.result)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.actions = self.load_actions()
        self.df = pd.DataFrame(columns=['url', 'selected_html', 'rendered_html', 'action'])

    def open_popup(self, data):
        dialog = ActionDialog(self.root, self.actions)
        action = dialog.result
        if action:
            print("Selected Action:", action)
            new_row = pd.DataFrame([[data['url'], data['outerHTML'], action]], 
                                columns=['url', 'selected_html', 'action'])
            with open('data.csv', 'a') as f:
                new_row.to_csv(f, header=False, index=False)

        self.save_actions()

    def load_actions(self):
        try:
            with open('actions.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_actions(self):
        with open('actions.json', 'w') as file:
            json.dump(self.actions, file, indent=4)

    async def websocket_server(self, websocket, path):
        async for message in websocket:
            print("Received:", message)
            data = json.loads(message)
            self.open_popup(data)

    async def run_server(self):
        server = websockets.serve(self.websocket_server, 'localhost', 5000)
        await server

app = App()

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(app.run_server())
    print("WebSocket server started")
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    app.save_actions()
    loop.close()
