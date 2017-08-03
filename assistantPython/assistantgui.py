import wx
import wikipedia
import wolframalpha
import webbrowser

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="I'm your assistant, what do you want?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        inputcommand = ['/open']
        command = ['webbrowser.open(data)']
        if input[0] != "/":
            try:
                #wolframalpha
                app_id = "AGRKJV-22W7HUGYXG"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print answer
            except:
                #wikipedia
                print wikipedia.summary(input)
        else:
            for x in range(len(inputcommand)):
                if inputcommand[x] in input:
                    separe = input.split(" ")
                    data = separe[1]
                    exec(command[x])
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()