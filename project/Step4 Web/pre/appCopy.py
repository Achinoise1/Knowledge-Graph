from flask import (
    Flask, request, render_template
)
import jieba
import WholeContent
import WholeTitle

app = Flask(__name__)


def bi_tokenize(s):
    tokens = [word for word in jieba.cut(s) if word.strip() != ""]
    return " ".join(["".join(tokens[i:i + 2]) for i in range(len(tokens) - 1)])


@app.route("/", methods=["GET", "POST"])
def index():
    current_page = int(request.form.get("current_page", 1))
    page_size = int(request.form.get("page_size", 10))
    keyword = request.form.get("课程名称/课程信息", "")
    is_reverse_time = int(request.form.get("is_reverse_time", 1))
    if is_reverse_time:
        order = -1
    else:
        order = 1
    order_by = "time"
    n = len(list(jieba.cut(keyword)))
    if n < 2:
        condition = {
            "title": {"$regex": f".*{keyword}.*"}
        }
    else:
        condition = {
            "$text": {"$search": bi_tokenize(keyword)}
        }
    '''count = 1#topic_col.find(condition).count()'''
    page = Page(current_page, page_size, count)
    '''topics = topic_col.find(
        condition
    ).sort([(order_by, order)]).skip(page.start).limit(page.page_size)'''
    return render_template(
        "indexCopy.html"
        , topics=1#topics
        , is_reverse_time=is_reverse_time
        , keyword=keyword
        , count=1#count
        , page=1#page
    )


class Page(object):
    def __init__(self, current_page, page_size, count):
        self.current_page = current_page
        self.page_size = page_size
        self.count = count
        self.max_page = int((count + page_size - 1) / page_size)
        self.max_page = max(self.max_page, 1)
        self.current_page = min(self.current_page, self.max_page)
        self.start = (self.current_page - 1) * page_size
        self.start = 0 if self.start < 0 else self.start
        self.end = self.start + page_size
        self.begin_page, self.end_page = \
            self.page_range(self.current_page, self.max_page)

    def page_range(self, current_page, max_page):
        begin_page, end_page = 1, 1
        if max_page < 15:
            begin_page = 1
            end_page = max_page
        else:
            begin_page = current_page - 7
            end_page = current_page + 7
            if begin_page < 1:
                begin_page = 1
                end_page = 15
            elif end_page > max_page:
                end_page = max_page
                begin_page = max_page - 15
        return int(begin_page), int(end_page)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
