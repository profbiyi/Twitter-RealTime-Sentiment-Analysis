from flask import Flask, render_template, request, url_for, redirect, flash
from api import twitter_keywords


app = Flask(__name__) 
app.secret_key = 'uguqifg;bacihvwbiwyriyesklnl831980-12983y8u9'

streams_list = []
my_routes = {
 
     "MD": ["Global Expense Overview", "Expense"]
  
}


# views 
views = [
    # (view_name, report_id)
("Expense_Analysis", "4f98d4f7-7033-46d4-8fa1-746b9b36ad90"),
("Expense", "4f98d4f7-7033-46d4-8fa1-746b9b36ad90")

]



@app.route("/")                   
def home():                      
    return render_template("index.html")


@app.route("/dashboard")
def render_view():
    # check if user has access to view
   
    # render the first view
    _, report_id = views[0]

    return render_template("report.html", my_routes=my_routes["MD"], 
        reportId=report_id, active_view=None)


@app.route('/streaming', methods=('POST', 'GET'))                  
def streaming():    
    print(">>>>>>>>>>>>>>>>",streams_list)
    if request.method == "POST":
        keywords = request.form.get('keywords', '')
        keywords = [keyword.strip() for keyword in keywords.split(',')]
        stream = twitter_keywords(keywords)
        streams_list.append({"stream": stream, "id": len(streams_list) + 1, "title": keywords })
        flash('Your keywords have been received')
        return redirect(url_for('streaming'))
    
    return render_template('streaming.html', streams_list=streams_list)


@app.route('/delete_stream', methods=('POST',))
def delete_stream():
  stream_id = request.form.get('stream_id')
  streams_list = list(filter(lambda stream: stream["id"] != stream_id, streams_list))
  return redirect(url_for('streaming'))





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)