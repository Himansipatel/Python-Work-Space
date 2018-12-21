import pandas as pd

from flask import Flask,request #Flask use to write api in python
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/preview")
def preview():
    df2=pd.read_csv("physician_rx.csv")
    preview_df=df2.head()
    #preview_df.to_json(orient='records')
    return preview_df.to_html()


@app.route("/column/<column_name>")
def column_preview(column_name):
    df2=pd.read_csv("physician_rx.csv")
   # preview_df=df2[[column_name]]
   # preview_df=df2[column_name].to_frame
    #preview_df.to_json(orient='records')
    return df2[column_name].to_frame().to_html()



@app.route("/columnno")
def columnno():
    df2=pd.read_csv("physician_rx.csv")
    row_count=request.args.get("rows",type=int,default=5)
    prewiew_df=df2.iloc[0:row_count]
    return prewiew_df.to_html()


@app.route("/previeww")
def previeww():
    start = request.args.get("start" , type=int , default = 0)
    end = request.args.get("end" , type=int , default = 5)
    column_str =request.args.get("columns" , type=str , default = "0") #0,2,5
    li = column_str.split(",")
    colums=[]
    for index in li:
        colums.append(int(index))
    df2=pd.read_csv("physician_rx.csv")
    prewiew_df=df2.iloc[start:end,colums]
    return prewiew_df.to_html()

@app.route("/previewsearch")
def previewsearch():
    name = request.args.get("name" , type=str)
    operator =  request.args.get("operator" , type=str)
    value = request.args.get("value" , type=float , default = 5)
    df2=pd.read_csv("physician_rx.csv")
    if(operator == "less than"):
        return df2[df2[name] < value].to_html()
    elif(operator == "greater than"):
        return df2[df2[name] > value].to_html()
    elif(operator == "equal to"):
        return df2[df2[name] == value].to_html()
    
  #  prewiew_df=df2[df2[name] operator value ]
   # prewiew_df=df2.iloc[start:end,colums]
    #return prewiew_df.to_html()

if __name__ == "__main__":
    app.run()