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
    #print(Title)
    # RealInput = request.cookies.get("title","..")
    # print(RealInput)
    return render_template(
        "def.html", 
        NameTitle = WholeTitle.Correspond,
        NumTitle = WholeTitle.Array,
        NameContent = WholeContent.ContentTitle,
        NumContent = WholeContent.ContentNum,
        PosContent = WholeContent.ContentPos        
    )
    
@search.route('/search',methods=["GET","POST"])
def Search():
    sel = request.form.get("sel")
    print(sel)
    Title = request.form.get("title","default")
    #print(Title)
    #return f"<html>{Title}</html>"
    if sel == "content" :
        Title = ""
    if sel == "title":
        Content = ""
    if Title != "": 
        InputText = Title
        print(InputText)
        WholeTitle.procedureTitle(Title)
        #return f"<html>{WholeTitle.Correspond[0]}{WholeTitle.Array[0]}<br>{WholeTitle.Correspond[1]}{WholeTitle.Array[1]}<br>{{WholeTitle.Correspond[0]}}{WholeTitle.Array[2]}</html>"
        #TitleList = WholeTitle.Display()
    Content = request.form.get("content","default")
    #return f"<html>{Content}</html>"
    if Content !="":
        InputText = Content
        WholeContent.procedureContent(Content)
        # return f"<html>{WholeContent.ContentTitle[0]}{WholeContent.ContentNum[0]}{WholeContent.ContentPos[0]}<br>{WholeContent.ContentTitle[1]}{WholeContent.ContentNum[1]}{WholeContent.ContentPos[1]}<br>{WholeContent.ContentTitle[2]}{WholeContent.ContentNum[2]}{WholeContent.ContentPos[2]}</html>"
        #ContentList = WholeContent.Display()
    # return redirect(url_for("index"))
    return render_template(
        "def.html", 
        NameTitle = WholeTitle.Correspond,
        NumTitle = WholeTitle.Array,
        NameContent = WholeContent.ContentTitle,
        NumContent = WholeContent.ContentNum,
        PosContent = WholeContent.ContentPos,
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
    print(DicCopy)
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
    #print(DicCopy)
    #data = json.dumps(DicCopy, ensure_ascii=False, indent=4, separators=(',', ':'))
    #return f"<html>{Dic[WholeTitle[0]]}</html>"
    return render_template(
        "Arrange.html",
        NameTitle =  WholeTitle.Correspond[idx],
        order = Dic[WholeTitle.Correspond[idx]]
    )
  
if __name__ == "__main__":
    search.run(debug=True)