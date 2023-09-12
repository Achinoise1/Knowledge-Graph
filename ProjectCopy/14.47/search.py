import json
from flask import(
    Flask,request,render_template, url_for,redirect,g
)
from matplotlib.pyplot import title
import WholeContent
import WholeTitle

search = Flask(__name__)
InputText = ""
Choice = 0

@search.route('/',methods=["GET","POST"])
def index(): 
    return render_template(
        "def.html",
        NameTitle = ["","",""],
        NumTitle = [0,0,0],
        NameContent = ["","",""],
        NumContent = [0,0,0],
        PosContent = [["",""],["",""],["",""]],
        title = "",
        content = "",
        sel = ""      
    )

@search.route('/search',methods=["GET","POST"])
def Search():
    sel = request.form.get("sel")
    Title = request.form.get("title","default")
    Content = request.form.get("content","default")
    
    CorList = ["","",""]
    AList = [0,0,0]
    TList = ["","",""]
    NList = [0,0,0]
    PList = [["",""],["",""],["",""]]
    SearchInfo = []
    
    if sel == "choice":
        Title = ""
        CorList = ["","",""]
        AList = [0,0,0]
        Content = ""
        TList = ["","",""]
        NList = [0,0,0]
        PList = [["",""],["",""],["",""]]
        
    if sel == "content" :
        Title = ""
        CorList = ["","",""]
        AList = [0,0,0]
        
    if sel == "title":
        Content = ""
        TList = ["","",""]
        NList = [0,0,0]
        PList = [["",""],["",""],["",""]]

    if Title != "": 
        InputText = Title
        print(InputText)
        SearchInfo = WholeTitle.procedureTitle(Title)
        CorList = SearchInfo[0]
        AList = SearchInfo[1]

    if Content !="":
        InputText = Content
        SearchInfo = WholeContent.procedureContent(Content)
        TList = SearchInfo[0]
        NList = SearchInfo[1]
        PList = SearchInfo[2]

    return render_template(
        "def.html", 
        NameTitle = CorList,
        NumTitle = AList,
        NameContent = TList,
        NumContent = NList,
        PosContent = PList,
        title = Title,
        content = Content,
        sel = sel
    )

@search.route('/content/<int:idx>',methods=["GET","POST"])
def PresentC(idx):
    with open("./templates/a.json",encoding='utf-8') as data:
        Dic = json.load(data)
    DicCopy = {}
    DicCopy.update({WholeContent.ContentTitle[idx]:Dic[WholeContent.ContentTitle[idx]]})
    data = json.dumps(DicCopy, ensure_ascii=False, indent=4, separators=(',', ':'))
    
    return render_template(
        "Arrange.html",
        NameTitle =  WholeContent.ContentTitle[idx],
        order = Dic[WholeContent.ContentTitle[idx]]
    )


@search.route('/title/<int:idx>',methods=["GET","POST"])
def PresentT(idx):
    with open("./templates/a.json",encoding='utf-8') as data:
        Dic = json.load(data)
    DicCopy = {}
    DicCopy.update({WholeTitle.Correspond[idx]:Dic[WholeTitle.Correspond[idx]]})
    
    return render_template(
        "Arrange.html",
        NameTitle =  WholeTitle.Correspond[idx],
        order = Dic[WholeTitle.Correspond[idx]]
    )
  
if __name__ == "__main__":
    search.run(debug=True)